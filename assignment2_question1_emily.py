import csv
from datetime import datetime

def list_to_dict(list):
    return {'date': list[1], 'taxon': list[22]}

with open('cleaned_GPMDB_table.tsv', 'r') as f:
    header = f.readline()
    li_of_dicts = []
    for line in f:
        li_lines = [line.strip().split('\t')]
        for date in li_lines:
            date[1] = datetime.strptime(date[1], "%Y:%m:%d:%H:%M:%S")
            for item in li_lines:
                d = list(map(list_to_dict, li_lines))
                li_of_dicts.append(d)
                print(li_of_dicts)