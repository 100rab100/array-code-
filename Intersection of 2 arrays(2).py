# Approach 1
def Intersection(lst1, lst2):
	return set(lst1).intersection(lst2)
# return list(set(nums1) & set(nums2))	
# Driver Code
lst1 = [ 4, 9, 1, 17, 11, 26, 28, 28, 26, 66, 91]
lst2 = [9, 9, 74, 21, 45, 11, 63]
print(Intersection(lst1, lst2))
# Approach 2
def inter (nums1,nums2):
  res=[]
  for i in nums:
    if i not in res and i in nums2:
      res.append(i)
  return res
