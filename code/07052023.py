def pair_sum(myList, sum):
    # TODO
    for i in range(len(myList)):
        pair_b = sum - myList[i]
        for j in range(i+1,len(myList)):
            if myList[j] == pair_b:
                print(myList[i],'+', myList[j])

if __name__ == '__main__':
    pair_sum1 = ([2, 4, 3, 5, 6, -2, 4, 7, 8, 9])
    pair_sum(pair_sum1, 7)