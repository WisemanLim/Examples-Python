#!/bin/bash
echo "$#"
if [ "$#" -lt 1 ]
then
  echo "Usage : pdf_convert.sh filename"
  exit 1
fi

cd /Volumes/MyWorks_WD/Documents/PycharmProjects/Examples-Python/Video2PDF
source ../venv/bin/activate
python3 video2pdf.py --filename "$1" --env full
deactivate
