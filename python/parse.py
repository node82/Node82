#isinstance('key', int)
#isinstance('key', str)

def parse_lists(items):
            str_list_items = []
            num_list_items = []
            for i in items:
                        if isinstance(i, float) or isinstance(i, int):
                                    num_list_items.append(i)
                        elif: isinstance(i, str):
                                    str_items.append(i)
                        else:
                                    pass
           return str_list_items, num_list_items

print(parse_lists(items))
