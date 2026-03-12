import os
import zipfile
import shutil

shutil.unpack_archive('unzip_me_for_instructions.zip', '', 'zip')

# def unzip_file(zip_file_path, extract_to):
#     with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
#         zip_ref.extractall(extract_to)

with open('unzip_me_for_instructions.zip', 'rb') as zip_files:
    Content=zip_files.read()
    # print(Content)

def list_files_in_directory():
    for root, dirs, files in os.walk(os.getcwd()+'\\extracted_content'):
        print(f"Total files in {root}: {len(files)}")
        for file in files:
            print(file)

def search_for_phone_numbers():
    phone_numbers = []
    for root, dirs, files in os.walk(os.getcwd()+'\\extracted_content'):
        for file in files:
            if file.endswith('.txt'):
                with open(os.path.join(root, file), 'r') as f:
                    content = f.read()
                    phone_numbers.extend(extract_phone_numbers(content))
    return phone_numbers

def extract_phone_numbers(text):
    import re
    phone_pattern = re.compile(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b')
    return phone_pattern.findall(text)


if __name__ == "__main__":    
    # zip_file_path = 'C:\\Users\\Dell\\Downloads\\unzip_me_for_instructions_QA\\extracted_content\\unzip_me_for_instructions.zip'
    # extract_to = 'C:\\Users\\Dell\\Downloads\\unzip_me_for_instructions_QA\\extracted_content'
    # unzip_file(zip_file_path, extract_to)   
    list_files_in_directory()
    print("Searching for phone numbers in the extracted files...")
    phone_numbers = search_for_phone_numbers()  
    print("Found phone numbers:")
    for number in phone_numbers:
        print(number)