import pandas as pd
import re

def remove_special_chars(input_string):
    # Regex pattern để loại bỏ tất cả các ký tự đặc biệt và số, bao gồm cả "vietkey"
    pattern = r'[^a-zA-Z\sàáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵđ]'
    return re.sub(pattern, '', input_string)

def process_excel(input_file, output_file):
    # Đọc dữ liệu từ file Excel vào DataFrame
    df = pd.read_excel(input_file)
    
    # Áp dụng hàm remove_special_chars cho cột "Sentence"
    df['Processed_Sentence'] = df['Sentence'].apply(remove_special_chars)
    
      # Loại bỏ các dòng trùng nhau
    df = df.drop_duplicates()
    
    # Ghi dữ liệu đã xử lý ra file Excel
    df.to_excel(output_file, index=False)

# Sử dụng hàm:
input_file = "data/data.xlsx"
output_file = "data/output.xlsx"
process_excel(input_file, output_file)
