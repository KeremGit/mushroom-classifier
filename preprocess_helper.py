import pandas as pd
import numpy as np
from typing import Callable, Dict, List

boolean_options = ['t','f']
schema = {
    'class': {'target': True, 'categories': ['e','p']},
    'cap-shape': {'categories': ['x', 'f', 's', 'b', 'o']}, 
    'cap-surface': {'categories': ['t', 's', 'y', 'h', 'g']}, 
    'cap-color': {'categories': ['n', 'y', 'w', 'g', 'e']}, 
    'gill-attachment': {'categories': ['a', 'd', 'x', 'e', 's']}, 
    'gill-spacing': {'categories': ['c', 'd', 'f', 'e', 'a']}, 
    'gill-color': {'categories': ['w', 'n', 'y', 'p', 'g']}, 
    'stem-root': {'categories': ['b', 's', 'r', 'c', 'f']}, 
    'stem-surface': {'categories': ['s', 'y', 'i', 't', 'g']}, 
    'stem-color': {'categories': ['w', 'n', 'y', 'g', 'o']}, 
    'veil-type': {'categories': ['u', 'w', 'a', 'e', 'f']}, 
    'veil-color': {'categories': ['w', 'y', 'n', 'u', 'k']}, 
    'ring-type': {'categories': ['f', 'e', 'z', 'l', 'r']}, 
    'spore-print-color': {'categories': ['k', 'p', 'w', 'n', 'r']}, 
    'habitat': {'categories': ['d', 'g', 'l', 'm', 'h']}, 
    'season': {'categories': ['a', 'u', 'w', 's']}, 
    'does-bruise-or-bleed': {'categories': boolean_options}, 
    'has-ring': {'categories': boolean_options},
     'cap-diameter': {},
    'stem-height': {},
    'stem-width': {},
}

def perform_operation_in_chunk(file_name: str, function:Callable[[pd.DataFrame], dict], chunk_size=10000):
    result = {}
    counter = 1
    for chunk in pd.read_csv(file_name, chunksize=chunk_size):
        counter +=1
        if counter > 2:
            return result
        chunk_properties = function(chunk)
        for column_name, props in chunk_properties.items():
            if column_name not in result:
                result[column_name] = props
            else:
                existing_props = result[column_name]
                existing_props['is_categorical'] = existing_props['is_categorical'] or props['is_categorical']
                existing_props['has_missing_data'] = existing_props['has_missing_data'] or props['has_missing_data']
                existing_props['categories'].update(props['categories'])
    return result

def column_has_missing_data(column: pd.Series) -> bool:
    return column.isnull().any()
    
def is_column_categorical(column: pd.Series):
    """
    This function returns true if the column is object. Pandas reads string columns as objects by default.
    This is not very reliable but applicalbe to the data set in this project
    """
    return column.dtype.name == 'object'

def identify_column_properties(df: pd.DataFrame) -> dict:
    
    column_properties = {}
    for column_name in df:
        col = df[column_name]
        
        categories = set()
        is_categorical = is_column_categorical(col)
        if(is_categorical):
            categories=set(col.dropna().unique())
            
        has_missing_data = column_has_missing_data(col)
        
        column_properties.update({
            column_name:{
            'has_missing_data': has_missing_data,
            'is_categorical': is_categorical,
            'categories': categories,
        }})
    return column_properties
        
    

def clean_training_data(source_file: str, output_file: str, schema: Dict[str, any], clean_func: Callable[[pd.DataFrame, Dict[str, any]], pd.DataFrame], chunk_size=10000):
    first_chunk = True
    
    for chunk in pd.read_csv(source_file, chunksize=chunk_size):
        processed_chunk = clean_func(chunk, schema)  
        if first_chunk:
            processed_chunk.to_csv(output_file, index=False)
            first_chunk = False
        else:
            # Append subsequent chunks
            processed_chunk.to_csv(output_file, mode='a', header=False, index=False)


def clean_data(df: pd.DataFrame, schema: Dict[str, any]) -> pd.DataFrame:
    for column_name, properties in schema.items():
        column = df[column_name]
        is_target = properties.get('target', False)
        categories = properties.get('categories', [])
        
        if(is_target):
            # todo clean up target
            continue
        elif(len(categories) > 0):
            df[column_name] = column.where(column.isin(categories), np.nan)
        else:
            df[column_name] = pd.to_numeric(column, errors='coerce')        
    return df



def clean_mushroom_dataset():
    clean_training_data('train.csv','clean_train.csv', schema, clean_data)
    