#!/bin/bash
sudo pip3 install -y virtualenv poetry
cd /home/ec2-user/app
virtualenv whale-api-venv
source whale-api-venv/bin/activate
sudo poetry install