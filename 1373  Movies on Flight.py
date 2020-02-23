"""***************************  TITLE  ****************************"""
"""1373  Movies on Flight.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
You are on a flight and wanna watch two movies during this flight.
You are given List movieDurations which includes all the movie durations.
You are also given the duration of the flight which is d in minutes.
Now, you need to pick two movies and the total duration of the two movies is less than or equal to (d - 30min).
"""



"""***************************  EXAMPLES  ****************************"""
"""
Example:
Input: movieDurations = [90, 85, 75, 60, 120, 150, 125], d = 250
Output: [0, 6]
Explanation: movieDurations[0] + movieDurations[6] = 90 + 125 = 215 is the maximum number within 220 (250min - 30min)

"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param arr: An integer array
    @param k: An integer
    @return: return the pair of movies index with the longest total duration
    """
    def FlightDetails(self, arr, k):
        if not arr:
            return []
            
        arr = [(num, idx) for idx, num in enumerate(arr)]
        arr.sort()
        
        left, right = 0, len(arr)-1
        best_l, best_r = None, None
        best_sum = None
        while left < right:
            while left < right and arr[left][0] + arr[right][0] < k -30:
                if best_sum is None or  arr[left][0] + arr[right][0] > best_sum:
                    best_l, best_r = left, right
                    best_sum = arr[left][0] + arr[right][0]
                
                left += 1
                
            if left < right and arr[left][0] + arr[right][0] == k-30:
                return sorted([arr[left][1], arr[right][1]])
            
            
            # now the only possibility is that arr[left] + arr[right] > k-30
            right -= 1
        return sorted([arr[best_l][1], arr[best_r][1]])
            
