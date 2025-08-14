import json
import csv

def json_csv(json_file, csv_file):
    try:
        with open(json_file, "r", encoding = "utf-8") as f:
            data = json.load(f)


        if not isinstance(data, list):
           raise ValueError("Json file must contain list of onjects")

        if not all(isinstance(item, dict) for item in data):
           raise ValueError("All items in json file must be in dictionaries")

        fieldnames = list(data[0].keys())

        with open(csv_file, "w", newline = "", encoding ="utf-8") as f:
           writer = csv.DictWriter(f, fieldnames = fieldnames)
           writer.writeheader()
           writer.writerows(data)

        print(f"File '{json_file}' converted to '{csv_file}' successfully....!!")

    except FileNotFoundError:
        print(f"File not found: {json_file}")
    except json.JSONDecodeError:
        print(f" Invalid JSON format in {json_file}")
    except Exception as e:
        print(f" Error: {e}")
json_file = "Task.json" 
csv_file = "Task.csv"

json_csv(json_file,csv_file)
               
