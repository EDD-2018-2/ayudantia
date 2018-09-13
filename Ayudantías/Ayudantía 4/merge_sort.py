def merge(list, l, m, r):

    n1 = m - l + 1
	n2 = r- m
	L = [0] * (n1)
	R = [0] * (n2)
	for i in range(0 , n1):
		L[i] = arr[l + i]
	for j in range(0 , n2):
		R[j] = arr[m + 1 + j]
	# Merge the temp arrays back into arr[l..r]
	i = 0	 # Initial index of first subarray
	j = 0	 # Initial index of second subarray
	k = l	 # Initial index of merged subarray

	while i < n1 and j < n2 :
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	# Copy the remaining elements of L[], if there
	# are any
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	# Copy the remaining elements of R[], if there
	# are any
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1
        
def merge_sort(list, start = 0, end = len(list)):
    if len(list) <= 1:
        return
    else:
        #size = len(list)
		middle = (start + (end-1) )/2
        print(middle)
        merge_sort(list, 0, middle)
    	merge_sort(list, middle+1, size)
    	merge(list, 0, middle, size)

def merge_sort(list):

    print("Splitting ", list)

    if len(list) > 1:
        mid = len(list)//2
        left_half = list[:mid]
        right_half = list[mid:]

        #recursion
        merge_sort(left_half)
        merge_sort(righ_thalf)

        i=0
        j=0
        k=0

        while i < len(left_half) and j < len(righthalf):
            if left_half[i] < right_half[j]:
                list[k] = left_half[i]
                i = i+1
            else:
                list[k] = right_half[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

    print("Merging ",alist)

if __name__=="__main__":
    list = [8, 9, 7, 9, 3, 2, 3, 8, 4, 6]
    insertion_sort(list)
    print('Sorted list: {}'.format(list))