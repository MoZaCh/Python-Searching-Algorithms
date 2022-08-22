
def linear_search(arr, value):
    """
    Searches through a list for a specific element (sequentially)
    :param arr: The array to be searched
    :param value: Integer the value to be searched for
    :return: A boolean value True or False depending on whether the element exists in the list
    """
    found = False  # Boolean flag default as false

    if len(arr) == 0:
        return found

    for i in arr:
        if i == value:
            found = True
            break

    return found


def print_list(arr):

    for i in range(len(arr)-1):
        print(arr[i])
    return True


def copy_range_of_list(start, end, arr):
    newList = []

    for i in range(start, end, 1):
        newList.append(arr[i])
    return newList


def binary_search(arr, value):

    if len(arr) == 1:
        if arr[0] == value:
            return True
        else:
            return False
    else:
        mid = len(arr)//2  # Length of list divided by 2 to get the middle value
        temp = []

        if arr[mid] > value:
            temp = copy_range_of_list(0, mid, arr)
            return binary_search(temp, value)
        elif arr[mid] < value:
            temp = copy_range_of_list(mid, len(arr), arr)
            return binary_search(temp, value)
        else:
            return True


if __name__ == '__main__':

    listA = [1, 2, 4, 7, 8, 6]
    listB = [10]
    listC = []
    listD = [1, 2]
    #print(linear_search(listA, 7))
    #print(linear_search(listA, 10))
    #print(linear_search(listB, 10))
    #print(linear_search(listC, 4))
    print(binary_search(listD, 10))

