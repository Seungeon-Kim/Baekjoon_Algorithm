# 4
# 0 2 1 3

# 1 // 1 0 / 1 + 0 / 1
# 2 // 2 1 0 / 1 + 1 / 2
# 3 // 3 2 1 0 / 1 + 1 + 2 / 4
# 5 // 4 3 2 1 0 / 1 + 1 + 2 + 3 / 7


import sys
import copy

def make_sequences(number, teams):
    pivot_sequence = [i for i in range(number-1, -1, -1)]
    if teams == pivot_sequence : return 1
    
    for i in range(0, number-2):
        for j in range(i+2, number):
            tmp = pivot_sequence.deepcopy()
            tmp[i] -= 1
            tmp[j] += 1
            if teams == tmp :  return 1
            
    return -1

if __name__ == "__main__":
    number = int(sys.stdin.readline())
    teams = list(map(int, sys.stdin.readline().split()))

    teams.sort(reverse=True)
    result = make_sequences(number, teams)
    print(result)