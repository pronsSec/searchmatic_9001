import os
import shutil
import concurrent.futures
from googletrans import Translator
from tqdm import tqdm


print('-'*45)
print('-'*45)
print('-'*45)
print("""
    ███        ▄█    █▄       ▄████████         ▄████████    ▄████████    ▄████████    ▄████████  ▄████████    ▄█    █▄      ▄▄▄▄███▄▄▄▄      ▄████████     ███      ▄█   ▄████████      
▀█████████▄   ███    ███     ███    ███        ███    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███   ▄██▀▀▀███▀▀▀██▄   ███    ███ ▀█████████▄ ███  ███    ███      
   ▀███▀▀██   ███    ███     ███    █▀         ███    █▀    ███    █▀    ███    ███   ███    ███ ███    █▀    ███    ███   ███   ███   ███   ███    ███    ▀███▀▀██ ███▌ ███    █▀       
    ███   ▀  ▄███▄▄▄▄███▄▄  ▄███▄▄▄            ███         ▄███▄▄▄       ███    ███  ▄███▄▄▄▄██▀ ███         ▄███▄▄▄▄███▄▄ ███   ███   ███   ███    ███     ███   ▀ ███▌ ███             
    ███     ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀          ▀███████████ ▀▀███▀▀▀     ▀███████████ ▀▀███▀▀▀▀▀   ███        ▀▀███▀▀▀▀███▀  ███   ███   ███ ▀███████████     ███     ███▌ ███             
    ███       ███    ███     ███    █▄                ███   ███    █▄    ███    ███ ▀███████████ ███    █▄    ███    ███   ███   ███   ███   ███    ███     ███     ███  ███    █▄       
    ███       ███    ███     ███    ███         ▄█    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███   ███   ███   ███   ███    ███     ███     ███  ███    ███      
   ▄████▀     ███    █▀      ██████████       ▄████████▀    ██████████   ███    █▀    ███    ███ ████████▀    ███    █▀     ▀█   ███   █▀    ███    █▀     ▄████▀   █▀   ████████▀       
                                                                                      ███    ███                                                                                         
""")
print('-'*45)
print('This will search all files in a directory in parallel for a search phrase you input. \nIt will infer the file"s source lang and translate your phrase to that language. \nAt the end it will translate the files to English. \nYeah motherfucker, and it is fast as fuck. Well, relatively fast for what it is doing.')
print('-'*45)


directory = input("Enter the directory path: ")


search_phrase = input("Enter the search phrase: ")


extensions = input("Enter the file extensions (separated by commas): ").split(",")


results_directory = input("Enter the name of the results directory: ")
if not os.path.exists(results_directory):
    os.makedirs(results_directory)


translator = Translator()

def process_file(filepath):
    # Open the file and read its contents
    with open(filepath, "r") as file:
        contents = file.read()

    
    lang = translator.detect(contents).lang
    translated_phrase = translator.translate(search_phrase, src='en', dest=lang).text

    
    if translated_phrase in contents:
        # Copy the file to the results directory
        destination_file = os.path.join(results_directory, os.path.basename(filepath))
        shutil.copyfile(filepath, destination_file)
        print(f"Copied {filepath} to {destination_file}")


file_paths = []
for filename in os.listdir(directory):
    if any(filename.endswith(ext.strip()) for ext in extensions):
        file_path = os.path.join(directory, filename)
        file_paths.append(file_path)


with tqdm(total=len(file_paths), desc="Processing files") as progress:
    # Create a ThreadPoolExecutor with 4 worker threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        # Submit a processing job for each file
        futures = [executor.submit(process_file, filepath) for filepath in file_paths]

       
        for future in concurrent.futures.as_completed(futures):
            progress.update()


for filename in os.listdir(results_directory):
    filepath = os.path.join(results_directory, filename)
    with open(filepath, "r") as file:
        contents = file.read()
    translated_contents = translator.translate(contents, dest='en').text
    with open(filepath, "w") as file:
        file.write(translated_contents)

print("Done!")
