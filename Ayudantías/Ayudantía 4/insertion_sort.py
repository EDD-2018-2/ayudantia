def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key

if __name__=="__main__":
    list = [8, 9, 7, 9, 3, 2, 3, 8, 4, 6]
    insertion_sort(list)
    print('Sorted list: {}'.format(list))