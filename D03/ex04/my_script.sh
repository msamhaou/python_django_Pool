#!/bin/sh

python3 -m venv django_venv
source django_venv/bin/activate
python3 -m pip install --upgrade pip
pip --version
pip3 install -r requirement.txt
