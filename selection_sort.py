arr = [4,1,6,9,2,3]

def selection_sort(ar):
    
    for i in range(0,len(ar)-1):
        pointer = i
        low = ar[i]
        low_loc = i
        while pointer < len(ar):
            if ar[pointer] < low:
                low = ar[pointer]
                low_loc = pointer
            pointer += 1
        temp = ar[i]
        ar[i] = low
        ar[low_loc] = temp
    print(ar, end = ' ')

selection_sort(arr)

        