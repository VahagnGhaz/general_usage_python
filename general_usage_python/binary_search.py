# Iterative implementation
def binary_search_iterative(arr: list, x) -> int:
    """Find given element in given array and return the index if found any, else return -1
    :param arr:
    :param x: element to be find in array
    :return: location of x in given array arr if present, else returns -1
    """

    # Set defualt values
    left = 0
    right = len(arr) - 1


    while left <= right:
        mid = int (left + (right -left)/2)

        # Check if x is present at mid
        if arr[mid] == x:
           return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            left = mid + 1

        # If x is smaller, ignore right half
        else:
            right = mid - 1

    return -1

# Recursive  implementation
def binary_search_recursive(arr: list, left, right, x) -> int:
    """Find given element in given array and return the index if found any, else return -1

    :param arr:
    :param left:
    :param right:
    :param x: element to be find in array
    :return: location of x in given array arr if present, else returns -1
    """

    if(right >= left):
       mid = int(left + (right-left)/2)

       if arr[mid]==x:
           return mid
       elif arr[mid] <x:
           binary_search_recursive(arr, left=mid + 1, right=right, x=x)
       else:
           binary_search_recursive(arr=arr,left=left, right=mid-1, x=x)
    else:
        return -1

def binary_sum_search(arr: list, x: int) -> bool:
    """

    :param arr:
    :param x:
    :return:
    """
    # Set defualt values
    left = 0
    right = len(arr) - 1

    while(left <= right):
        sum = int(left+right)

        if sum == x:
            return True
        elif sum < x:
            binary_search_recursive(arr, left=mid + 1, right=right, x=x)
        else:
            binary_search_recursive(arr=arr, left=left, right=mid - 1, x=x)
    else:
        return -1

# test binary search

if __name__ == "__main__":

    arr = ['name1', 'name2', 'name3']
    name = 'name3'
    res1 = binary_search_iterative(arr=arr, x=name)
    res2 = binary_search_recursive(arr, left=0, right=len(arr)-1, x=name)

    if res1!= -1:
        print("Element is present at index {}".format(res1))
    else:
        print("Element is not present in array")
