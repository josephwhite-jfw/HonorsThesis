#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import pyreadstat

# Set the input folder where the .sas7bdat files are located
input_folder = r"C:\Users\Owner\OneDrive\Documents\Honors_Thesis\data\drive-download-20250525T211237Z-1-001"

# Set the output folder where the CSV files will be saved
output_folder = r"C:\Users\Owner\OneDrive\Documents\Honors_Thesis\data\cost-reports-csv"
os.makedirs(output_folder, exist_ok=True)

# Convert each SAS file to CSV
for file in os.listdir(input_folder):
    if file.endswith(".sas7bdat"):
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, file.replace(".sas7bdat", ".csv"))

        print(f"Converting {file}...")
        df, meta = pyreadstat.read_sas7bdat(input_path)
        df.to_csv(output_path, index=False)
        print(f"Saved to {output_path}")

