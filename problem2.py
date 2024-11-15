# Approach1: heaps
# Time: O(klogn)
# Space: O(n)

import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minheap = []

        # Initialize the heap with the first element of each row, up to `min(n, k)` rows
        for row in range(min(len(matrix), k)):
            heapq.heappush(minheap, (matrix[row][0], row, 0))
        
        # Extract min k-1 times to reach the k-th smallest element
        for _ in range(k - 1):
            ele, row, col = heapq.heappop(minheap)

            # If there's a next element in the same row, push it into the heap
            if col + 1 < len(matrix[row]):
                heapq.heappush(minheap, (matrix[row][col + 1], row, col + 1))
        
        # The k-th smallest element is now at the top of the heap
        return heapq.heappop(minheap)[0]

# Approach2: binary search
# Total Time Complexity: O(n × log(max-min))
# Binary search range is (max-min) where:
# max = matrix[n-1][n-1]
# min = matrix[0][0]
# Each iteration does O(n) work in count_less_equal
# Total iterations: O(log(max-min))

# Space Complexity: O(1)
# Only using constant extra space for variables
# No additional data structures used

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        low, high = matrix[0][0], matrix[-1][-1]

        # Binary search for the kth smallest value
        while low < high:
            mid = (low + high) // 2
            count = self.count_less_equal(matrix, mid)
            
            # Adjust search range based on count
            if count < k:
                low = mid + 1
            else:
                high = mid

        return low

    def count_less_equal(self, matrix, target):
        n = len(matrix)
        count = 0
        row = n - 1  # Start from the last row
        col = 0      # Start from the first column
        
        while row >= 0 and col < n:
            if matrix[row][col] <= target:
                count += (row + 1)  # All elements in this column up to `row` are <= target
                col += 1  # Move right
            else:
                row -= 1  # Move up
        return count
