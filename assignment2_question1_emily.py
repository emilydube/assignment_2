import csv
from datetime import datetime, date


def list_to_dict(list):
        return {'date': datetime.strptime(list[1], "%Y:%m:%d:%H:%M:%S"), 'taxon': list[22]}

li_of_dicts = []
with open('cleaned_GPMDB_table.tsv', 'r') as f:
    header = f.readline()
    for line in f:
        li_of_dicts.append(line.strip().split('\t'))
    mapped_list = map(list_to_dict, li_of_dicts)
    start_date = date(2010, 0o6, 0o1)
    end_date = date(2010, 9, 0o1)
    filter_list = filter(lambda x: x(start_date, end_date,), mapped_list)
    print(list(filter_list))


#  filter_list = filter(lambda x: x in (start_date-end_date), mapped_list)



