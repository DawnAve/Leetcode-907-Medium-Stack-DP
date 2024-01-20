class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        answer = 0
        MOD = 10**9 +7
        def calculate(arr):
            answer = 0
            left = arr[:-1].copy()
            right = arr[1:].copy()
            while len(left)>0:
                answer += min(left)
                left = left[:-1]
                
                answer += min(right)
                right = right[1:]
            answer += min(arr)
            if len(arr)>2:
                answer += calculate(arr[1:-1])

            return answer
        return calculate(arr) % MOD
