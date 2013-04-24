#!/bin/bash

python get_latest.py
if [ $? -eq 0 ]
then
	
    git commit -a -m "Updated archive on $(date)"
    git push origin master
fi
