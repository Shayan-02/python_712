i = 1
while i <= 20:
    if i == 17:
        break
    elif i == 13 or i == 7:
        i += 2
        continue
    print(i)
    i += 1