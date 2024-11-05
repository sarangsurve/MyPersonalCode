#!/bin/bash

files=("abc.py" "def.py" "ghi.py")

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        file_content=$(<"$file")

        details_content=$(echo "$file_content" | grep -oP 'details = \{.*?\}')

        if [ -n "$details_content" ]; then
            details_content=$(echo "$details_content" | awk -F '{' '{print $2}' | awk -F '}' '{print $1}')
            echo "Content from $file:"
            echo "$details_content}"
            echo "---"
        else
            echo "Details not found in $file."
            echo "---"
        fi
    else
        echo "$file not found."
        echo "---"
    fi
done






Requirements/Problem Statement: As part of data modernization, we aimed to create a sample ingestion pipeline using the DIFW framework to convert Parquet data into Delta format and catalog it in Unity Catalog. This included three ingestion flows: Parquet to Unity Catalog, Parquet to Delta, and Delta to Unity Catalog.

Implementation: The development encountered an initial blocker related to accessing secrets from the Databricks role, which required updated permissions. The AWS team assisted in resolving this access issue, allowing the necessary permissions for secret management.

Outcome: With the access issue resolved, development was completed successfully. The DIFW framework now supports seamless conversions from Parquet to Delta and Unity Catalog, meeting ingestion requirements and enhancing data accessibility in Unity Catalog.



