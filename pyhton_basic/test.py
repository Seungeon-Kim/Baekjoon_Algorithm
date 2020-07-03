def solution(array, commands):
    answer = []
    
    for command in commands:
        i,j,k = command[0]-1, command[1], command[2]-1
        
        tmp = array[i:j]
        print("tmp :: " , tmp)
        tmp.sort()
        answer.append(tmp[k])
    return answer

if __name__ == "__main__":
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    print(solution(array, commands))

# # array	commands	return
# 		[5, 6, 3]