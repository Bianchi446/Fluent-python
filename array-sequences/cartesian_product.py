colors = ["black", "white"]

sizes = ["S", "M", "L"]

# Iterating : V1

tshirts = [(color, size) for color in colors for size in sizes]

print(tshirts)


# Iterating : V2

for color in colors:
    for size in sizes:
        print((color, size))



