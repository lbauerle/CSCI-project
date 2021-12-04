#!/bin/bash

# so we don't get an error
source /opt/conda/etc/profile.d/conda.sh

# activate conda environment
#conda activate swefs

# run code with arguments
python density_difference.py > output.txt

# deactivate conda environment
#conda deactivate