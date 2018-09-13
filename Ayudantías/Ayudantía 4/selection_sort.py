def selection_sort(list):
    for i in range(len(list)):
        position_min = i
        
        for j in range(i+1, len(list)):
            if list[j] < list[position_min]:
                position_min = j
        temp = list[i]
        list[i] = list[position_min]
        list[position_min] = temp
        print("min", list[i], list)
        
if __name__=="__main__":
    list = [8, 9, 7, 9, 3, 2, 3, 8, 4, 6]
    selection_sort(list)
    print('Sorted list: {}'.format(list))