def list_to_string(item_list, capital=False):
    if len(item_list) == 0:
        raise Exception("No list to arrange.")
    if capital:
        working_string = item_list[0].name.capitalize()
    else:
        working_string = item_list[0].lower()
    if len(item_list) >= 2:
        for i in item_list[1:len(item_list) - 1]:
            working_string += ", {0}".format(i.name)
        working_string += " and {0}".format(item_list[len(item_list)-1].name)
    return working_string
