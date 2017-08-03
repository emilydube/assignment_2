from collections import defaultdict
from itertools import combinations
import pprint
import math

# def user_item_compare(user_key, dict):                #TRIED MAKING A FUNCTION HERE
#     for user_key in combinations(dict.keys(), 1):
#         user_dict = dict[user_key[0]]
#         list_user_items = [user_dict.items()]
#         return print(list_user_items)


user_item_rating = {
    'user1': {'item1': 2.5, 'item2': 3.5, 'item3': 3.0,
              'item4': 3.5, 'item5': 2.5, 'item6': 3.0},
    'user2': {'item1': 3.0, 'item2': 3.5, 'item3': 1.5,
              'item4': 5.0, 'item5': 3.5, 'item6': 3.0},
    'user3': {'item1': 2.5, 'item2': 3.0, 'item4': 3.5,
              'item6': 4.0},
    'user4': {'item2': 3.5, 'item3': 3.0, 'item4': 4.0,
              'item5': 2.5, 'item6': 4.5},
    'user5': {'item1': 3.0, 'item2': 4.0, 'item3': 2.0,
              'item4': 3.0, 'item5': 2.0, 'item6': 3.0},
    'user6': {'item1': 3.0, 'item2': 4.0, 'item4': 5.0,
              'item5': 3.5, 'item6': 3.0},
    'user7': {'item2': 4.5, 'item4': 4.0, 'item5': 1.0}
}
rev_item_user_dict = defaultdict(dict)          #reverse/ transform dictionary
for k, v in user_item_rating.items():
    for nest_k, nest_v in v.items():
        rev_item_user_dict[nest_k][k] = nest_v
        pprint.pprint(rev_item_user_dict)

for item in combinations(rev_item_user_dict.keys(), 2):                      #using cominations to pull out user ratings for item
    item1_dict, item2_dict = rev_item_user_dict[item[0]], rev_item_user_dict[item[1]]
    item1_list = item1_dict.items()     #pulled out the item1 values but in dict.item type - unable to do anything
    # item1_new = sorted(item1_list)    #tried sorted to convert dict.items to list
    item2_list = item2_dict.items()
    # item2_new = sorted(item2_list)

    print('item 1 user ratings:', item1_list) #list of tuples? - trying to work out
    print('item 1 user ratings:', item2_list)

    # keys_1 = set(item1_list.keys())         #intersection to get common keys - not working because item1_list is not dictionary just dict.items
    # keys_2 = set(item2_list.keys())
    # intersection = keys_1 & keys_2
    # print(intersection)



# item1_list = []                               #Step 2 attempts TRIED THIS TO NOT GET DICT.ITEMS
# for key, value in item1_dict.items():
#     item1_sorted = [key,value]
#     item1_sorted.append(item1_list)
#     print(item1_list)

# x = combinations(rev_item_user_dict['item1'], 2 )                        #Step 2 attempts TRIED TO WORK OUT SIMPLIER METHOD, DIDNT WORK
# y = list(x)
# final = [''.join( x ) for x in combinations(rev_item_user_dict['item1'], 2)]
# print(final)

