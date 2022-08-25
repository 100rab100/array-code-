def bsdk(nums, target):
    for i in range(n):

        for j in range(i + 1, n):
           if target == nums[i] + nums[j]:
               return ([i,j])
              # break

          #  return [i,j]


nums = [2,7,11,15]
n = len(nums)
target = 9
print(bsdk(nums, target))
