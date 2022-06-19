def sort(list_to_sort):
    sort_logic(list_to_sort, 0, len(list_to_sort))

def sort_logic(list_to_sort, start_index, size):

    if not list_to_sort or size < 2:
        return
    if size == 2:
        if list_to_sort[start_index] > list_to_sort[start_index + 1]:
            list_to_sort[start_index], list_to_sort[start_index + 1] = \
                list_to_sort[start_index + 1], list_to_sort[start_index]
        return
    
    sort_logic_for_normal_list(list_to_sort, start_index, size)


def sort_logic_for_normal_list(list_to_sort, start_index, size):
    pivot = list_to_sort[start_index]
    left_pointer = start_index + 1
    right_pointer = start_index + size - 1

    while left_pointer <= right_pointer:
        if list_to_sort[left_pointer] > list_to_sort[right_pointer]:
            list_to_sort[left_pointer], list_to_sort[right_pointer] = \
                list_to_sort[right_pointer], list_to_sort[left_pointer]
        if list_to_sort[left_pointer] <= pivot:
            left_pointer += 1
        if list_to_sort[right_pointer] >= pivot:
            right_pointer -= 1
    
    list_to_sort[start_index], list_to_sort[right_pointer] = \
        list_to_sort[right_pointer], list_to_sort[start_index]
    
    sort_logic(list_to_sort, start_index, right_pointer - start_index)
    sort_logic(list_to_sort, left_pointer, size - left_pointer)