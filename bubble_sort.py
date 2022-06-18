def sort(list_to_sort):
    # checks if there were any swaps during the run through list
    swapped = True
    while swapped:
        swapped = False
        runs = 0
        for i in range(len(list_to_sort) - 1 - runs):
            if list_to_sort[i] > list_to_sort[i + 1]:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
                swapped = True
        runs += 1
