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






Requirements/Problem Statement:
The Black Duck scan identified critical vulnerabilities within specific Lambda layers, "AWSUSGHHUSDWD-CSTMAwsMicroservice" and "AWSUSGHHUSDWT-CirrusAdmnUINodePackages." Vulnerable components included python-certifi-2018.11.29, json-schema-0.2.2 and 0.2.3, and tough-cookie-v2.5.0. To mitigate security risks, updates to these components were required to eliminate vulnerabilities in our development and testing environments.

Implementation:
We updated vulnerable packages with secure versions: python-certifi-0.4.0, json-schema-2024.02.02, and tough-cookie-5.0.0-rc.1. Additionally, deprecated packages, like request, were removed from the Lambda layer "AWSUSGHHUSDWT-CirrusAdmnUINodePackages." A new build was created and redeployed to apply these updates.

Outcome:
Post-update Black Duck scans confirmed that all critical vulnerabilities were resolved. The updated Lambda layers were validated for stability, and functionality was thoroughly tested in the Admin UI, confirming no adverse impacts. Development is now complete with secure, stable, and tested Lambda layers.

Just note this