class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        answer = 0
        MOD = 10**9 + 7
        stack = []
        arr = [0] + arr + [0]  # 添加哨兵元素
        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                j = stack.pop()
                k = stack[-1]
                answer += arr[j] * (i - j) * (j - k)
            stack.append(i)
        return answer % MOD
