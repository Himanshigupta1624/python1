# def get_ans(N, Tpos, Shpos):
#     count = 0
    
#     # For prefix attacks (destroys positions 1 to L)
#     for L in range(N+1):
#         if Tpos > L and Shpos > L:
#             count += 1
    
#     # For suffix attacks (destroys positions N-L+1 to N)
#     # For L=1, positions N to N are destroyed
#     # For L=2, positions N-1 to N are destroyed, etc.
#     for L in range(1, N+1):
#         # For treasures to be safe, they must be at positions <= N-L
#         if Tpos <= N-L and Shpos <= N-L:
#             count += 1
    
#     return count

# def main():
#     # Test cases with detailed output
#     test_cases = [(4, 4, 2), (3, 1, 2)]
    
#     for N, Tpos, Shpos in test_cases:
#         prefix_count = 0
#         suffix_count = 0
        
#         # Debug prefix attacks
#         print(f"\nFor N={N}, Tpos={Tpos}, Shpos={Shpos}:")
#         print("Prefix attacks (L=0 to N):")
#         for L in range(N+1):
#             safe = Tpos > L and Shpos > L
#             prefix_count += 1 if safe else 0
#             print(f"  L={L}: {'Safe' if safe else 'Not safe'}")
        
#         # Debug suffix attacks
#         print("Suffix attacks (L=1 to N):")
#         for L in range(1, N+1):
#             safe = Tpos <= N-L and Shpos <= N-L
#             suffix_count += 1 if safe else 0
#             print(f"  L={L}: {'Safe' if safe else 'Not safe'}")
        
#         total = prefix_count + suffix_count
#         print(f"Total safe configurations: {total} (Prefix: {prefix_count}, Suffix: {suffix_count})")
    
# if __name__ == "__main__":
#     main()
import sys
import math

sys.setrecursionlimit(10**6)

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def compute_lcm(arr):
    result = 1
    for num in arr:
        result = lcm(result, num)
    return result

def get_ans(N, A):
    lcm_total = compute_lcm(A)

    dp = []
    current_lcm = 0
    for num in A:
        if not dp or num >= dp[-1]:
            next_lcm = lcm(current_lcm, num) if current_lcm else num
            if next_lcm != lcm_total:
                dp.append(num)
                current_lcm = next_lcm
            else:
                # Try to skip this to avoid lcm_total
                pass

    return len(dp)

def main():
    N = int(sys.stdin.readline().strip())
    A = []
    for _ in range(N):
        A.append(int(sys.stdin.readline().strip()))

    result = get_ans(N, A)
    print(result)

if __name__ == "__main__":
    main()
