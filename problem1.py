# Approach1: heap
# Time: O(nlogn)
# Space: O(n)

import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort()
        rooms = []

        for start, end in intervals:
            heapq.heappush(rooms, end)
        
            if rooms[0] <= start:
                heapq.heappop(rooms)
        
        return len(rooms)
    

# Approach2: Sweep Line
# Time: O(nlogn)
# Space: O(n)

class Solution:
    def minMeetingRooms(self, intervals):
        events = []
        for start, end in intervals:
            events.append((start, 1))  # Start of a meeting (room needed)
            events.append((end, -1))   # End of a meeting (room freed)
        
        events.sort()  # Sort events based on time, with tie-breaking on type (end before start)
        
        max_rooms_needed = current_rooms = 0
        for _, event in events:
            current_rooms += event  # Update the number of rooms in use
            max_rooms_needed = max(max_rooms_needed, current_rooms)  # Track the maximum rooms used
        
        return max_rooms_needed