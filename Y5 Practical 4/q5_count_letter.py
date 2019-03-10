def count_letter(str,ch):
    if len(str) == 0:
        return 0
    elif str[len(str)-1:len(str)] == ch:
        return count_letter(str[0:len(str)-1], ch) + 1
    else:
        return count_letter(str[0:len(str)-1], ch)

print(count_letter("Welcome", "e"))
