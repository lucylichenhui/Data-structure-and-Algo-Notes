class Solution(object):
	def breakPalindrome(self, palindrome):
		"""
		:type palindrome: str
		:rtype: str
		"""
		s=""
		list=[]
		for element in palindrome: 
			list.append(element)

		if len(list)==1: 
			return ""

		for i in range(len(list)): 
			if len(list)%2==1: 
				if (len(list)//2)!=i:
					if list[i]!="a":
						list[i]="a" 
						for i in list: 
							s+=i
						return s 

			else: 
				if list[i]!="a":
					list[i]="a" 
					for i in list: 
						s+=i
					return s 


		list[-1]="b"
		for i in list: 
			s+=i
		return s 