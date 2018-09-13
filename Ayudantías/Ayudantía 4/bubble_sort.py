def bubble_sort(list):
    for i in range(len(list) - 1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                
if __name__=="__main__":
    list = [8, 9, 7, 9, 3, 2, 3, 8, 4, 6]
    bubble_sort(list)
    print('Sorted list: {}'.format(list))