def sort_dictonary_by_value(dictonary):
    sorted_dictonary = {}
    keys = []
    next = 0

    for key in dictonary:
        keys += [key]

    current = keys[0]

    for i in range(len(keys)):
        for index in range(1, len(keys)):
            next = keys[index]

            if dictonary[current] < dictonary[next]:
                current = next

        sorted_dictonary[current] = dictonary[current]
        keys.remove(current)
        if len(keys):
            current = keys[0]

    return sorted_dictonary
