first_string = input(" Enter the first String : \n ")
second_string = input(" Enter the second String : \n ")


def check_if_two_strings_are_anagrams_of_each_other(first_string_, second_string_):
    second_string_listed = list(second_string_.upper())
    first_string_list = list(first_string_.upper())
    common_count = {}
    for m in first_string_list:
        common_count[m] = 0
    letter_in_common = []
    for x in first_string_list:
        if x in second_string_listed:
            common_count[m] = common_count[m] + 1
            letter_in_common.append(x)
    if letter_in_common == []:
        print("No letter in common ! ")
    else:
        for po in list(common_count):
            if common_count[po] == 0:
                del common_count[po]
        print(f"Letter common times : {common_count}")
        for qu in letter_in_common:
            print(f"Letter in common : {qu.lower()}")

check_if_two_strings_are_anagrams_of_each_other(
    first_string_=first_string, second_string_=second_string
)

#
