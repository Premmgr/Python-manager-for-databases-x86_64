#!/usr/bin/env python3
import os
import sys
import time
from env_modules import colors
from env_modules.environment import var
static_path = "static_data"
postgres_default_path = f'{static_path}/postgres'
mysql_default_path = f'{static_path}/mysql'


docker_build_version = var("docker_build_version")
docker_build_name = var("docker_build_name")
static_path = var("static_path")

# mysql var
pull_mysql_image_version = var("pull_mysql_image_version")
mysql_container_name = var("mysql_container_name")
mysql_run_port = var("mysql_run_port")
mysql_restart_policy = var("mysql_restart_policy")
mysql_default_local_db_path = var("mysql_default_local_db_path")
mysql_default_root_password = var("mysql_default_root_password")

# postgres var
pull_postgres_image_version = var("pull_postgres_image_version")
postgres_container_name = var("postgres_container_name")
postgres_run_port = var("postgres_run_port")
postgres_restart_policy = var("postgres_restart_policy")
postgres_default_local_db_path = var("postgres_default_local_db_path")
postgres_default_root_password = var("postgres_default_root_password")

# status var
status_ok = f"{colors.green}OK{colors.ec}"
status_failed = f"{colors.red}Failed{colors.ec}"


current_path = os.getcwd()

# general functions -----------------------------


def lines():
    print('-'*100)


def sleep(self):
    return time.sleep(self)


def check_path(self):
    os.path.exists(self)


def check_file(self):
    os.path.isfile(self)
# end of general function -----------------------

# docker section -------------------------------------------------------


class docker:
    # pull function
    def pull_mysql():
        os.system(f'docker pull mysql:{pull_mysql_image_version}')
        print(f'mysql pull process: {status_ok}')

    def pull_postgres():
        os.system(f'docker pull postgres:{pull_postgres_image_version}')
        print(f'mysql pull process: {status_ok}')

    # show running containers
    def ps():
        os.system(f'docker ps')

    def ps_mysql():
        return os.system(f'docker ps -f name={mysql_container_name}')

    def ps_postgres():
        return os.system(f'$(docker ps -f name={postgres_container_name})')

    # docker container start
    def start_mysql():
        os.system(f'docker run -d --name {mysql_container_name} -p {mysql_run_port}:3306 --restart {mysql_restart_policy} -v ./{mysql_default_local_db_path}:/var/lib/mysql -e MYSQL_ROOT_PASSWORD={mysql_default_root_password} mysql:{pull_mysql_image_version}')

    def start_postgres():
        os.system(f'docker run -d --name {postgres_container_name} -p {postgres_run_port}:3306 --restart {postgres_restart_policy} -v ./{postgres_default_local_db_path}:/var/lib/postgres -e MYSQL_ROOT_PASSWORD={mysql_default_root_password} mysql:{pull_mysql_image_version}')

    # docker rmi functions
    def rmi_mysql():
        os.system(f'docker rmi mysql:{pull_mysql_image_version}')

    def rmi_postgres():
        os.system(f'docker rmi postgres:{pull_postgres_image_version}')

    # docker build fucntions
    def buil_mysql():
        os.chdir(mysql_default_path)
        os.system(
            f'docker build -t {docker_build_name}:{docker_build_version} .')
        print(f'mysql build process: {status_ok}')

    def buil_postgres():
        os.chdir(postgres_default_path)
        os.system(
            f'docker built -d {docker_build_name}_postgres:{pull_postgres_image_version}')
        print(f'postgres build process: {status_ok}')

    # show logs
    def log_mysql():
        os.system(f'docker logs -f {mysql_container_name}')

    def log_postgres():
        os.system(f'docker logs -f {postgres_container_name}')

    # stop container
    def stop_mysql():
        print(f'stopping {mysql_container_name} container')
        os.system(f'docker stop {mysql_container_name}')
        print(f'removing stopped {mysql_container_name} container')
        os.system(f'docker rm {mysql_container_name}')

    def stop_postgres():
        os.system(f'docker stop {postgres_container_name}')

    # general system docker functions
    def restart_docker():
        os.system(f'systemctl restart docker')

    def docker_help():
        os.system(f'docker --help')

    def status():
        os.system(f'docker stat')

    def info():
        return os.system(f'docker info')
    
    def images():
        return os.system(f'docker images')
    
    def build():
        image_name = input(f'image name: ')
        image_version = input(f'tag version: ')
        os.system(f'docker build -t {image_name}:{image_version}')
        

