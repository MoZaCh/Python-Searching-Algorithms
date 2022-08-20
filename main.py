
def linear_search(arr, value):
    """
    Searches through a list for a specific element (sequentially).
    :param arr: The array to be searched.
    :param value: Integer the value to be searched for.
    :return: A boolean value True or False depending on whether the element exists in the list.
    """
    found = False # Boolean flag default as false

    for i in arr:
        if i == value:
            found = True
            break

    return found


if __name__ == '__main__':

    listA = [1, 2, 4, 7, 8, 6]
    print(linear_search(listA, 7))
    print(linear_search(listA, 10))
