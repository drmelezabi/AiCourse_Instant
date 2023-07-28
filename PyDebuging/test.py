def removeOccurrencesElements(string, number):
    # check input type
    if not isinstance(string, (str)):
        return 'wrong input Type'

    # Find the first non-repeated character
    stringList = string.split()

    uniqueList = [x for x in stringList if x != str(number)]

    if(uniqueList):
        return " ".join(uniqueList)
    else:
        return 'no repeated chars'


print(removeOccurrencesElements('1 1 2 3 4 5 1 2 1', 1))
