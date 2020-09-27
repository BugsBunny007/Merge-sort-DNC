#INPUT:-
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)
alist = []
n=input("How many no. you want to insert")
for i in range(n):
    a=int(input("Enter value"))
    alist.append(a) 

mergeSort(alist)
print(alist)

#OUTPUT:-
#python MSR.py 
#How many no. you want to insert5
#Enter value5
#Enter value4
#Enter value2
#Enter value3 
#Enter value1
#('Splitting ', [5, 4, 2, 3, 1])
#('Splitting ', [5, 4])
#('Splitting ', [5])
#('Merging ', [5])
#('Splitting ', [4])
#('Merging ', [4])
#('Merging ', [4, 5])
#('Splitting ', [2, 3, 1])
#('Splitting ', [2])
#('Merging ', [2])
#('Splitting ', [3, 1])
#('Splitting ', [3])
#('Merging ', [3])
#('Splitting ', [1])
#('Merging ', [1])
#('Merging ', [1, 3])
#('Merging ', [1, 2, 3])
#('Merging ', [1, 2, 3, 4, 5])
#[1, 2, 3, 4, 5]
