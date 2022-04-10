#!/bin/bash

# Setting-up the environment
echo "Setting-up the environment..."
python -m virtualenv IGenv
source IGenv/bin/activate
echo "Done!"

# Installing prerequisite modules
echo "Installing prerequisite modules..."
pip install -r requirements.txt
echo "Done!"

# Adding path of utils
export PYTHONPATH=${PWD}/utils:$PYTHONPATH