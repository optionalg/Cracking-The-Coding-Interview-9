'''
A child can climb stairs by 1, 2, or 3 steps.
Given the number of levels, count how many ways he can climb to the top.

Solution
<Dynamic Programming>

K(n) = K(n-1) + K(n-2) + K(n-3)

'''

def numOfSteps(level):

	if level < 0:
		return 0
	if level == 0:
		return 1
	else:
		
		return numOfSteps(level - 1) + \
				numOfSteps(level - 2) + \
				numOfSteps(level - 3)

print numOfSteps(7)