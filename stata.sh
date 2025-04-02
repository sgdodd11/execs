#!/bin/bash
#$ -N user_id_extraction
#$ -j y

# set home directory to analysis/do, where we would be locally, so that relative paths work. 
cd "$HOME/projects/execs"

# specify code file inside do
DOFILE0="code/user_id_extraction.do"
LOG0=$DOFILE0.${JOB_ID}$(if [[ ! ${SGE_TASK_ID} == 'undefined' ]]; then echo ".${SGE_TASK_ID}"; fi).log

stata-se do $DOFILE0 > $LOG0 2>&1 $@