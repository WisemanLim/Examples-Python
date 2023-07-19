#!/bin/bash
if [ "$#" -lt 2 ]
then
  echo "Usage : pdf_delete.sh filename pages:'10-12,20,30-35'"
  exit 1
fi

cd /Volumes/MyWorks_WD/Documents/PycharmProjects/Examples-Python/Video2PDF
source ../venv/bin/activate
python3 video2pdf.py --filename "$1" --env skip --delete "$2" --merge full
deactivate
