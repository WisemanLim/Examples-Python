find ./in -type f -name "*.mov" -exec sh -c 'sh pdf_convert.sh "$(basename "{}" )"' \;
