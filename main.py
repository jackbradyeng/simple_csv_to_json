import csv
import json
import os
from dotenv import load_dotenv

def csv_to_json(file_path):
    # check if the file exists before trying to open it
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' was not found.")
        return

    try:
        with open(file_path, mode='r', encoding='utf-8-sig') as csv_file:
            # DictReader uses the first row as dictionary keys
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                # convert the dictionary row into a JSON string
                json_output = json.dumps(row, indent=4)
                print(json_output)
                print("-" * 20)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Replace 'your_data.csv' with your actual local filename
    load_dotenv()
    path_to_csv = os.getenv("FILEPATH")
    csv_to_json(path_to_csv)