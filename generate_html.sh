#!/bin/bash

# Function to generate the HTML
generate_html() {
    echo "<html><head><title>Monitor de Procesos de macOS</title></head><body>"
    echo "<h1>Procesos Actuales</h1>"
    echo "<form action='/kill_process' method='POST'>"
    echo "<label for='process'>Selecciona un proceso para cancelar:</label><br>"
    echo "<select name='process'>"

    # Updated `ps` command for macOS compatibility
    ps -Ao pid,comm | tail -n +2 | while read pid comm; do
        echo "<option value='$pid'>$comm ($pid)</option>"
    done

    echo "</select><br>"
    echo "<button type='submit'>Cancelar Proceso</button>"
    echo "</form>"
    echo "</body></html>"
}

# Generate the HTML file
generate_html > /var/www/process_monitor/index.html

