# Not a leetcode question
# Experimentation with k smallest/largest items

# For k smallest => Use max-heap of size K
# Beacause, max-heap pops the maximum item, when all (n-k) max items are popped, you'll end up with (k) smallest items

# For k largest => Use min-heap of size K
# Justification is same as above

import heapq

class Solution:
	def __init__(self, k, items):
		self.k = k
		self.items = items
		print(k, items)

	def k_smallest(self):
		heap = []
		heapq.heapify(heap)

		# Put all items in Heap
		# for item in self.items:
		# 	heapq.heappush(heap, item)
		
		# print(heapq.nsmallest(self.k, heap))

		# Maintain only K item max-heap
		for item in self.items:
			heapq.heappush(heap, -1 * item)

			if len(heap) > self.k:
				heapq.heappop(heap)
		
		print("K item max-heap :",[-1 * i for i in heap])

	def k_largest(self):
		heap = []
		heapq.heapify(heap)

		# Put all items in Heap
		# for item in self.items:
		# 	heapq.heappush(heap, item)
		
		# print(heapq.nlargest(self.k, heap))

		# Maintaining only K item min-heap
		for item in self.items:
			heapq.heappush(heap, item)

			if len(heap) > self.k:
				heapq.heappop(heap)
		
		print("K item min-heap :",heap)

if __name__ == "__main__":
	solution = Solution(3, [0,1,2,3,4,5,6,7,8,9])
	print("k-smallest : ")
	solution.k_smallest()
	print("k-largest : ")
	solution.k_largest()