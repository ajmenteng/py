#import numpy as np
class Solution:
    # @param {integer} n
    # @return {integer}
	def countPrimes(self,n):
		if n <= 2:
			return False
		l = [True] * n
		l[0] = l[1] = False
		i = 2
		while i*i < n:
			if l[i]:
				j = i + i
				while j < n:
					l[j] = False
					j += i
			i += 1
		count = 0
		for k in l:
			if k:
				count += 1
		return count
		
from datetime import datetime
startTime = datetime.now()
primes = Solution()
#print(primes.countPrimes(200))
print(primes.countPrimes(999983))
print(datetime.now() - startTime)