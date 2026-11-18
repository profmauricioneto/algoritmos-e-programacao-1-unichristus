t = "um tigre, dois tigres, três tigres"
i = 0
while i > -1:
    i = t.find("tigre", i)
    if i >= 0:
        print(f"Posição: {i}")
        i += 1 