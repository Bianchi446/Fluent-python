lax_coordinates = (33.9425, -118.408056)
lattitude, longitude = lax_coordinates # Unpacking

print(lattitude)
print(longitude)


# The os.path.split()  function builds a tuple (path, last_part) from a filesystem path :

import os

_, filename = os.path.split('/Desktop/fluentpy')

print(filename)
