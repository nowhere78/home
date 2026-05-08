import os
import time
import requests

WORK_DIR = os.path.join(os.getcwd(), "work")
DONE_DIR = os.path.join(os.getcwd(), "dones")

os.makedirs(WORK_DIR, exist_ok=True)
os.makedirs(DONE_DIR, exist_ok=True)

def process_file(file_name):
    """
    Processa o arquivo especificado:
    - Primeira linha: URL com placeholders.
    - Demais linhas: Dados do formulário.
    """
    file_path = os.path.join(WORK_DIR, file_name)
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    if not lines:
        print(f"File {file_name} is empty.")
        return
    
    url_template = lines[0].strip()
    data_lines = lines[1:]

    for idx, line in enumerate(data_lines):
        data_fields = line.strip().split(',')
        url = url_template

        for i, field in enumerate(data_fields):
            url = url.replace(f"$${i}", field)

        try:
            print(f"Sending request to: {url}")
            response = requests.get(url)
            print(f"Response {idx + 1}: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Failed to send request {idx + 1}: {e}")

def main():
    print("Starting HTTP request processor...")
    processed_files = set()

    while True:
        try:
            files = [f for f in os.listdir(WORK_DIR) if os.path.isfile(os.path.join(WORK_DIR, f))]
            new_files = [f for f in files if f not in processed_files]

            for file_name in new_files:
                process_file(file_name)

                src_path = os.path.join(WORK_DIR, file_name)
                dest_path = os.path.join(DONE_DIR, file_name)
                os.rename(src_path, dest_path)
                processed_files.add(file_name)

            time.sleep(35)

        except KeyboardInterrupt:
            print("\nStopping HTTP request processor...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
