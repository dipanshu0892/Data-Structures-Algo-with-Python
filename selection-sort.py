# Selection Sort

def selectionSort(arr):
  n = len(arr)
  for i in range(n):
    mini = i
    for j in range(i,n):
      if arr[j] < arr[mini]:
        mini = kj
    arr[i], arr[mini] = arr[mini], arr[i]

arr = [1,2,43,421,3,1,2,32,1,9,23,8]
selectionSort(arr)
print(arr)
