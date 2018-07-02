def list_to_string(item_list, capital=False):
    if len(item_list) == 0:
        raise Exception("No list to arrange.")
    if capital:
        working_string = "A {0}".format(item_list[0].name)
    else:
        working_string = "a {0}".format(item_list[0].lower())
    if len(item_list) >= 2:
        for i in item_list[1:len(item_list) - 1]:
            working_string += ", a {0}".format(i.name)
        working_string += " and a {0}".format(item_list[len(item_list)-1].name)
    return working_string


def check_for_item(item_name, list_to_check):
    for item in list_to_check:
        if str(item) is item_name:
            return True

    return False
