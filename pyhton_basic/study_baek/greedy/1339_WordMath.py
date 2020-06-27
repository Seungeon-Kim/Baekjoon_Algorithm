# 2
# GCF
# ACDEB

# 99437

if __name__ == "__main__":
    num = int(input())
    arr = [list(input()) for _ in range(num)]
    dictionary = dict()

    for element in arr:
        loop = len(element)

        for i in range(0, loop):
            if element[i] not in dictionary.keys():
                dictionary[element[i]] = 0
            
            dictionary[element[i]] += 10**(loop-i)


    tmp = list()
    for val in dictionary.values():
        tmp.append(val)

    
# def convert_dict(arr):

        