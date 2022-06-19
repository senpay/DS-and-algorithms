def merge(first_sorted_list, second_sorted_list):
    if not first_sorted_list and not second_sorted_list:
        return []
    if not second_sorted_list:
        return first_sorted_list
    if not first_sorted_list:
        return second_sorted_list

    first_pointer = 0
    second_pointer = 0

    resulting_list = []

    while True:
        if (first_pointer < len(first_sorted_list) and
            (second_pointer >= len(second_sorted_list) or
             first_sorted_list[first_pointer] <= second_sorted_list[second_pointer])):
            resulting_list.append(first_sorted_list[first_pointer])
            first_pointer += 1
        elif (second_pointer < len(second_sorted_list)):
            resulting_list.append(second_sorted_list[second_pointer])
            second_pointer += 1
        else:
            break
    return resulting_list

