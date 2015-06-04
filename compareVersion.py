class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
		v1 = version1.split('.')
		v2 = version2.split('.')
		for i in range(max(len(v1),len(v2))):
			if i > len(v1)-1:
				v1.append(0)
			if i > len(v2)-1:
				v2.append(0)
			
			v1[i] = int(v1[i])
			v2[i] = int(v2[i])
			
			if v1[i] > v2[i]:
				return 1
			elif v1[i] < v2[i]:
				return -1
		else:
			return 0

from datetime import datetime
startTime = datetime.now()
c = Solution()
print c.compareVersion("1","1.1")
print(datetime.now() - startTime)