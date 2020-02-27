# a tuple of 5 floating-point numbers
stats = (48.0, 30.5, 20.2, 100.0, 48.0)
# a tuple of 6 strings
herbs = ("lavender", "pokeroot", "chamomile", "valerian", "nettles", "oatstraw")
# a tuple that stores the data for a movie
movie = ("Monty Python and the Holy Grail", 1975, 9.99)

print("stats: ", stats)
print(stats[0])
print(stats[0:3])
a, b, c = movie
print("a, b, c: ", a, b, c)

def get_location():
    nums = (1, 2, 3)
    x, y, z = nums
    return x, y, z

x, y, z = get_location()
print("get location: ", x, y, z)