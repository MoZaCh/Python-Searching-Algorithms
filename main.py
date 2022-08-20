
def linear_search(arr, value):
    found = False

    for i in arr:
        if i == value:
            found = True
            break

    return found


if __name__ == '__main__':
    print("This is a test!")
