def addTwoNumbers(l1, l2):
    longest = l1 if len(l1) > len(l2) else l2
    shortest = l1 if len(l1) < len(l2) else l2
    total_len = len(longest)
    res = []

    for each in range(len(longest) - len(shortest)):
        shortest.append(0)

    for index in range(total_len):
        added = shortest[index] + longest[index]

        res.append(added)

    for each in range(len(res)):
        if res[each] >= 9:
            res[each] %= 10

            try:
                res[each + 1] += 1

            except:
                res.append(1)

    return list(reversed(res))