import csv
from datetime import datetime, date
from functools import reduce as reduce


def func_list_to_dict(list):
    return {'date': datetime.strptime( list[1], "%Y:%m:%d:%H:%M:%S" ), 'taxon': list[22]}


def countfn(dict, item):
    counts = {}
    for tax in dict:
        for item in tax.values():
            item = item.split(',')
            counts[item] = counts.get(item, 0) + 1
        return counts


# def find_the_key(dictionary, filter_keys):
#     for items in dictionary:
#         return dict(filter(lambda i: i[0] in filter_keys, dictionary.items()))


reduced_dict = {}
li_of_dicts = []
with open( 'cleaned_GPMDB_table.tsv', 'r' ) as f:
    header = f.readline()
    for line in f:
        li_of_dicts.append( line.strip().split( '\t' ) )
    mapped_list = map( func_list_to_dict, li_of_dicts )
    start_date = datetime( 2010, 0o6, 0o1 )
    end_date = datetime( 2010, 9, 0o1 )
    filter_list = filter(lambda x: start_date <= x['date'] <= end_date, mapped_list)
    r = countfn((filter_list), 'taxon')
    print(r)
    # e = list(filter_list)
    # result = reduce(countfn(e,['taxon']), e, dict())






    # for tax in filter_list:
    #     for item in tax.values():
    #         reduced_dict[item] = reduced_dict.get(item, 0 ) + 1
    #         reduce(lambda x: )

    # reduce(sum(['taxon' in reduced_dict for reduced_dict in filter_list]), filter_list, reduced_dict)
# filter_list_keys = (find_the_key(list(filter_list), 'taxon'))