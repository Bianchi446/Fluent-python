# Which list is more readable?

# V1

symbols = '#$%^&'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)


# V2


symbols = '@#$%&'
codes1 = [ord(symbol) for symbol in symbols]

print(codes1)


                                                                # The same list but using map / filter

symbols2 = '$¢£¥€¤'

beyond_ascii = [ord(s) for s in symbols2 if ord(s) > 127]

print(beyond_ascii)


# v2

beyond_ascii2 = list(filter(lambda c : c > 127, map(ord, symbols2)))

print(beyond_ascii2)


