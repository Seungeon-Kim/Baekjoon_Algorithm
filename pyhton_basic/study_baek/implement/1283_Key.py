# 5
# New
# Open
# Save
# Save As
# Save All

# [N]ew
# [O]pen
# [S]ave
# Save [A]s
# Sa[v]e All

# 6
# New
# Open
# Save
# Save As
# Save All
# SA

# 32
def print_result(string, word):
    if word != '-':
        index = string.find(word)

        result = string[:index] + '[' + string[index:]
        result = result[:index+2] + ']' + result[index+2:]

        print(result)
    else: print(string)

if __name__ == "__main__":
    result = list()
    number = int(input())
    arr = [list(input().split()) for _ in range(number)]
    size = 0
    for values in arr:
        isFlag = True
        size += 1
        for value in values:
            if value[0] not in result:
                result.append(value[0])
                isFlag = False
                break

        if isFlag:
            for value in values:
                str_length = len(value)
                for i in range(1, str_length):
                    if value[i] not in result and value[i].upper() not in result:
                        result.append(value[i])
                        isFlag = True
                        break
                if isFlag == True: break
        if len(result) != size:
            result.append('-')

    print(result)
    for strings in arr:
        tmp = str()
        for string in strings:
            tmp += str(string)
            tmp += ' '
        print_result(tmp[0:-1], result.pop(0))
