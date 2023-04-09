#!/bin/bash

sed -rni '/^[0-9]{2}\/[0-9]{2}\/[0-9]{4}/p' $1
python budget.py $1

