from datetime import datetime, date
from functools import reduce as reduce


def func_list_to_dict(list_x):  # Step 3: function to convert list to dictionary with date and taxon
    return {'date': datetime.strptime(list_x[1], "%Y:%m:%d:%H:%M:%S" ), 'taxon': list_x[22]}


def reduce_counts(dict_of_counts, f_dicts):     # Step 4: reduce function: counts for taxon
    taxon_list = f_dicts['taxon'].split(',')    # split the taxon by ,
    for each_taxon in taxon_list:               # for each taxon in list of dicts, get taxon and count for each
        each_taxon = each_taxon.strip()
        dict_of_counts[each_taxon] = dict_of_counts.get(each_taxon, 0) + 1
    return dict_of_counts


li_of_dicts = []
with open('cleaned_GPMDB_table.tsv', 'r') as f:                               #with open file so it automatically closes
    header = f.readline()                                                       #header = so header/ top line is stored
    for line in f:
        li_of_dicts.append(line.strip().split('\t'))                        #append each line to list of dicts
mapped_dicts = map(func_list_to_dict, li_of_dicts)                        #map to only have date and taxon
start_date = datetime(2010, 6, 1)
end_date = datetime(2010, 9, 30)
fil_dt_dicts = filter(lambda x: start_date <= x['date'] <= end_date, mapped_dicts)  #filter for date range/taxons
reduced_fd = reduce(reduce_counts, fil_dt_dicts, {})
print(max(reduced_fd.items(), key=lambda x: x[1]))                           #print the taxon with the highest value
