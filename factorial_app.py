import time

def factorial_iter(n: int) -> int:
    
    if n < 0:
        raise ValueError("입력값 n은 0 이상이어야 합니다.")
    
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_rec(n: int) -> int:
    if n < 0:
        raise ValueError("입력값 n은 0 이상이어야 합니다.")
        
    if n <= 1: # 기본 조건(Base case): n이 0 또는 1이면 1을 반환
        return 1
    else: # 재귀 단계(Recursive step)
        return n * factorial_rec(n - 1)

def run_with_time(func, n: int) -> tuple:
   
    start_time = time.perf_counter()
    result = func(n)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return result, elapsed_time

def run_test_cases():
    test_cases = [5, 10, 20, 50, 100, 500]
    print("\n" + "="*50)
    print("사전 정의된 테스트 케이스 일괄 수행")
    print("="*50)
    print(f"{'n':>5} | {'반복 방식 시간(s)':>20} | {'재귀 방식 시간(s)':>20}")
    print("-" * 50)
    for n in test_cases:
        try:
            _, iter_time = run_with_time(factorial_iter, n)
            _, rec_time = run_with_time(factorial_rec, n)
            print(f"{n:>5} | {iter_time:>20.10f} | {rec_time:>20.10f}")
        except RecursionError:
            print(f"{n:>5} | {iter_time:>20.10f} | {'RecursionError 발생':>20}")
        except Exception as e:
            print(f"n={n} 처리 중 오류 발생: {e}")
    print("="*50)


def main():
    while True:
        print("\n===== 팩토리얼 계산 프로그램 =====")
        print("1. 반복(Iterative) 방식 계산")
        print("2. 재귀(Recursive) 방식 계산")
        print("3. 두 방식 비교")
        print("4. 테스트 케이스 일괄 수행")
        print("5. 종료")
        print("="*31)
        
        choice = input("메뉴를 선택하세요: ")

        if choice in ('1', '2', '3'):
            try:
                n_str = input("계산할 정수 n을 입력하세요 (n ≥ 0): ")
                n = int(n_str)

                if choice == '1':
                    result, elapsed_time = run_with_time(factorial_iter, n)
                    print(f"\n[반복] 결과: {n}! = {result}")
                    print(f"경과 시간: {elapsed_time:.10f} 초")
                
                elif choice == '2':
                    result, elapsed_time = run_with_time(factorial_rec, n)
                    print(f"\n[재귀] 결과: {n}! = {result}")
                    print(f"경과 시간: {elapsed_time:.10f} 초")

                elif choice == '3':
                    print("\n--- [비교 결과] ---")
                    iter_result, iter_time = run_with_time(factorial_iter, n)
                    print(f"  - 반복 방식 결과: {iter_result}")
                    print(f"  - 반복 방식 시간: {iter_time:.10f} 초")
                    rec_result, rec_time = run_with_time(factorial_rec, n)
                    print(f"  - 재귀 방식 결과: {rec_result}")
                    print(f"  - 재귀 방식 시간: {rec_time:.10f} 초")
                    if iter_time < rec_time:
                        print("\n >> 반복 방식이 더 빨랐습니다.")
                    else:
                        print("\n >> 재귀 방식이 더 빨랐거나 시간이 동일했습니다.")
            
            except ValueError as ve:
                print(f"오류: 잘못된 입력입니다. {ve}")
            except Exception as e:
                print(f"알 수 없는 오류가 발생했습니다: {e}")

        elif choice == '4':
            run_test_cases()

        elif choice == '5':
            print("프로그램을 종료합니다.")
            break
            
        else:
            print("오류: 1, 2, 3, 4, 5 중 하나를 입력해주세요.")


if __name__ == "__main__":
    main()