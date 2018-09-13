def bubble_sort(list):
    for i in range(len(list) - 1, 0, -1):
        for j in range(i):  
            if list[j] < list[j+1]:
                # temp = list[j]
                # list[j] = list[j+1]
                # list[j+1] = temp
                list[j], list[j+1] = list[j+1], list[j]

def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key > list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
    
def selection_sort(list):
    for i in range(len(list)):
        position_min = i
        for j in range(i+1, len(list)):
            if list[j] < list[position_min]:
                position_min = j
        list[i], list[position_min] = list[position_min], list[i]
    
def merge_sort():
    pass

if __name__=="__main__":
    list = [8, 9, 7, 9, 3, 2, 3, 8, 4, 6]
    # bubble_sort(list)
    # insertion_sort(list)
    selection_sort(list)
    print('Sorted list: {}'.format(list))