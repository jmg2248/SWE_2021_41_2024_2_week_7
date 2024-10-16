from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    temp: List[int] = []
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                temp.append(i)
                temp.append(j)
                break
    return temp