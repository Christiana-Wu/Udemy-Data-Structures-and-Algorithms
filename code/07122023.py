# his_dict = {'a': 5, 'b': 9, 'c': 2}
# def max_value_key(my_dict):
#     # TODO
#     max_value = my_dict['a']
#     output_key = 'a'
#     for key in my_dict.keys():
#         if my_dict[key] > max_value:
#             max_value = my_dict[key]
#             output_key = key
#
#     return output_key

# my_dict6584 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# def filter_dict(my_dict, condition):
#     # TODO
#     new_dict = {}
#     for k, v in my_dict.items():
#         if condition(k,v):
#             new_dict [k] = v
#     return new_dict

list11 = [1, 2, 3, 2, 1]
list22 = [3, 1, 2, 1, 3]
def check_same_frequency(list1, list2):
    # TODO
    dict1 = {}
    for i in range(len(list1)):
        dict1[list1[i]] = dict1.get(list1[i], 0) + 1
    dict2 = {}
    for j in range(len(list2)):
        dict2[list2[i]] = dict2.get(list2[j], 0) + 1
    if dict1 == dict2:
        return True
    else:
        return False

if __name__ == '__main__':
    print(check_same_frequency(list11, list22))