def manipulate_list():
    # Create an empty list
    my_list = []

    # Append elements to the list
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)

    print("List after appending elements:", my_list)

    # Insert the value 15 at the second position
    my_list.insert(1, 15)

    print("List after inserting 15:", my_list)

    # Extend the list with another list
    my_list.extend([50, 60, 70])

    print("List after extending:", my_list)

    # Remove the last element from the list
    my_list.pop()

    print("List after removing the last element:", my_list)

    # Sort the list in ascending order
    my_list.sort()

    print("List after sorting:", my_list)

    # Find and print the index of the value 30
    try:
        index_of_30 = my_list.index(30)
        print("Index of 30:", index_of_30)
    except ValueError:
        print("30 is not found in the list.")

# Execute the function
manipulate_list()
