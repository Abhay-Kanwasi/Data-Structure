import array as arr

elements = arr.array('i', [2,3,4,6])

key = int(input("Enter the key :"))
def linear_search(key):
    for i in range(len(elements)):
        if elements[i] == key:
            return f"Element found at index", {i}
    return "Element not found"

print(linear_search(key))
