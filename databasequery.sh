#!/bin/bash
#$ -N query_database
#$ -j y    # join output and error

# setup 
module load python/3.12.3
module load gcc/12.2.0

# cd to project home 
cd ~/projects/execs

# activate virtual environment to access packages
source pyenv/bin/activate

# edecute script 
python "code/databasequery.py"