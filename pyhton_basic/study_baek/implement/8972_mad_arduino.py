# 9 10
# ..........
# .........R
# ..........
# R.........
# R...I.....
# R.........
# ..........
# .........R
# ....R.....
# 5558888

# ....I.....
# ....R.....
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........

movable = {
    1: (1, -1),
    2: (1, 0),
    3: (1, 1),
    4: (0, -1),
    5: (0, 0),
    6: (0, 1),
    7: (-1, -1),
    8: (-1, 0),
    9: (-1, 1)
}
def get_locations(arr, r, c):
    my_key = 'I'
    mad_key = 'R'
    regist_my_loc = tuple()
    regist_mad_loc = list()

    for row in range(r):
        for col in range(c):
            if arr[row][col] == my_key :
                regist_my_loc = (row, col)
            elif arr[row][col] == mad_key:
                regist_mad_loc.append((row, col))
    
    return regist_my_loc, regist_mad_loc

def move(loc, tp):
    return (loc[0] + tp[0], loc[1] + tp[1])

def moves_mad(mad_locs, my_loc, r, c):
    result = list()
    trash = list()
    for mad in mad_locs:
        short = short_calculation(my_loc, mad, r, c)
        if short in result:
            result.remove(short)
            trash.append(short)
        elif short not in trash:
            result.append(short)
        
    return result

# |r1-r2| + |s1-s2| minimum
def short_calculation(my_loc, mad_loc, r, c):
    record = 99999999
    result_tp = tuple()
    for index in range(1, 10):
        move = movable[index]
        tmp = (mad_loc[0] + move[0], mad_loc[1] + move[1])
        if tmp[0] >= 0 and tmp[0] <= r and tmp[1] >= 0 and tmp[1] <= c:
            absolute = abs(my_loc[0] - tmp[0]) + abs(my_loc[1] - tmp[1])
            if record > absolute:
                result_tp = tmp
                record = absolute

    return result_tp

# def explosion_calcultion(mad_loc):
#     convert_set = set(mad_loc)
#     removable = list()

#     for element in convert_set:
#         for target in mad_loc:
#             if target == element:
#                 removable.append(element)

#         if len(removable) >= 2:
#             for remove in removable:
#                 mad_loc.remove(remove)

#         removable.clear()
#     return mad_loc

def print_resut(my_loc, mad_loc, r, c):
    result = [['.' for _ in range(c)] for _ in range(r)]

    result[my_loc[0]][my_loc[1]] = 'I'
    for mad in mad_locs: result[mad[0]][mad[1]] = 'R'

    convert_str = ''
    for row in range(r):
        for col in range(c):
            convert_str += result[row][col]
        convert_str += '\n'
    print(convert_str[:-1])


if __name__ == "__main__":
    r,c = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(r)]
    controls = list(map(int, input()))
    my_loc, mad_locs = get_locations(arr, r, c)

    step = 1
    for control in controls:
        my_loc = move(my_loc, movable[control])
        if my_loc in mad_locs: break
        if mad_locs:
            mad_locs = moves_mad(mad_locs, my_loc, r, c)
            # mad_locs = explosion_calcultion(mad_locs)
            if my_loc in mad_locs: break
        step += 1

    if step - 1 != len(controls):  
        result = 'kraj ' + str(step)
        print(result)
    else : print_resut(my_loc, mad_locs, r, c)





# 9 20
# ...R................
# ...............R....
# ....................
# R...................
# R......I............
# R...................
# ...............R....
# ..R......R..........
# ....R..........RR...
# 888822346161622