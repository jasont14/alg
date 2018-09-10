arr = [6,5,2,4,9,1]

def insertion_sort(ar):
    #position 1 is trivally sorted
    for j in range (1,len(ar)):
        curr_eval = ar[j]
        i=j-1
        while i > -1:
            if curr_eval < ar[i]:
                ar[i+1] = ar[i]
                ar[i] = curr_eval
            i-=1
    for cout in ar:
        print(cout, end = ' ')
            

insertion_sort(arr)