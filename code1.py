def merge_sort(arr):
  if len(arr)<=1:
    return arr
  mid=len(arr)//2
  l_half=arr[:mid]
  r_half=arr[mid:]
  l_half=merge_sort(l_half)
  r_half=merge_sort(r_half)
  return merge(l_half,r_half)

def merge(l_half,r_half):
  new=[]
  i,j=0,0
  while i<len(l_half) and j<len(r_half):
    if l_half[i]<r_half[j]:
      new.append(l_half[i])
      i+=1
    else:
      new.append(r_half[j])
      j+=1
  new.extend(l_half[i:])
  new.extend(r_half[j:])
  return new

arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)