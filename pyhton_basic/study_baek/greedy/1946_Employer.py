# 테스트 케이스의 수
# 2

#   인원
# 5

# 1차 2차
# 3 2
# 1 4
# 4 1
# 2 3
# 5 5

# 7
# 3 6
# 7 3
# 4 2
# 1 4
# 5 7
# 2 5
# 6 1

import sys 

if __name__ == "__main__":
    result = list()
    tc_number = int(sys.stdin.readline())

    for i in range(tc_number):
        people = int(sys.stdin.readline())
        grades = [ tuple(map(int, sys.stdin.readline().split())) for _ in range(people)]        
        # prior_grade = sorted(grades, key=lambda index_value: index_value[0])
        grades.sort()

        cnt = 1
        cut_line = grades[0][1]
        for i in range(1, people):
            if cut_line > grades[i][1]:
                cnt += 1
                cut_line = grades[i][1]


        result.append(cnt)
            
    for prt in result:
        print(prt)

            