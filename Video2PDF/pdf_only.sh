#!/bin/bash
cd /Volumes/MyWorks_WD/Documents/PycharmProjects/Examples-Python/Video2PDF
source ../venv/bin/activate
python3 video2pdf.py --filename in --env pdf
deactivate