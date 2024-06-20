import pandas as pd

# Path to your .tab file
file_path = 'https://raw.githubusercontent.com/juliaDataScience-22/project2-620/main/affiliations_1996.txt'

# Read .tab file into a DataFrame
df = pd.read_csv(file_path, delimiter='\t')

# Display the first few rows of the DataFrame
print(df.head())


'''
@data{DVN/NPLPOJ_2022,
author = {Filho, Bento Alves},
publisher = {Harvard Dataverse},
title = {{Data Set - Doctor-Patient Interaction}},
UNF = {UNF:6:hVBjnFXvPJqs+eSNlGJrxQ==},
year = {2022},
version = {DRAFT VERSION},
doi = {10.7910/DVN/NPLPOJ},
url = {https://doi.org/10.7910/DVN/NPLPOJ}
}'''