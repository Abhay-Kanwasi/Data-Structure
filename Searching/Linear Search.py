import array as arr

elements = arr.array('i', [2,3,4,6])

key = 6

for i in range(len(elements)):
    if elements[i] == key:
        print("Element found at index", i)
    else:
        continue

