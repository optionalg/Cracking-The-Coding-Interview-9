def LengthOfLongestIncreasingSubsequence(lst):
	l = [1] * len(lst)
	for i in range(len(lst)):
		for j in range(i):
			if lst[j] < lst[i]:
				if l[i] <= l[j]:
					l[i] = 1 + l[j]
	max_length = max(l)
	print "Longest increasing subsequence is of length ", max_length
	return l
	

print LengthOfLongestIncreasingSubsequence([3, 4, -1, 0, 6, 2, 3])