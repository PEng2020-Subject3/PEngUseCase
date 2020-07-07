#!/usr/bin/env sh
python3 -m venv venv
source venv/bin/activate

pip install -r indiv-scores/requirements.txt
pip install -r driver-scores/requirements.txt
pip install -r performance-scores/requirements.txt

