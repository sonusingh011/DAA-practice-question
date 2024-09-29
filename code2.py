# Function to find both maximum and minimum
def find_max_min(arr, low, high):
    if low == high:
        return arr[low], arr[low]
    
    if high == low + 1:
        if arr[low] > arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    
    mid = (low + high) // 2
    
    max1, min1 = find_max_min(arr, low, mid)
    
    max2, min2 = find_max_min(arr, mid + 1, high)
    
    overall_max = max(max1, max2)
    overall_min = min(min1, min2)
    
    return overall_max, overall_min

arr = [3, 5, 1, 8, 9, 2, 7, 6]
max_val, min_val = find_max_min(arr, 0, len(arr) - 1)
print("Maximum:", max_val)
print("Minimum:", min_val)
