import json
import pandas as pd
from unpaywall_api import get_full_text

json_df_2 = pd.read_json("covid19_ai_imaging_2.jsonl", lines = True)

json_list = json_df_2["doi"].to_list()

# print(json_list)

individual_dois = []

for i in json_list:
    try:
        lines = i.split("\n")
        # print("-" * 50)
        for line in lines:
            individual_dois.append(line)
    except AttributeError:
        continue
    
print(individual_dois)

# full_texts = get_full_text(individual_dois)

# for text in full_texts:
#     print(text)
