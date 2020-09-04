def list_to_string(item_list, capital=False, article=True, article_definite=False):
    if len(item_list) == 0:
        raise Exception("No list to arrange.")
    adjusted_list = []
    for item in item_list:
        if article:
            if article_definite:
                adjusted_list.append("the {0}".format(item.name.lower()))
            else:
                if item.name[0] in ["a", "e", "i", "o", "u"]:
                    item = "an " + item.name.lower()
                else:
                    item = "a " + item.name.lower()
                adjusted_list.append(item)
        else:
            adjusted_list.append(item.name)
    output = adjusted_list[0].capitalize() if capital else adjusted_list[0].lower()
    for counter in range(1, len(item_list)-1):
        output += ", {0}".format(adjusted_list[counter].lower())
    if len(item_list) > 1:
        output += " and {0}".format(adjusted_list[-1].lower())
    return output


def check_for_item(item_name, list_to_check):
    for item in list_to_check:
        if item.name is item_name:
            return True

    return False


def calculate_weight(item_list):
    weight = 0
    for item in item_list:
        try:
            weight += item.weight
        except Exception:
            raise Exception("List might not be an item list.")
    return weight
