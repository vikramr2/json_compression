#!/bin/bash 
DIR="$(cd "$(dirname "$0")" && pwd)"

python3 $DIR/scripts/change_format.py $1 &> /dev/null
python3 $DIR/scripts/json_compression.py $1