# end of class docker sections ----------------------------------------------------


# db connections
class conn_db:
    # mysql section
    # connects to mysql db
    def connect_mysql():
        os.system(
            f'docker exec -it {mysql_container_name} mysql --password={mysql_default_root_password} --user=root')

# fix init.sql fucntions
    # init the db with sql file
    # def init_mysql_db():
    #     if os.system(f'docker ps | grep {mysql_container_name}'):
    #         os.chdir(static_path)
    #         os.system(f'docker run -d --name {mysql_container_name} -p {mysql_run_port}:3306 --restart {mysql_restart_policy} -v ./{mysql_default_local_db_path}:/var/lib/mysql -e MYSQL_ROOT_PASSWORD={mysql_default_root_password} mysql:{pull_mysql_image_version}')
    #         os.system(
    #             f'docker exec -i {mysql_container_name} mysql --password={mysql_default_root_password} --user=root < mysql_init.sql')
    #     else:
    #         os.system(
    #             f'docker stop {mysql_container_name} && docker rm {mysql_container_name}')
    #         print(f"containers stopped and removed: {mysql_container_name}")
    def show_all_mysql_db():
        # connects to docker my docker container and show the db
        os.system(
            f'docker exec -i {mysql_container_name} mysql --password={mysql_default_root_password} --user=root -e "SHOW DATABASES;"')
        #  docker exec -i container_name mysql --password=db_password --user=root -e "queries"
        # -u $MYSQL_USER -p $MYSQL_PASSWORD $MYSQL_DATABASE < epcis_schema.sql

    # db queries
    def exec_db_mysql():
        try:
            exec_value = input("enter query: \n")
            os.system(
                f'docker exec -i {mysql_container_name} mysql --password={mysql_default_root_password} --user=root -e "{exec_value}"')
        except:
            print(
                f'\n{colors.red}db query exec terminated for {mysql_container_name}{colors.ec}')

    def show_all_postgres_db():
        pass

    def exec_db_postgres():
        pass


# postgres section (continue here)
# --------------------------------

def alter_function():
    pass


# verification function
required_files = ['mysql', 'postgres', 'mysql_init.sql']


def static_files_check():
    passed_files = []
    failed_files = []
    print(f'checking required files in <{static_path}>')
    # checks if all the required files are in static path
    for file in required_files:
        if file in os.listdir(static_path):
            print(f'status {file}:', status_ok,)
            passed_files.append(file)
            sleep(0.1)
        else:
            print(f'status {file}:', status_failed)
            failed_files.append(file)
            sleep(0.1)
    # end of verification message
    if passed_files == required_files:
        print(f'\nverification completed, no files are missing')
        sys.exit(0)
    else:
        print(
            f'\nverfification failed, please check if following files exist in {static_path}\n', failed_files)
        sys.exit(1)
# -----------------------------------------------------------------------------

# help section -------------------------------------------------


