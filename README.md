# Usage:

AVAILABLE OPTIONS:  
NOTE : POSTGRES FUNCTIONS ARE NOT YET READY  
----------------------------------------------------------------------------------------------------
```verification:  
    --verify_static         : verifies all the required static files
----------------------------------------------------------------------------------------------------
backup:
    --backup_mysql          : creates backup of mysql db
    --backup_postgres       : creates backup of postgres db

----------------------------------------------------------------------------------------------------
mysql:
    --mysql_help            : prints this help text
    --build_mysql           : builds the custom mysql db from Dockerfile
    --start_mysql           : starts the mysql container with default variables
    --connect_mysql         : connect to mysql db
    --log_mysql             : follows the mysql contianer's log
    --show_all_db_mysql     : shows all the available db in mysql container db
    --db_query_mysql        : execute query in db ```
----------------------------------------------------------------------------------------------------
postgres:
    --postgres_help         : prints this help text
    --build_postgres        : builds the custom postgres db from Dockerfile
    --start_postgres        : starts the postgres container with default variables
    --connect_postgres      : connect to postgres db
    --log_postgres          : follows the postgres contianer's log
    --show_all_db_postgres  : shows all the available db in postgres container db
    --db_query_postgres     : execute query in db
----------------------------------------------------------------------------------------------------
docker:
    --docker_help           : show docker official help
    --restart_docker        : restart docker service (root access needed)
    --status_docker         : shows that docker stat
    --docker_info           : shows the docker configuration , same as (docker info) command
    --docker_images         : shows the list of docker images
    --docker_ps             : shows running docker containers
    --docker_build          : build docker container from current path (Dockerfile required)
