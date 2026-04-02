import pandas as pd
import os

input_file = 'data/sample_data.csv'
output_file = 'data/cleaned_data.csv'

if os.path.exists(input_file):
    # sep=None and engine='python' allows pandas to guess the separator (comma/tab)
    df = pd.read_csv(input_file, sep=None, engine='python')
    
    print("Detected Columns:", df.columns.tolist())

    # List of numeric columns to clean
    cols_to_fix = ['experiment_score', 'temperature', 'humidity']
    
    for col in cols_to_fix:
        if col in df.columns:
            # Fill missing values with the average of that column
            df[col] = df[col].fillna(df[col].mean())
        else:
            print(f"Warning: Column '{col}' not found. Check your CSV headers!")

    # Save as a proper comma-separated file
    df.to_csv(output_file, index=False)
    print(f"Success! Cleaned data saved to {output_file}")
else:
    print(f"Error: {input_file} not found.")