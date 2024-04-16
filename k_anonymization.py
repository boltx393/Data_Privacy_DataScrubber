import pandas as pd
import random

def generalize(df, qi_columns):
    for column in qi_columns:
        if df[column].dtype in ['int64', 'float64']:
            df[column] = df[column].apply(lambda x: round(x, -1))
        elif df[column].dtype == 'object':
            df[column] = df[column].apply(lambda x: x[:-2] + 'XX' if len(x) > 2 else x)
    return df

def suppress(df, sensitive_columns):
    suppression_symbols = ['**', '##', '!!', '??', '++']
    for column in sensitive_columns:
        suppression_symbol = random.choice(suppression_symbols)
        df[column] = suppression_symbol
    return df

def group_records(df, qi_columns, sensitive_columns, k):
    df = generalize(df, qi_columns)
    df = suppress(df, sensitive_columns)
    
    grouped = df.groupby(qi_columns)
    
    anonymized_groups = []
    for _, group in grouped:
        if len(group) >= k:
            anonymized_groups.append(group)
        else:
            while len(group) < k:
                num_samples = min(k - len(group), len(group))
                synthetic_records = df.sample(n=num_samples, replace=True)
                anonymized_groups.append(synthetic_records)
                group = pd.concat([group, synthetic_records])
                
    anonymized_df = pd.concat(anonymized_groups)
    return anonymized_df

def k_anonymize(df, risky_qi, sensitive_columns, k):
    anonymized_df = df.copy()  # Make a copy of the DataFrame
    
    # Generalize quasi-identifier columns and suppress sensitive columns
    anonymized_df = generalize(anonymized_df, risky_qi)
    anonymized_df = suppress(anonymized_df, sensitive_columns)
    
    # Group records based on generalized quasi-identifier columns
    anonymized_df = group_records(anonymized_df, risky_qi, sensitive_columns, k)
    
    return anonymized_df
