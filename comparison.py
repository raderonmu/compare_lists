""" This file is part of the File I/O exercise.

It should be used with the two input files, fruits_1.txt and fruits_2.txt."""

def open_and_read_file(filename):
    """Opens file as a file object and returns list of contents."""

    # Write your code below.
    file_list = open(filename)
    file_list_read = file_list.read()

    file_list_read = file_list_read.strip()
    file_contents = file_list_read.split("\n")

    return file_contents 

    pass


def compare(lst1, lst2):
    """Takes in two lists and returns a list of items in common. """

    # Write your code below.

    common_item_list = []

    #creating the common list
    for item in lst1:
        if item in lst2:
            common_item_list.append(item)

    #printing result of common list
    if len(common_item_list) != 0:
        string = ", "
        join_string = string.join(common_item_list[0:-1])

        print "These lists have " + join_string + " and " + common_item_list[-1] + " in common."
    else:
        print "These lists have no fruits in common."

    return common_item_list
    pass


# Call your functions at the bottom, after they've been defined.

fruits1 = open_and_read_file("fruits_1.txt")
fruits2 = open_and_read_file("fruits_2.txt")
fruits_empty = []

print compare(fruits1, fruits2)
print compare(fruits1, fruits_empty)