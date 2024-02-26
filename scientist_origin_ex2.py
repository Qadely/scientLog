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
    reader = list((file.readlines()))
    for _ in range(1, len(reader)):
        for i in range(_, len(reader) - 1):
            x, y = reader[_].split("#"), reader[i].split("#")
            if time(x[2], y[2]):
                reader[_] = y
                reader[i] = x 


with open("C:/Users/examen/Documents/scientLog/scientist2.txt", "r", encoding="utf-8") as filew:
    filew.write("ScientistName#preparation#date#components\n")
    for i in reader:
        filew.write("#".join(i))