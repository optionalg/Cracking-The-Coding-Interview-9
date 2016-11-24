class FindSubsets:
	def subsets(self, set):
		return self.find_subsets([], set)

	def find_subsets(self, prev, subset):
		if subset:
			cur = subset[0]
			return self.find_subsets(prev, subset[1:]) + self.find_subsets(prev + [cur], subset[1:])

		return [prev]

print FindSubsets().subsets([2, 1, 3])
