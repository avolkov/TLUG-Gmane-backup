#!/bin/bash

python get_latest.py
if [ $? -eq 0 ]
then
    git commit
    git push origin master
fi