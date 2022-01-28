def change():

    cost = float(input("Enter cost of purchase: "))
    assert str(cost)[::-1].find('.') <= 2, f"{cost} is invalid format, please input cost as inf<-#.##"

    amount_given = float(input("Enter amount given: "))
    assert str(amount_given)[::-1].find('.') <= 2, f"{amount_given} is invalid, format please input cost as inf<-#.##"

    change_total = amount_given - cost

    change_to_give_back={100:0,
                        50:0,
                        20:0,
                        10:0,
                        5:0,
                        2:0,
                        1:0,
                        .25:0,
                        .10:0,
                        .05:0,
                        .01:0}

    for denomination in change_to_give_back.keys():
        change_to_give_back[denomination] = round(change_total // denomination)
        change_total %= denomination

    lines = []
    for denomination, count in change_to_give_back.items():
        if count > 0:
            if denomination % 1 == 0:
                lines.append(f"{denomination}'s: {count} = {denomination * count}\n")
            else:
                lines.append(f"{denomination}: {count} = {denomination * count}\n")

    return "".join(lines)


print(change())