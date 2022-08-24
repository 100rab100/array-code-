def getInvCount(arr, n):

	inv_count = 0
	for i in range(n):
		for j in range(i + 1, n):
			if (arr[i] > arr[j]):
				inv_count += 1

	return inv_count


# Driver Code
arr = [1, 20, 6, 4, 5]
n = len(arr)
print("Number of inversions are",getInvCount(arr, n))
'''
Complexity Analysis: 
Time Complexity: O(n^2), Two nested loops are needed to traverse the array from start to end, so the Time complexity is O(n^2)
Space Complexity:O(1), No extra space is required.'''
