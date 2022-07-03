def sort(list_to_sort):
    sorted_elements = 0
    while sorted_elements < len(list_to_sort):
        for i in range(sorted_elements, len(list_to_sort)):
            if list_to_sort[i] < list_to_sort[sorted_elements]:
                list_to_sort[sorted_elements], list_to_sort[i] = list_to_sort[i], list_to_sort[sorted_elements]
        sorted_elements += 1
