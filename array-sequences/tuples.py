# Tuples used as records 

lax_coordinates = (33.9425, -118.888)
city, year, pop, chg, area = ("Tokyo", 2003, 32.450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print("%s/%s" % passport)

for country, _ in traveler_ids:
    print(country)



# Tuples as inmutable data structures. 

a = (10, "alpha", [1,2])
b = (10, "alpha", [1,2])

print(a==b)

b[-1].append(99)

print(a==b)


