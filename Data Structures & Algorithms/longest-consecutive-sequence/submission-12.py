class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        temp = []
        if not nums :
            return 0
        if len(nums)==1:
            return 1
        nums_dup = sorted(list(set (nums)))
        for i,x in enumerate (nums_dup [0: len(nums_dup)-1]) :
            if x+1 == nums_dup[i+1] :
                count+=1
            else :
                temp.append(count)
                count = 0
        temp.append(count)
        if len(temp)>1:
            return (max(temp)+1)
        else :
            return count+1
        
                







        
        