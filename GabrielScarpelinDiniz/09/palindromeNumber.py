def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    string = str(x)
    length = len(string)

    reverse = ""
    for i in range(length - 1, -1, -1):
        reverse = reverse + string[i]

    print(f"Reverse: {reverse} | String {string}")
    return reverse == string

isPalindrome(121)
