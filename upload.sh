#!/bin/bash
read username password<date.txt
current_pwd=$(pwd)
echo $username:$password

for f in $current_pwd/*
do
cd $f
pwd

./auto_upload.sh $username $password
done

