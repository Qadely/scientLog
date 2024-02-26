def time(t1, t2):
    '''
    :t1 первое время формата гггг-мм-дд
    :t2 второе время формата гггг-мм-дд
    :return True, если первое время больше второго
    '''
    t1 = [int(_) for _ in t1.split("-")]
    t2 = [int(_) for _ in t2.split("-")]
    if t1[0] > t2[0]:
        return True
    elif t1[0] == t2[0] and t1[1] > t2[1]:
        return True
    elif t1[0] == t2[0] and t1[1] == t2[1] and t1[2] > t2[2]:
        return True
    return False


with open("C:/Users/examen/Documents/scientLog/scientist.txt", "r", encoding="utf-8") as file:
    reader = file.readlines()
    preps = {"Аллопуринол": []}
    lecs = []
    for row in range(1, len(reader) - 1):
        rs = reader[row].split("#")
        if rs[1] not in preps:
            preps[rs[1]] = rs
        if rs[1] == "Аллопуринол":
            preps[rs[1]] += [[rs[0], rs[2]]]
        elif time(rs[2], preps[rs[1]][2]):
            preps[rs[1]] = rs
        if rs[1] not in lecs:
            lecs.append(rs[1])

with open("C:/Users/examen/Documents/scientLog/scientist_origin.txt", "w", encoding="utf-8") as filew:
    filew.write("ScientistName#preparation#date#components\n")
    for i in lecs:
        if i != "Аллопуринол":
            filew.write("#".join(preps[i]))
        else:
            gs = preps[i]
            for _ in range(0, len(gs) - 1):
                for i in range(_, len(gs) - 1):
                    x, y = gs[_], gs[i]
                    if time(x[-1], y[-1]):
                        gs[_] = y
                        gs [i] = x 
            print(f"Разработчиками Аллопуринола были такие люди:")
            for _ in gs[::-1]:
                print(f"{_[0]}-{_[1]}")
        

