def sub_lists(my_list):
    subs = [[]]
    for i in range(len(my_list)):
        n = i+1
        while n <= len(my_list):
            sub = my_list[i:n]
            subs.append(sub)
            n += 1
            print(n)
    return subs

