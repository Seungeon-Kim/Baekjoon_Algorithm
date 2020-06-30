# 1 보다 작은 분수를 여러 개의 서로 다른 단위분수의 합으로 표현할 수 있다는 것을 알아내었다. 여기서 단위분수란 분자가 1 인 분수를 말한다. 
# 예를 들어, 4/23 은 1/6 + 1/138 와 같이 두 개의 단위 분수의 합으로 나타낼 수 있다. 


# a<b 인 양의 정수 a 와 b로 이루어진 분수 a/b가 주어질 때에, 먼저 1/x1 <= a/b를 만족하는 가장 큰 단위 1/x1 분수를 계산한다. 
# 그런 다음 a/b에서 1/x1 를 뺀 나머지에 대하여 위의 과정을 반복한다. 
# 즉, 1/x2 <= a/b - 1/x1 를 만족하는 가장 큰 단위분수 1/x2를 계산하고 뺀다. 이러한 과정을 나머지가 남지 않을 때까지 반복한다.

# a/b = 5/7
# 5/7 = 1/2 + 1/5 + 1/70 [output] 마지막 분모 70

# 5/7
# 1) 1/2   1/x1 <= 5/7    5 * x1  >=  7        // x1 = 2, a = 5, b = 7
# 2) 1/5   1/x2 <= 3/14   3 * x2  >=  14       // x2 = 5, a = 3, b = 14
# 3) 1/70  1/x3 <= 1/70   1 * x3  >=  70      // x3 = 1, a = 70, b = 1

# [input]
# 3
# 4 23
# 5 7
# 8 11
# [output]
# 138
# 70
# 4070

# 루프로 돌리면 시간초과 발생.
# def get_minimum_x(a, b):
#     x = 2
#     while(True):
#         if a * x >= b:
#             break
#         else:
#             x += 1
#     return x

def get_minimum_x(a, b):
    if b % a == 0: return int(b/a)
    else: return int(b/a) + 1

def next_fraction(x, a, b):
    # (a / b) - (1 / x) = (ax - b) / (x * b)
    a, b = (a * x) - b, x * b

    # 8 12인 경우, 2 3로 리턴(최대공약수) 
    divide = get_gcd(a, b)
    return int(a / divide), int(b / divide)

#최대 공약수
def get_gcd(a, b):
    x, y = max(a,b), min(a,b)

    while x % y != 0:
        tmp = x % y
        x = y
        y = tmp
    return y

if __name__ == "__main__":
    number = int(input())
    inputs = [list(map(int, input().split())) for _ in range(number)]    

    for value in inputs:
        a, b = value[0], value[1]
        while(a != 1):
            x = get_minimum_x(a, b)
            a, b = next_fraction(x, a, b)
        print(b)


