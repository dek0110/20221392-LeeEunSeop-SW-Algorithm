def count_stairs_ways(n):
    if n <= 0: return 0
    if n == 1: return 1
    if n == 2: return 2
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[n]

try:
    n_input = int(input("계단의 개수를 입력하시오: "))
    print(f"{n_input}개의 계단을 오르는 방법의 수는 {count_stairs_ways(n_input)}가지입니다.")
except ValueError:
    print("숫자를 입력해주세요.")