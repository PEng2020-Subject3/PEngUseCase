#!/usr/bin/env sh
echo "➡ Setting up virtual env"
python3 -m venv venv
source venv/bin/activate

echo "➡ Installing function dependencies"
pip install -r indiv-performancescores/requirements.txt
pip install -r indiv-driverscores/requirements.txt
pip install -r driver-scores/requirements.txt
pip install -r performance-scores/requirements.txt

