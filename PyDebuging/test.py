firstList = [10, 20, 30, 40, 50]
indexList = [1, 3, 5]

# Check if any value in indexList is a valid index in firstList
if any(item < 0 or item >= len(firstList) for item in indexList):
    print("Some elements in indexList are invalid indices.")
else:
    print("All elements in indexList are valid indices.")
