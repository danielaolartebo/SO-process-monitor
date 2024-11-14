from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# Número máximo de procesos por página
PROCESS_PER_PAGE = 10

# HTML template with table and pagination
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Monitor de Procesos de Linux</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
        }
        h1 {
            text-align: center;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        table, th, td {
            border: 1px solid #ddd;
        }
        th, td {
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #4CAF50;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        tr:hover {
            background-color: #ddd;
        }
        .pagination {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        .pagination a {
            padding: 8px 16px;
            margin: 0 4px;
            text-decoration: none;
            background-color: #4CAF50;
            color: white;
            border-radius: 4px;
        }
        .pagination a:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h1>Procesos Actuales</h1>
    <form action="/kill_process" method="post">
        <table>
            <thead>
                <tr>
                    <th>Seleccionar</th>
                    <th>PID</th>
                    <th>Comando</th>
                </tr>
            </thead>
            <tbody>
                {% for pid, comm in processes %}
                    <tr>
                        <td><input type="radio" name="process" value="{{ pid }}"></td>
                        <td>{{ pid }}</td>
                        <td>{{ comm }}</td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
        <button type="submit">Cancelar Proceso</button>
    </form>

    <div class="pagination">
        {% if page > 1 %}
            <a href="/?page={{ page - 1 }}">Anterior</a>
        {% endif %}
        {% if page < total_pages %}
            <a href="/?page={{ page + 1 }}">Siguiente</a>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    # Obtener los procesos
    processes = []
    with os.popen("ps -Ao pid,comm | tail -n +2") as f:
        for line in f:
            pid, comm = line.strip().split(maxsplit=1)
            processes.append((pid, comm))

    # Paginación
    page = int(request.args.get('page', 1))
    total_processes = len(processes)
    total_pages = (total_processes // PROCESS_PER_PAGE) + (1 if total_processes % PROCESS_PER_PAGE > 0 else 0)

    # Calcular los índices de los procesos a mostrar en la página actual
    start_index = (page - 1) * PROCESS_PER_PAGE
    end_index = start_index + PROCESS_PER_PAGE

    # Extraer la sublista de procesos para la página actual
    processes_to_display = processes[start_index:end_index]

    return render_template_string(
        html_template,
        processes=processes_to_display,
        page=page,
        total_pages=total_pages
    )

@app.route('/kill_process', methods=['POST'])
def kill_process():
    pid = request.form.get('process')
    if pid:
        try:
            os.kill(int(pid), 9)  # Enviar SIGKILL al proceso
            return f"El proceso {pid} ha sido cancelado."
        except Exception as e:
            return f"Error al intentar cancelar el proceso {pid}. Error: {str(e)}"
    return "No se recibió el PID del proceso."

if __name__ == "__main__":
    app.run(port=7070)

