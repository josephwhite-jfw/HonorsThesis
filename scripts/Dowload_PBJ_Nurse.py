#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import requests

# Set target directory
target_dir = r"C:\Users\Owner\OneDrive\Documents\Honors_Thesis\data\data-raw"

# Check it exists
os.makedirs(target_dir, exist_ok=True)

# CMS Data Nurse Staffing Levels API endpoint for the data catalog
api_url = "https://data.cms.gov/data.json"

# Fetch metadata
response = requests.get(api_url)
if response.status_code != 200:
    raise Exception(f"Failed to fetch data from CMS API. Status code: {response.status_code}")

data = response.json()

# Find the PBJ Daily Nurse Staffing dataset
pbj_dataset = None
for dataset in data['dataset']:
    if dataset['title'] == "Payroll Based Journal Daily Nurse Staffing":
        pbj_dataset = dataset
        break

if not pbj_dataset:
    raise Exception("PBJ Daily Nurse Staffing dataset not found in the CMS data catalog.")

# Iterate through each version of the dataset
for distribution in pbj_dataset.get('distribution', []):
    if distribution.get('mediaType') == "text/csv":
        download_url = distribution.get('downloadURL')
        temporal = distribution.get('temporal', 'latest')
        filename = f"PBJ_Daily_Nurse_Staffing_{temporal.replace('/', '_')}.csv"
        file_path = os.path.join(target_dir, filename)

        # Download and save the CSV file
        print(f"Downloading data for period: {temporal}...")
        csv_response = requests.get(download_url)
        if csv_response.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(csv_response.content)
            print(f"Saved to {file_path}")
        else:
            print(f"Failed to download data for period: {temporal}. Status code: {csv_response.status_code}")

