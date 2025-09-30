import os
import pandas as pd

def save_cleaned_data(df, filename="weather_cleaned.csv"):
    """
    Save cleaned/preprocessed DataFrame to data/processed/ folder.
    
    Parameters:
    df (pd.DataFrame): Cleaned DataFrame
    filename (str): Name of the output CSV file
    """
    # Construct path to processed folder
    processed_dir = os.path.join(os.getcwd(), "data", "processed")
    
    # Create folder if it doesn't exist
    os.makedirs(processed_dir, exist_ok=True)
    
    # Full path for the CSV file
    file_path = os.path.join(processed_dir, filename)
    
    # Save CSV
    df.to_csv(file_path, index=False)
    print(f"✅ Cleaned data saved to: {file_path}")
    
    return file_path
