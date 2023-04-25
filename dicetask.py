for i in range(1, 7):
    for j in range(1, 7):
        if i+j > 6:
            break
        print(i, ",", j)
    if i == 6:
        print("6, 6")
