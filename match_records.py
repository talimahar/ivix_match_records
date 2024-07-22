import pandas as pd
from util import normalize_df, match_address_and_name

# Load and normalize CSV datasets
dataset1_path = "/Users/talimahar/workspace/ivix/datasets/dataset_1.csv"
dataset2_path = "/Users/talimahar/workspace/ivix/datasets/dataset_2.csv"
df1 = pd.read_csv(dataset1_path)
df2 = pd.read_csv(dataset2_path)
normalize_df(df1)
normalize_df(df2)

# Match records by BOTH address and at least one name
matched_records = match_address_and_name(df1, df2)

# Convert the matched records to a DataFrame
matched_df = pd.DataFrame(matched_records, columns=["id_1", "id_2"])

# Save the matched records to a new CSV file
output_path = "/Users/talimahar/workspace/ivix/datasets/matched_records.csv"
matched_df.to_csv(output_path, index=False)

print(f"Matched records saved to {output_path}")
