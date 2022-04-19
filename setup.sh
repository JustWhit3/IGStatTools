#!/bin/bash

# Setting-up the environment
echo "Setting-up the environment..."
python -m virtualenv IGenv
source IGenv/bin/activate
echo "Done!"

# Extra Python paths
export PYTHONPATH=src:$PYTHONPATH