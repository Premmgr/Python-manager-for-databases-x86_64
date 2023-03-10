#!/usr/bin/env python3
import os
import sys
import time

# var color ------------------------
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
EC = "\033[0m"
# end of color var -------------
# basic var
status_ok = f"{GREEN}OK{EC}"
status_failed = f"{RED}Failed{EC}"


# general required files
required_files = ['mysql', 'mysql_db', 'postgres', 'mysql_init.sql']


docker_build_version = "v1.0"
docker_build_name = "stage_database"
static_path = "static_data"
postgres_default_path = f'{static_path}/postgres'
mysql_default_path = f'{static_path}/mysql'

# mysql var
pull_mysql_image_version = "5.7"
mysql_container_name = "mysql_stage_db"
mysql_run_port = "3306"
mysql_restart_policy = "unless-stopped"
mysql_default_local_db_path = "mysql_db"
mysql_default_root_password = "stage"

# postgres var
pull_postgres_image_version = "14"
postgres_container_name = "postgres_stage_db"
postgres_run_port = "3306"
postgres_restart_policy = "unless-stopped"
postgres_default_local_db_path = "postgres_db"
postgres_default_root_password = "stage"

# msg
docker_build_success_msg = "docker image build success"
docker_build_error_msg = f"{RED}error while building docker image{EC}"

current_path = os.getcwd()

# general functions -----------------------------
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
        print(f'postgres run process: {status_ok}')

    # docker rmi functions
    def rmi_mysql():
        os.system(f'docker rmi mysql:{pull_mysql_image_version}')
    def rmi_postgres():
        os.system(f'docker rmi postgres:{pull_postgres_image_version}')
    
    # docker build fucntions
    def buil_mysql():
        os.chdir(mysql_default_path)
        os.system(f'docker build -t {docker_build_name}:{docker_build_version} .')
        print(f'mysql build process: {status_ok}')
    def buil_postgres():
        os.chdir(postgres_default_path)
        os.system(f'docker built -d {docker_build_name}_postgres:{pull_postgres_image_version}')
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

# end of class docker sections ----------------------------------------------------

# verification function
def verify_static_files():
    passed_files = []
    failed_files = []
    print(f'checking required files in <{static_path}>')
    # checks if all the required files are in static path
    for file in required_files:
        if file in os.listdir(static_path):
            print(f'status {file}:',status_ok,)
            passed_files.append(file)
            sleep(0.1)  
        else:
            print(f'status {file}:',status_failed)
            failed_files.append(file)
            sleep(0.1)
    # end of verification message
    if passed_files == required_files:
        print(f'\nverification completed, no files are missing')
        sys.exit(0)
    else:
        print(f'\nverfification failed, please check if following files exist in {static_path}\n', failed_files)
        sys.exit(1)
#-----------------------------------------------------------------------------


def alter_function():
    pass

# db connections
class conn_db:
# mysql section
    # connects to mysql db
    def connect_mysql():
        os.system(f'docker exec -it {mysql_container_name} mysql --password={mysql_default_root_password} --user=root')

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
        os.system(f'docker exec -i {mysql_container_name} mysql --password={mysql_default_root_password} --user=root -e "SHOW DATABASES;"')
        #  docker exec -i container_name mysql --password=db_password --user=root -e "queries"
        # -u $MYSQL_USER -p $MYSQL_PASSWORD $MYSQL_DATABASE < epcis_schema.sql

    #db queries
    def exec_db_mysql():
        try:
            exec_value = input("enter query: \n")
            os.system(f'docker exec -i {mysql_container_name} mysql --password={mysql_default_root_password} --user=root -e "{exec_value}"')
        except:
            print(f'\n{RED}db query exec terminated for {mysql_container_name}{EC}')



# postgres section (continue here)
# --------------------------------

# help section -------------------------------------------------
def lines():
    print('---------------------------------------------------------------------------')

def general_help():
    print(f'{YELLOW}AVAILABLE OPTIONS: {EC}')
    print(f'{RED}NOTE : POSTGRES FUNCTIONS ARE NOT YET READY{EC}')
    mysql_help()
    postgres_help()


def postgres_help():
    lines()
    print(f"""postgres: 
--postgres_help        (prints this help text)
--build_postgres       (builds the custom postgres db from Dockerfile)
--start_postgres       (starts the postgres container with default variables)
--connect_postgres     (connect to postgres db)
--log_postgres         (follows the postgres contianer's log) 
--show_all_db_postgres (shows all the available db in postgres container db)
--db_query_postgres    (execute query in db)    """)
    
def mysql_help():
    lines()
    print(f"""mysql:
--mysql_help        (prints this help text)
--build_mysql       (builds the custom mysql db from Dockerfile)
--start_mysql       (starts the mysql container with default variables)
--connect_mysql     (connect to mysql db)
--log_mysql         (follows the mysql contianer's log) 
--show_all_db_mysql (shows all the available db in mysql container db)
--db_query_mysql    (execute query in db)   """)

# end of help section -------------------------------------------------




# entrypoints --------------------------------------
options = f'--help, --verify_static, --log_mysql, --show_all_db_mysql, --docker_ps, --start_mysql, --stop_mysql, --build_mysql, --restart_docker, --connect_db_mysql, --db_query_mysql'
if len(sys.argv)<2:
    print(f'{RED}invalid option{EC}')
    print(f'try: {options}')
    sys.exit(1)

print("used command: ", sys.argv)


# end of entrypoint ---------------------------------

# args
arg1 = sys.argv[1]

# verifies static files
if arg1 == "--help":
    general_help()
if arg1 == "--verify_static":
    verify_static_files()
# show sthe mysql log
if arg1 == "--log_mysql":
    docker.log_mysql()
# connects to mysql db
if arg1 == "--show_all_db_mysql":
    conn_db.show_all_mysql_db()
# shows the running docker containers
if arg1 == "--docker_ps":
    docker.ps()
# start mysql container with default mysql image (not the custom built one)
if arg1 == "--start_mysql":
    docker.start_mysql()
# stops the mysql container (not the custom built one)
if arg1 == "--stop_mysql":
    docker.stop_mysql()
# builds the custom image from mysql official image (file are in static_data)
if arg1 == "--build_mysql":
    docker.buil_mysql()
# restart docker
if arg1 == "--restart_docker":
    docker.restart_docker()

if arg1 == "--connect_db_mysql":
    conn_db.connect_mysql()
if arg1 == "--mysql_help":
    mysql_help()
if arg1 == "--db_query_mysql":
    conn_db.exec_db_mysql()

# # db query agrs
# db_queries = sys.argv[2]

