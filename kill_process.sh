#!/bin/bash

# Lee el ID del proceso desde la solicitud POST
read process_id

# Mata el proceso seleccionado
kill -9 "$process_id" 2>/dev/null
echo "Content-Type: text/html"
echo ""
echo "<html><body><h1>Proceso $process_id cancelado exitosamente</h1>"
echo "<a href='/'>Volver a la lista de procesos</a>"
echo "</body></html>"

