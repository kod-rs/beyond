h = []

def add(h, new_val):

    if h:
        if h[-1] == new_val:
            return h

        if new_val in h:
            h.remove(new_val)

    h.append(new_val)
    if len(h) > 10:
        h.pop(0)
    return h


def add(h, new_val):

    if h:
        print("last", h[-1])
        if h[-1] == new_val:
            print("last value same as new, no add")
            return h

        if new_val in h:
            print("already have this")
            h.remove(new_val)
    else:
        print("empty, no check")

    h.append(new_val)
    if len(h) > 10:
        h.pop(0)
    return h
"""
dode vrijednost ako postoji onda brisi
sigurni smo da neema duplih
# uzmi zadnjih 10, ostalo obrisi
# ako ima vise od 10 obrisi zadnji
ako ih je 10 obrisi zadnji
"""

# h.append(0)

for i in [1,1,2,3,4,3,5,6,12,7,8,9,10,11,1,1,3,2,1,6,13,2,1,3,2,1,2,1,2,]:
    print(add(h, i), len(h), i)
    print(80 * "-")

# print(add(h, 1))
# print(80 * "-")
# print(add(h, 1))
# print(80 * "-")
# print(add(h, 2))
# print(80 * "-")
# print(add(h, 1))
# print(80 * "-")
