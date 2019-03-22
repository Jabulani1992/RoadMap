def bubble_sort(items):
    '''Return array of items, sorted in ascending order'''
    for k in range(len(items)-1,0,-1):
        for i in range(k):
            if items[i]>items[i+1]:
                new_list = items[i]
                items[i] = items[i+1]
                items[i+1] = new_list
    return items

def merge_sort(items):
    '''Return array of items, sorted in ascending order'''
    if len(items) > 1:
        middle = len(items)//2
        left = items[:middle]
        right = items[middle:]

        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                items[k] = left[i]
                i = i + 1
            else:
                items[k] = right[j]
                j=j+1
            k += 1

        while i< len(left):
            items[k]= left[i]
            i+=1
            k+=1

        while j < len(right):
            items[k]= right[j]
            j+=1
            k+=1
    return items

def quick_sort(items):
    '''Return array of items, sorted in ascending order'''
    def quickSort2(items,first,last):
       if first<last:
           point = divide(items,first,last)
           quickSort2(items,first,point-1)
           quickSort2(items,point+1,last)

    def divide(items,first,last):
       pivotvalue = items[first]
       left = first+1
       right= last

       done = False
       while not done:
           while left <= right and items[left] <= pivotvalue:
               left = left + 1
           while items[right] >= pivotvalue and right >= left:
               right = right -1

           if right < left:
               done = True
           else:
               temp = items[left]
               items[left] = items[right]
               items[right] = temp

       temp = items[first]
       items[first] = items[right]
       items[right] = temp
       return right

    quickSort2(items,0,len(items)-1)
    return items
