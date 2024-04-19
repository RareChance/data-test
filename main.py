import csv
import os
from datetime import datetime

now = datetime.now()
generation_date = now.strftime("%Y-%m-%d %H:%M:%S")

input_folder = os.path.abspath('')
input_file_1 = os.path.join(input_folder, 'weekend_data_processing/data_2023-02-11.csv')
input_file_2 = os.path.join(input_folder, 'weekend_data_processing/data_2023-02-12.csv')
output_file = os.path.join(input_folder, 'weekend_data_processing/combined_data.csv')

with open(input_file_1, 'r', newline='') as file_1, open(input_file_2, 'r', newline='') as file_2:
    reader_1 = csv.reader(file_1, delimiter=';')
    reader_2 = csv.reader(file_2, delimiter=';')
    headers = next(reader_1)
    next(reader_2)
    headers.append('generation_date')
    data = [row.append(generation_date) or row for row in reader_1]
    data_list_2 = [row.append(generation_date) or row for row in reader_2]
    data.extend(data_list_2)
    data.sort(key=lambda x: x[1])
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=';')
        writer.writerow(headers)
        writer.writerows(data)
