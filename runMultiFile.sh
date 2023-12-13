#! /usr/bin/bash
cd /home/ec2-user/data/COMP0235
source ~/data/virtualenv/venv/bin/activate
for filename in test/*.fa; do
  python ./pipeline_script.py "$filename"
done
