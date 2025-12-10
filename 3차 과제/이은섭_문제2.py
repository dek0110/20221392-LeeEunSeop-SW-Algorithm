def knapSack_dp(W, wt, val, n):
    A = []
    for i in range(n + 1):          
        row = []
        for w in range(W + 1):      
            row.append(0)           
        A.append(row)

    for i in range(1, n + 1):       
        for w in range(1, W + 1):   
            if w < wt[i-1]:         
                A[i][w] = A[i-1][w]
            else:                   
                valWith = val[i-1] + A[i-1][w - wt[i-1]]  
                valWithout = A[i-1][w]                    
                A[i][w] = max(valWith, valWithout)       
    
    return A[n][W], A

def find_selected_items(W, wt, n, name, A):
    selected_list = []
    current_w = W
    
    for i in range(n, 0, -1):
        if A[i][current_w] != A[i-1][current_w]:
            selected_list.append(name[i-1]) 
            current_w -= wt[i-1]            
            
    return selected_list[::-1] 

names = ["노트북", "카메라", "책", "옷", "휴대용 충전기"]
weights = [3, 1, 2, 2, 1]
values = [12, 10, 6, 7, 4]
n = len(values)

try:
    W_input = int(input("배낭 용량을 입력 하세요 : "))
    max_satisfaction, dp_table = knapSack_dp(W_input, weights, values, n)
    selected_items = find_selected_items(W_input, weights, n, names, dp_table)

    print(f"최대 만족도: {max_satisfaction}")
    print(f"선택된 물건: {selected_items}")

except ValueError:
    print("유효한 숫자를 입력해주세요.")