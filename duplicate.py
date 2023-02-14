my_list = []
elem = [w, w, w, o, r, l, d, g, g, g, g, r, e, a, t, t, e, c, c, h, e, m, g, g, p, w, w]
my_list.append([elem[0]])
for _ in range(1, len(elem)):
    if my_list[_ - 1] == elem[_]:
        my_list[_ - 1].extend(elem[_])
    else:
        my_list.append([elem[_]])

print(my_list)