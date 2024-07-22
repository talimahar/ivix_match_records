import pandas as pd
import re
from fuzzywuzzy import fuzz

def normalize_string(value):
    if pd.isna(value):
        return ""
    value = str(value)
    value = value.lower()
    value = re.sub(r'[^a-z0-9 ]', '', value)
    value = re.sub(r'\s+', ' ', value).strip()
    return value

def normalize_df(df):
    for column in df.columns:
        df[column] = df[column].apply(normalize_string)

def match_address_and_name(df1, df2):
    matched_records = []

    for _, row2 in df2.iterrows():
        id2 = row2['id']
        address2 = f"{row2['street']} {row2['city']} {row2['zip']}"
        names2 = [row2['name_1'], row2['name_2'], row2['name_3']]

        for _, row1 in df1.iterrows():
            id1 = row1['id']
            address1 = row1['address']
            name1 = row1['name']

            address_ratio = fuzz.ratio(address2, address1)
            name_ratio = max(fuzz.ratio(name2, name1) for name2 in names2)

            if name_ratio > 50 and address_ratio > 50:
                existing_record = None
                for record in matched_records:
                    if record['id_1'] == id1 or record['id_2'] == id2:
                        existing_record = record
                        break

                if existing_record:
                    if address_ratio > existing_record['address_ratio'] or name_ratio > existing_record['name_ratio']:
                        existing_record['id_1'] = id1
                        existing_record['id_2'] = id2
                        existing_record['address_ratio'] = address_ratio
                        existing_record['name_ratio'] = name_ratio
                else:
                    matched_records.append({'id_1': id1, 'id_2': id2, 'address_ratio': address_ratio, 'name_ratio': name_ratio})

    return matched_records
