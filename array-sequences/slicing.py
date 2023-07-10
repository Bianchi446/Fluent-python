# A commonn feature of list, tupple and dict is the support of slicing operations 


# Why slices and Ranges exclude the last item ?

# It’s easy to compute the length of a slice or range when start and stop are given
# It’s easy to split a sequence in two parts at any index x, without overlapping


# Slice Objects 

# The notation s[a:b:c] can be used to specify a stride(step) c.

# Example : To evaluate the expresion seq[star:stop:step] Python call the special method seq.__getitem__(slice(start, stop, step)) 


# Example 2 : You need to parse a flat-like data like 'invoice', name the slices.

invoice = """
... 0.....6.................................40........52...55........
...  1909 Pimoroni PiBrella                      $17.50  3   $52.50
...  1489 6mm Tactile Switch x20                 $4.95   2   $9.90
...  1510 Panavise Jr. - PV-201                  $28.00  1   $28.00
...  1601 PiTFT Mini Kit 320x240                 $34.95  1   $34.95
... """

SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
for item in line_items: 
    print(item[UNIT_PRICE], item[DESCRIPTION])


