# Instrucciones de uso
Abre el fichero `docker-compose.yml` y edítalo para cambiar el nombre de los dos contenedores para que, como prefijo, se use tu nombre y no el mío.

Además, cambia el puerto que se expone al exterior de `8080` al `80<número de alumno con dos dígitos>`. Por ejemplo, si eres el alumno `alu03` entonces usa como puerto el `8003`. Si eres el alumno `alu17` entonces usa como puerto el `8017`.

Tras esos cambios puedes levantar los contenedores con la orden `docker compose up -d`.

Una vez levantados, a través del navegador web entra al servidor con su IP y el puerto que has usado.
