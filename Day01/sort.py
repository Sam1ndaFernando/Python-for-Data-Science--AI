arrSort = ["car", "bike", "van", "bus"]

# Reversed list (reverse modifies the list in place, so print the list after it)
arrSort.reverse()
print("Reversed List: ", arrSort)

# Sorting the list in ascending order
arrSort.sort()
print("Sorted List: ", arrSort)

# Sorting the list case-insensitively
arrSort = ["car", "bike", "van", "bus"]
arrSort.sort(key=str.lower())
print("Case-insensitive Sorted List: ", arrSort)

# Sorting the list in descending order
arrSort.sort(reverse=True)
print("Descending Sorted List: ", arrSort)
