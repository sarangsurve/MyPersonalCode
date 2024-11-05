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






Requirements/Problem Statement: During the MCS 2.0 migration, USDH transitioned the integration bucket com-merck-hhieus-test-integration to HHIE accounts, with access granted to IAM user arn:aws:iam::004109663796:user/srvhhie-us-integration. However, Informatica applications are experiencing access failures, returning errors that suggest bucket access issues or potential misconfiguration in region settings.

Implementation: The issue was traced to DNS usage (usdh01.hhie.tst.merck.com) in Redshift connections within Informatica. A temporary solution was provided, advising the use of an alternate Redshift JDBC connection string for stability: jdbc:redshift://hhieusdhrst01.cpdsnhacsfma.us-east-1.redshift.amazonaws.com:25881/ghhusddwrs02?ssl=true

Outcome: This workaround allows continued Informatica operations while the root cause is being investigated with the Informatica vendor. A DevSecOps ticket has also been referenced by Santosh Singh for further tracking and resolution.

