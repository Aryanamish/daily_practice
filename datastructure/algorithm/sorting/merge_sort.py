def mergesort(array):
    if len(array) > 1:
        left = array[:len(array)//2]
        right = array[len(array)//2:]
        mergesort(left)
        mergesort(right)
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k+=1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
        

a = [3,4,6,1,8,3,4]
mergesort(a)
print(a)
            

a = 'ababa'


print('palindrone' if a == a[::-1] else 'not palindrone')