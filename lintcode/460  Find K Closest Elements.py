"""***************************  TITLE  ****************************"""
"""460  Find K Closest Elements.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given target, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.
"""



"""***************************  EXAMPLES  ****************************"""
"""
target
"""



"""***************************  CODE  ****************************"""
                return right
            if A[left] <= target:
                return left
                
            return -1
        left_closest = find_closest_smaller(A, target)
        if left_closest == -1:
            return A[:k]
        result = []
        left, right = left_closest, left_closest+1
        while left >= 0 and right < len(A) and len(result) < k:
            if abs(A[left] - target) < abs(A[right] - target):
                result.append(A[left])
                left -= 1
            elif abs(A[left] - target) > abs(A[right] - target):
                result.append(A[right])
                right += 1
            else:
                result.append(A[left])
                left -= 1
        if len(result) == k:
            return result
        
        while left >= 0 and len(result) < k:
            result.append(A[left])
            left -= 1
            
        while right < len(A) and len(result) < k:
            result.append(A[right])
