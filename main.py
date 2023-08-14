from collections import Counter
class Solution:
	def singleNumber(self, nums):
		# Code here
		d=Counter(nums)
		a=[]
		for key,value in d.items():
		    if value==1:
		        a.append(key)
		        if(len(a)==2):
		            a.sort()
		            return a