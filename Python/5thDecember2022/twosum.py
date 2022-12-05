class Solution:
	def twoSum(self, A: List[int], target: int) -> List[int]:
		for i in range(len(A)):
			for j in range(i+1,len(A)):
				if(A[i]+A[j] == target):
					return [i,j]
