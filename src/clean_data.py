import pandas as pd
import os

def clean_research_data(input_path, output_path):
    # 1. Load the dataset
    if not os.path.exists(input_path):
        print(f"Error: The file {input_path} was not found.")
        return

    df = pd.read_csv(input_path)
    print(f"Original Data Shape: {df.shape}")
    print(f"Detected Columns: {df.columns.tolist()}")

    # 2. Separate columns by type to avoid the 'mean' error on strings
    # 'number' includes integers and floats
    numeric_cols = df.select_dtypes(include=['number']).columns
    categorical_cols = df.select_dtypes(exclude=['number']).columns

    print(f"Numeric columns found: {list(numeric_cols)}")
    print(f"Categorical columns found: {list(categorical_cols)}")

    # 3. Handle Missing Values
    # Fill numeric columns with their mean
    for col in numeric_cols:
        if df[col].isnull().sum() > 0:
            mean_val = df[col].mean()
            df[col] = df[col].fillna(mean_val)
            print(f" - Filled missing values in '{col}' with mean: {mean_val:.2f}")

    # Fill categorical/string columns with 'Missing' or a placeholder
    for col in categorical_cols:
        if df[col].isnull().sum() > 0:
            df[col] = df[col].fillna('Unknown')
            print(f" - Filled missing values in '{col}' with 'Unknown'")

    # 4. Save the cleaned file
    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    
    print("-" * 30)
    print(f"Success! Cleaned data saved to: {output_path}")

if __name__ == "__main__":
    # Adjust these paths if your folders are named differently
    INPUT_FILE = 'data/sample_data.csv' 
    OUTPUT_FILE = 'data/cleaned_data.csv'
    
    clean_research_data(INPUT_FILE, OUTPUT_FILE)