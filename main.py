
def linear_search(arr, value):
    """
    Searches through a list for a specific element (sequentially).
    :param arr: The array to be searched.
    :param value: The value to be searched for.
    :return: A boolean value True or False depending on whether the element exists in the list.
    """
    found = False

    for i in arr:
        if i == value:
            found = True
            break

    return found


if __name__ == '__main__':
    print("This is a test!")
