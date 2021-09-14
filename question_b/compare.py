def main():
    def compare():
        str1 = "1.1"
        str2 = "1.2"

        list1 = list(str1)
        list2 = list(str2)

        common_len = min(len(list1), len(list2))

        # Loop for common_len times and whenever the strings
        # don't match return greater/smaller accordingly.
        for i in range(common_len):
            if list1[i] > list2[i]:
                return f"{str1} is greater than {str2}"
            elif list1[i] < list2[i]:
                return f"{str1} is smaller than {str2}"

        # The two strings are equal so far and if they're of the 
        # same length, then they must be equal to each other
        if len(list1) == len(list2):
            return f"{str1} is equal to {str2}"

        # The first string is greater if the length is greater
        elif len(list1) > len(list2):
            return f"{str1} is greater than {str2}"

        # The second string is greater if the length is greater
        else:
            return f"{str1} is smaller than {str2}"
    print(compare())

if __name__ == "__main__":
    main()