#!/bin/bash

pip --version
echo "check local_lib"

if [ -d "local_lib" ]; then
    echo "Reinstalling Path"
    rm -rf local_lib
else
    echo "installing Path" 
fi
mkdir local_lib
pip install --force-reinstall git+https://github.com/jaraco/path.git -t ./local_lib >> install.log


if [ $? -eq 0 ]; then
    python3 my_program.py
fi