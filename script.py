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

'''
Subject: Deployment Failure in [DIFW_manual] Dataset CD Workflow Post Airflow Upgrade

Email:

Hi Team,

Following the recent Airflow upgrade, we have been implementing necessary changes to address issues caused by the update. One of the impacted DAGs failed due to missing modules in the upgraded apache-airflow-providers-amazon package (from v3.3.0 to v9.1.0), specifically redshift_sql and s3_delete_object.

We successfully remediated the changes and deployed two dataset DAGs. However, while the third DAG builds successfully via the [DIFW_manual] Dataset CI workflow (<CI-job-link>), it fails during deployment through the [DIFW_manual] Dataset CD workflow (<CD-job-link>), with the following error:

TypeError: GlueConnection.__init__() got an unexpected keyword argument 'connection_type'

We have reviewed the dataset_definition.yaml file and found no issues. This DAG was previously deployed successfully before the upgrade.

Could someone please assist in identifying and resolving the root cause of this deployment error?
'''