import pandas as pd
import re

def remove_special_chars(input_string):
    if isinstance(input_string, str):  # Check if input_string is a string
        # Regex pattern to remove all special characters and numbers
        pattern = r'[^a-zA-Z\sàáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵđ]'
        return re.sub(pattern, '', input_string)
    else:
        return str(input_string)  # Convert non-string input to string

def process_excel(input_file, output_file):
    # Read data from Excel file into DataFrame
    df = pd.read_excel(input_file)
    
    # Apply remove_special_chars function to the "Sentence" column
    df['Processed_Sentence'] = df['Sentence'].apply(remove_special_chars)
    
    # Remove duplicate rows
    df = df.drop_duplicates()
    
    # Write processed data to Excel file
    df.to_excel(output_file, index=False)

# Usage:
input_file = "data/data.xlsx"
output_file = "data/output.xlsx"
process_excel(input_file, output_file)
