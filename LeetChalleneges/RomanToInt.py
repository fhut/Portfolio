
def romanToInt(s):

    s_split = list(s)
    s_len = len(s_split)

    values = {'I':1,
              'V':5,
              'X':10,
              'L':50,
              'C':100,
              'D':500,
              'M':1000}

    total = 0
    index = 0

    siter = iter(s_split)

    for each in siter:
        try:
            nxt = next(siter)

            print(values[each] / 10)
            print(values[nxt] / 10)
        except:
            pass








    return total

print(romanToInt("MCMXCIV"))

#"MCMXCIV"
1000
100
1000
10
100
1
5


