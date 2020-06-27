def init_UCPC():
    arr = list()
    arr.append('U')
    arr.append('C')
    arr.append('P')
    arr.append('C')

    return arr


if __name__ == "__main__":
    arr = init_UCPC()
    str_input = list(input())

    for value in str_input:
        if len(arr) == 0:
            break
        elif len(arr) > 0 and value == arr[0]:
            del arr[0]

    if len(arr) == 0 :
        print('I love UCPC')
    else:
        print('I hate UCPC')
