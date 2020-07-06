# 4
# 2

# 2


if __name__ == "__main__":
    color_size = int(input())
    select_num = int(input())
    maximum_select = int(color_size / select_num)

    if maximum_select == select_num:
        print(0)
    elif maximum_select == 2:
        print(2)
    else:
        pass 
