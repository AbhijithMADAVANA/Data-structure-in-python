def max_heapify(A,n,i):
    l = left(i)
    r = right(i)
    if l < n and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < n and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A,n, largest)


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


# here we need to swap root elemetn with last element so we need to take n as length of array
def build_max_heap(A):
    n = len(A)
    for i in range(n, -1,-1):
        max_heapify(A,n, i)
        
    for i in range(n-1,-1,-1):
      A[0],A[i]=A[i],A[0]
      # here we are doing heapify with only first root elemet as it has been swapped, so passing array A and index 0 with mediator i
      # mediatore i means elements in arary till i th postion is unsorted and rest of elements are sorted.After each recursion, we need to pass i 
      #because as i is in decrementing order(i in range n-1,-1,-1) it will perform heapify operation till elements at i th postion. because
      # elements after i th postions are alreday sorted.
      max_heapify(A,i,0)


A = [11,6,5,0,8,2,7]
build_max_heap(A)
print(A)