from datetime import datetime, date
from functools import reduce as reduce


def func_list_to_dict(list):
    return {'date': datetime.strptime( list[1], "%Y:%m:%d:%H:%M:%S" ), 'taxon': list[22]}

# def reduce_counts(dict_of_counts, filter_dict):
#     dict_of_counts = {}
#     for x in filter_dict:
#         dict_of_counts[x] = dict_of_counts.get(x, 0) + 1
#         return dict_of_counts

def x(a, b):
    counts = {}
    for x in a:
        if x in b:
            x[counts] = sum(1 for x in a if x == b)
            return counts

# sum( 1 for d in my_list if d.get( 'id' ) == 1 )


dict_of_counts = {}
li_of_dicts = []
with open( 'cleaned_GPMDB_table.tsv', 'r' ) as f:
    header = f.readline()
    for line in f:
        li_of_dicts.append( line.strip().split( '\t' ) )
    mapped_dicts = map( func_list_to_dict, li_of_dicts )
    start_date = datetime( 2010, 6, 1 )
    end_date = datetime( 2010, 9, 30 )
    filter_dicts = filter(lambda x: start_date <= x['date'] <= end_date, mapped_dicts)
    reduce_dict = reduce(x(next(filter_dicts), dict_of_counts['taxon']),filter_dicts,{})








    # for tax in filter_list:
    #     for item in tax.values():
    #         reduced_dict[item] = reduced_dict.get(item, 0 ) + 1
    #         reduce(lambda x: )

    # reduce(sum(['taxon' in reduced_dict for reduced_dict in filter_list]), filter_list, reduced_dict)
# filter_list_keys = (find_the_key(list(filter_list), 'taxon'))