class help:

    def general_help():
        print(f'{colors.yellow}AVAILABLE OPTIONS: {colors.ec}')
        print(f'{colors.red}NOTE : POSTGRES FUNCTIONS ARE NOT YET READY{colors.ec}')
        help.verification()
        help.backup()
        help.mysql_help()
        help.postgres_help()
        help.docker_help()

    # help function
    def verification():
        lines()
        print(f"""verification:
    --verify_static         : verifies all the required static files """)

    def backup():
        lines()
        print(f"""backup:
    --backup_mysql          : creates backup of mysql db
    --backup_postgres       : creates backup of postgres db
        """)

    # postgres help
    def postgres_help():
        lines()
        print(f"""postgres: 
    --postgres_help         : prints this help text
    --build_postgres        : builds the custom postgres db from Dockerfile
    --start_postgres        : starts the postgres container with default variables
    --connect_postgres      : connect to postgres db
    --log_postgres          : follows the postgres contianer's log 
    --show_all_db_postgres  : shows all the available db in postgres container db
    --db_query_postgres     : execute query in db    """)

    # mysql help
    def mysql_help():
        lines()
        print(f"""mysql:
    --mysql_help            : prints this help text
    --build_mysql           : builds the custom mysql db from Dockerfile
    --start_mysql           : starts the mysql container with default variables
    --connect_mysql         : connect to mysql db
    --log_mysql             : follows the mysql contianer's log 
    --show_all_db_mysql     : shows all the available db in mysql container db
    --db_query_mysql        : execute query in db   """)

    # docker help
    def docker_help():
        lines()
        print(f"""docker:
    --docker_help           : show docker official help
    --restart_docker        : restart docker service (root access needed)
    --status_docker         : shows that docker stat
    --docker_info           : shows the docker configuration , same as (docker info) command
    --docker_images         : shows the list of docker images
    --docker_ps             : shows running docker containers
    --docker_build          : build docker container from current path (Dockerfile required)   """)

# end of help section -------------------------------------------------


# entrypoint ----------------------------------------------------------
def options():
    if len(sys.argv) < 2:
        print(f'{colors.red}No option provided,{colors.ec}\n')
        help.general_help()
        sys.exit(1)

    print(f"{colors.green}passed command{colors.ec}: {colors.magenta}{sys.argv}{colors.ec}")

    # args
    arg1 = sys.argv[1]

    def input_arg():
        if arg1 == "--help":
            help.general_help()
        # verifies static files
        if arg1 == "--verify_static":
            static_files_check()
        # backup.py
        if arg1 == "--backup_mysql":
            os.system(f'./mysql_backup.py')
        if arg1 == "--backup_postgres":
            os.system(f'./postgres_backup.py')

        # postgres
        if arg1 == "--postgres_help":
            help.postgres_help()

        if arg1 == "--build_postgres":
            docker.buil_postgres()

        if arg1 == "start_postgres":
            docker.start_postgres()

        if arg1 == "--connect_postgres":
            conn_db.connect_postgres()

        if arg1 == "--log_postgres":
            docker.log_postgres()

        if arg1 == "--show_all_db_postgres":
            conn_db.show_all_postgres_db()
        if arg1 == "--db_query_postgres":
            conn_db.exec_db_postgres()

        # mysql
        if arg1 == "--build_mysql":
            docker.buil_mysql()

        if arg1 == "start_mysql":
            docker.start_mysql()

        if arg1 == "--connect_mysql":
            conn_db.connect_mysql()

        if arg1 == "--log_mysql":
            docker.log_postgres()

        if arg1 == "--show_all_db_mysql":
            conn_db.show_all_mysql_db()
        if arg1 == "--db_query_mysql":
            conn_db.exec_db_mysql()

        # docker
        if arg1 == "--docker_help":
            help.docker_help()
        
        if arg1 == "--restart_docker":
            docker.restart_docker()
        
        if arg1 == "--status_docker":
            docker.status()

        if arg1 == "--docker_info":
            docker.info()
        
        if arg1 == "--docker_ps":
            docker.ps()
        
        if arg1 == "--docker_images":
            docker.images()
        if arg1 == "--docker_build":
            docker.build()

    # continue

    input_arg()


if __name__ == "__main__":
    options()
# end of entrypoint ---------------------------------
