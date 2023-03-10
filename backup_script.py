#!/usr/bin/env python3

import os, sys, platform
from datetime import datetime
import zipfile
import tarfile

# var color ------------------------
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
EC = "\033[0m"

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
backup_dest_path = "/data/backup/" # if data partition doesn't exist change it
backup_count = 9
local_db_path = "mysql_db"
mysql_backup_name = "mysql_backup"
mysq_backup_content = ['mysql_db','static_data']
postgres_backu_name = "postgres_backup"
postgres_backu_content= ['postgres_db','static_data']

# line generator
def lines():
    print("-"*100)
# end of line generator

# backup functions
class backup:
    def linux():
        print(f'creating backup from {local_db_path} to {backup_dest_path}')
        os.chdir(backup_dest_path)
        os.system(f'tar -czf {mysql_backup_name}.{year}{month}{day}.{hour}.{minute}.tar.gz {current_path}/{local_db_path}') 
        print(f'{GREEN}backup completed{EC}')
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
    print(f'script is running on linux machine')
    lines()
    backup.linux()
elif "windows" in machine_os:
    print(f'script is running on windows machine')
else:
    print(f'script running on unknown os')
    
    sys.exit(1)
# end of os detector ----------------------------------------


