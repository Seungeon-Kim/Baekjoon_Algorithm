# AC는 정수 배열에 연산을 하기 위해 만든 언어이다. 이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.
# 함수 R은 배열에 있는 숫자의 순서를 뒤집는 함수이고, D는 첫 번째 숫자를 버리는 함수이다. 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.

# 4
# RDD
# 4
# [1,2,3,4]
# DD
# 1
# [42]
# RRD
# 6
# [1,1,2,3,5,8]
# D
# 0
# []

# [2,1]
# error
# [1,2,3,5,8]
# error


if __name__ == "__main__":
    num = int(input())
    controls = list()
    values = list()

    for i in range(num):
        controls.append(list(input()))
        garbage = int(input())
        elements = list(input())
        elements.remove('[')
        elements.remove(']')
        if elements and ',' in elements:
            while ',' in elements:
                elements.remove(',')
            values.append(elements)
        else : values.append(list('-'))


    while controls and values:
        control = controls.pop(0)
        value = values.pop(0)
        
        if value[0] != '-':
            for key in control:
                if key == 'R':
                    value.reverse()
                else :
                    if value:
                        value.pop(0)
                    else: 
                        print('error')
                        break
            print(value)
        else: print('error')
