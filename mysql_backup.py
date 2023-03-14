#!/usr/bin/env python3

import os, sys, platform
from datetime import datetime
from env_modules import colors
from env_modules.environment import var

# date var
now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute

# backup var section
current_path = os.getcwd()
list_files = os.listdir()
posix_backup_dest_path = var("posix_backup_dest_path") # if data partition doesn't exist change it
backup_count = 9
local_db_path = "mysql_db"
static_data_path = "static_data"
mysql_backup_name = "mysql_backup"
mysq_backup_content = ['mysql_db','static_data']
postgres_backu_content= ['postgres_db','static_data']

# line generator
def lines():
    print("-"*100)
# end of line generator

# backup functions
class backup:
    def linux():
        print(f'creating backup from {local_db_path} to {posix_backup_dest_path}')
        os.chdir(posix_backup_dest_path)
        os.system(f'tar -czf {mysql_backup_name}.{year}{month}{day}.{hour}.{minute}.tar.gz {current_path}/{local_db_path} {current_path}/{static_data_path}') 
        print(f'{colors.green}backup completed{colors.ec}')
    # def windows():
    #     # continue here

        



# runtime os detector --------------------------------------
machine_os = []
def check_host_os():
    detected_os = platform.system()
    if "Linux" in detected_os:
        machine_os.append("linux")
    if "Windows" in detected_os:
        machine_os.append("windows")
check_host_os()

if "linux" in machine_os:
    print(f'{colors.green}script is running on linux machine{colors.ec}')
    lines()
    backup.linux()
elif "windows" in machine_os:
    print(f'{colors.green}script is running on windows machine{colors.ec}')
else:
    print(f'{colors.red}script running on unknown os{colors.ec}')
    
    sys.exit(1)
# end of os detector ----------------------------------------

