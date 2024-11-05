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






Requirements/Problem Statement: The SSL/TLS certificates used by EMR clusters are self-signed and must be renewed annually to ensure secure data encryption over the network. The current certificates are set to expire on November 21, 2024, and must be renewed to prevent disruptions to PMR production jobs.

Implementation: The USDH team has completed the renewal of the self-signed SSL certificates for EMR in the DEV environment, establishing a tested approach. The RMO team is now set to replicate this renewal process in higher environments to secure the EMR clusters for production.

Outcome: This staged renewal approach ensures continuity for PMR production operations by mitigating potential impacts of certificate expiration, confirming security and stability in DEV, and preparing for seamless deployment in production.

