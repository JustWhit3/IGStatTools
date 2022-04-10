#!/bin/bash

# Setting-up the environment
echo "Setting-up the environment..."
python -m virtualenv IGenv
source IGenv/bin/activate

# Adding path of utils
echo "Done!"
export PYTHONPATH=${PWD}/utils:$PYTHONPATH