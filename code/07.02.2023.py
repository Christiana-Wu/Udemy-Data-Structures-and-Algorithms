
# lst=[1,2,3,4]
# def middle(lst):
#     lst.remove(len(lst)-1)
#     lst.remove(0)
#     print(lst)

    # myList2D= [[1,2,3],[4,5,6],[7,8,9]]
    # def diagonal_sum(matrix):
    # # TODO
    #     for i in range(len(myList2D))
    #         sum = myList2D[i][i]
    #         return sum

# myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
# def first_second(my_list):
#     my_list.sort(reverse = True)
#     return my_list[0], my_list[1]
# print(first_second(myList))

original_list = [1, 1, 2, 2, 3, 4, 5]
def remove_duplicates(arr):
    # TODO
    removed_list = []
    for i in range(len(arr)):
        if arr[i] not in removed_list:
            removed_list.append(arr[i])
    return removed_list
print(remove_duplicates(original_list ))