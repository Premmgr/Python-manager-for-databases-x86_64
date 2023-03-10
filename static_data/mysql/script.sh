#!/usr/bin/env bash
var_volume="db"
var_port="3306"
var_image_version="$3"
var_container_name="$2"
var_root_passwd="$4"
var_image_name="$3"
# run commands

case "$1" in
	"cli")
		docker run -d -p ${var_port}:3306 --name ${var_container_name} -e MYSQL_ROOT_PASSWORD=${var_root_passwd} ${var_image_name}:${var_image_version}
	;;
	"db")
		read -s -p "root password for db: " var_tpass
		docker run -d -p ${var_port}:3306 --name ${var_container_name} -e MYSQL_ROOT_PASSWORD=${var_tpass} ${var_image_name}:${var_image_version}
	;;
*)
	echo "invalid arg, try $0 db <container_name> <image_name>:<version>"
esac

