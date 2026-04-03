def add_binary(a, b):
    a = a[2:]
    b = b[2:]
    c = len(a) - 1
    d = len(b) - 1
    abcd = 0
    result = ""
    while c >= 0 or d >= 0:
        if c >= 0:
            if a[c] == "1":
                a1 = 1
            else:
                a1 = 0
        else:
            a1 = 0
        if d >= 0:
            if b[d] == "1":
                b2 = 1
            else:
                b2 = 0
        else:
            b2 = 0
        total = a1 + b2 + abcd
        if total == 0:
            result = "0" + result
            abcd = 0
        elif total == 1:
            result = "1" + result
            abcd = 0
        elif total == 2:
            result = "0" + result
            abcd = 1
        else:
            result = "1" + result
            abcd = 1
        c = c - 1
        d = d - 1
    if abcd == 1:
        result = "1" + result
    return "0b" + result
            
        
            
        