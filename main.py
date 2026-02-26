import csv
import json
import os
from dotenv import load_dotenv

# csv to json conversion
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

# json to csv conversion
def json_to_csv(json_file_path, csv_output_path):
    # check if the file exists before attempting to open it
    if not os.path.exists(json_file_path):
        print(f"Error: {json_file_path} not found.")
        return

    try:
        with open(json_file_path, 'r', encoding='utf-8') as j_file:
            data = json.load(j_file)

        # ensure JSON data is a list
        if not isinstance(data, list):
            print("Error: JSON data must be a list of objects.")
            return

        if len(data) == 0:
            print("The JSON file is empty.")
            return

        # extract headers from the first dictionary keys
        headers = data[0].keys()

        # 4. Write to CSV
        with open(csv_output_path, 'w', newline='', encoding='utf-8') as c_file:
            writer = csv.DictWriter(c_file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)

        print(f"Successfully converted {json_file_path} to {csv_output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Replace 'your_data.csv' with your actual local filename
    load_dotenv()
    path_to_csv = os.getenv("FILEPATH")
    csv_to_json(path_to_csv)