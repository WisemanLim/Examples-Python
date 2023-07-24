#!/bin/bash
# find ./in -type f -name "*.mov" -exec sh -c 'sh pdf_convert.sh "$(basename "{}" )"' \; -o -exec sudo mv "{}" ~/.Trash/ \;
# for file in $(find ./in -type f -name "*.mov");
processing_files=0
find . -name "*.mov" -print0 | while read -d $'\0' file
do
	echo "Convert : [ "$file" ] => [ $(basename "$file") ]"
	sh pdf_convert.sh "$(basename "$file")"
	mv "$file" ~/.Trash/.
	((processing_files=processing_files+1))
	echo "Current completed files : "$processing_files""
done
