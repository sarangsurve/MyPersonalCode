#!/bin/bash

file_content=$(<your_file.txt)

details_content=$(echo "$file_content" | grep -oP 'details = \{.*?\}')

if [ -n "$details_content" ]; then
    details_content=$(echo "$details_content" | awk -F '{' '{print $2}' | awk -F '}' '{print $1}')
    echo "$details_content}"
else
    echo "Details not found in the file."
fi
