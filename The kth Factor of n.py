def subsets( nums):
    res = [[]]
    for n in nums:
        for i in range(len(res)):
            res.append(res[i] + [n])
            print(res)
    return res
nums=[1,2]
print(subsets(nums))