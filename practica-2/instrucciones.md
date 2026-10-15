Instrucciones:
* Instalar e iniciar el servicio de SSH
* Crear otro usuario estudiante_ssh para la conexión
* Probar de manera “normal” la conexión al otro usuario `estudiante_ssh` mediante ssh.
```
$ ssh estudiante_ssh@localhost
```
* Investigar medidas de seguridad para el servicio ssh
   En particular
   - port
   - ClientAliveInterval
   - ClientAliveCountMax
   - MaxAuthTries
   - LoginGraceTime
   - PermitRootLogin
   - Otras 3 de su preferencia
* Implementarlas en el archivo /etc/ssh/sshd_config
* Probar que la configuración se haya guardado
El entregable es un reporte de los pasos que hicieron, cómo lo fueron haciendo; más la investigación de las medidas de seguridad
