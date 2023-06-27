symbols = '$¢£¥€¤'
tuple(ord(symbol) for symbol in symbols)

import array
print(array.array("I", (ord(symbol) for symbol in symbols)))


# We build a cartesian product using generator expression, without storing it in memory

colors = ["black", "white"]
sizes = ['S', 'M', 'L']

for tshirts in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirts)



