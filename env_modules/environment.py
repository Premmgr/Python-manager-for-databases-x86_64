import os

# Read the .env file and store environment variables in a dictionary
env_dict = {}
with open("custom.env", "r") as f:
    for line in f:
        line = line.strip()
        if line.startswith("#") or not line:
            continue
        key, value = line.split("=", 1)
        env_dict[key] = value

# Access the MYSQL_PASSWORD variable from the dictionary
# print(env_dict.get("pull_mysql_image_version"))

def var(self):
    return env_dict.get(self)


