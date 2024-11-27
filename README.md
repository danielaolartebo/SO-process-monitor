# ***Monitor de Procesos***

*El proyecto consiste en la elaboración de dos herramientas (una en Powershell y una en bash) que faciliten las labores del administrador de un data center que posee máquinas Windows y Linux.*
*Las herramientas son las siguientes:*

## *1. Monitor de estado de los procesos de un servidor Windows*
*Este monitor debe ser accesible vía web, y debe tener las siguientes opciones:*
*Desplegar una tabla HTML de los procesos que corren actualmente en la máquina.*
*Cancelar uno de los procesos que estén corriendo, seleccionándolo de una lista. NO ES  VÁLIDO solicitar por teclado el ID del proceso... se debe marcar el proceso en una lista (es decir, hacer la operación lo más amigable posible).*  

## *2. Monitor de estado de un servidor Linux.*  
*Este monitor también debe ser accesible vía web, y ofrecer las siguientes opciones:* 
*Desplegar una tabla HTML de los procesos que corren actualmente en la máquina (la salida  debe ser HTML, NO se admite formato texto).*
*Cancelar uno de los procesos que estén corriendo, seleccionándolo de una lista. Aplica la  misma restricción que en el caso anterior.*

## ***Instrucciones*** 📦

*Bash:*

```bash
python POST_request.py
```

*Powershell:*

```powershell
POST_request.ps1
```

## ***Dificultades***

🔸*Implementar una interfaz web funcional y amigable fue un desafío, especialmente al integrar los comandos de PowerShell y Bash con tecnologías web. La configuración inicial para generar y actualizar dinámicamente una tabla HTML con los datos de los procesos requería trabajo adicional para manejar correctamente la comunicación entre el backend y la interfaz.*

🔸*En Linux, Bash surgieron problemas de permisos al intentar detener procesos que requerían privilegios administrativos, lo que exigió implementar una verificación adecuada de permisos.*

🔸*En Windows, PowerShell presentó problemas al manejar procesos con nombres duplicados o que finalizaban antes de la ejecución del comando de cancelación.*

## ***Conclusiones***📓

🔸*Este proyecto destacó las diferencias fundamentales entre la administración de procesos en Windows y Linux. Aunque ambos sistemas soportan tareas similares, su implementación y los comandos requeridos son muy distintos. Esto resalta la importancia de entender las particularidades de cada sistema operativo al desarrollar herramientas administrativas.*

🔸*Este proyecto mostró cómo automatizar tareas rutinarias puede simplificar la administración de un centro de datos y reducir errores humanos. La experiencia sugiere que herramientas similares podrían extenderse para incluir funciones adicionales, como el monitoreo del uso de recursos o alertas automáticas.*

🔸*Implementar restricciones para que solo usuarios con los permisos adecuados pudieran cancelar procesos fue un aspecto crítico. Este proyecto reforzó la importancia de validar cuidadosamente las acciones del usuario, especialmente en tareas administrativas sensibles.*


## ***Authors*** ✒️

<p align="left">
      <a href="https://github.com/gajokremer" target="_blank"> <img src="https://images.weserv.nl/?url=avatars.githubusercontent.com/u/83292625?v=4&h=60&w=60&fit=cover&mask=circle?v=4&h=60&w=60&fit=cover&mask=circle"></a>
  <a href="https://github.com/danielaolartebo" target="_blank"> <img src="https://images.weserv.nl/?url=avatars.githubusercontent.com/u/53228651?v=4&h=60&w=60&fit=cover&mask=circle"></a>
      <a href="https://github.com/SebastianZV010" target="_blank"> <img src="https://images.weserv.nl/?url=avatars.githubusercontent.com/u/84345055?v=4&h=60&w=60&fit=cover&mask=circle"></a>
</p>

---

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/for-you.svg)](https://forthebadge.com)
