def sort(list_to_sort):

    for index in range(1, len(list_to_sort)):
        current_element_index = index
        for sub_index in range(index - 1, -1, -1):
            if list_to_sort[sub_index] < list_to_sort[current_element_index]:
                # it means we must be in a right place, so we could stop the loop
                break
            if list_to_sort[sub_index] > list_to_sort[current_element_index]:
                list_to_sort[sub_index], list_to_sort[current_element_index ] = \
                   list_to_sort[current_element_index], list_to_sort[sub_index]
                current_element_index -= 1
