s = 0
l = 0
run = True
while run:
    a = int(input("enter a number: "))
    if a < 0:
        # break
        run = False
    else:
        s += a
        l += 1
print(s/l)