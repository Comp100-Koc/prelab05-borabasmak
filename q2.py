def remove_adjacent_duplicates(s):
    while True:
        i = 0
        new = ""
        remove = False
        while i < len(s):
            if i <len(s) -1:
                if s[i] == s[i + 1]:
                    remove = True
                    i = i + 2
                else:
                    new += s[i]
                    i += 1
            else:
                new += s[i]
                i += 1
        if remove == False:
            break
        s = new
    return s
 