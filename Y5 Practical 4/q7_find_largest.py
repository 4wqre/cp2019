def find_largest(alist):
    if len(alist) == 1:
        return alist
    elif alist[-2] > alist[-1]:
        return find_largest(alist[:len(alist)-1])
    elif alist[-1] > alist[-2]:
        del alist[-2]
        return find_largest(alist)
                            
alist = [5, 1, 8, 7, 2]
print(find_largest(alist))
