# TODO импортировать необходимые молули
import csv
import json
from collections import OrderedDict

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task(csv_file_path,json_file_path) -> None:
    json_string = []
    with open(csv_file_path, 'r', newline='') as csvfile:
        for row in csv.DictReader(csvfile, delimiter=',', quotechar='\n'):
            json_string.append(OrderedDict((str(key), val) for key, val in row.items()))
    with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(json_string, indent=4))

if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME,OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
