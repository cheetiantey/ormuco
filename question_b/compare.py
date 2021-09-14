def compare(str1, str2):
    list1 = list(str1)
    list2 = list(str2)

    common_len = min(len(list1), len(list2))

    # Loop for common_len times and whenever the strings
    # don't match return greater/smaller accordingly.
    for i in range(common_len):
        if list1[i] > list2[i]:
            return "Greater"
        elif list1[i] < list2[i]:
            return "Smaller"

    # The two strings are equal so far and if they're of the 
    # same length, then they must be equal to each other
    if len(list1) == len(list2):
        return "Equal"

    # The first string is greater if the length is greater
    elif len(list1) > len(list2):
        return "Greater"

    # The second string is greater if the length is greater
    else:
        return "Smaller"

