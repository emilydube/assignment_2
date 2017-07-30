import csv
from datetime import datetime


def list_to_dict(list):
    for item in list:
        item[1] = (datetime.strptime(item[1], "%Y:%m:%d:%H:%M:%S"))
    return {'date': item[1], 'taxon': item[22]}

li_of_dicts = []
with open('cleaned_GPMDB_table.tsv', 'r') as f:
    header = f.readline()
    for line in f:
        li_of_dicts.append([line.strip().split('\t')])
    mapped_list = (map(list_to_dict, li_of_dicts))
    filter_list = (filter(lambda d: d[(datetime.strptime("2010/09/30", "%Y/%m/%d")) >= d >= (datetime.strptime("2010/06/01", "%Y/%m/%d"))] in mapped_list))
    print(list(mapped_list))






