def quicksort (A):
    if len(A) <= 1:
        return A
    else:
        pivot = A.pop(0)
    
    items_lower = []
    items_higher = []

    for item in A[1:]: #skipping pivot
        if item.lower() > pivot.lower():
            items_higher.append(item)
        else:
            items_lower.append(item)

    return quicksort(items_lower) + [pivot] + quicksort(items_higher)
 
    