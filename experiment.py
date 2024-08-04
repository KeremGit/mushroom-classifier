import pandas as pd
from io import StringIO
from preprocess_helper import perform_operation_in_chunk, identify_column_properties
from preprocess_helper import clean_mushroom_dataset


csv_string = """col1,col2,col3
1,A,2024
2,,2025
3,C,2026"""

df = pd.read_csv(StringIO(csv_string))

result = perform_operation_in_chunk('clean_train.csv',  identify_column_properties)
print(result)

# val = { 'column_name': {'has': True, 'number': 3}}

# for col, props in val.items():
#     print(col)
#     print(props)


