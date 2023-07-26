
def max_product(arr):
    arr.sort(reverse=True)
    print(arr)
    return arr[0]*arr[1]


if __name__ == '__main__':
    max_product([1,6,1,9,4])