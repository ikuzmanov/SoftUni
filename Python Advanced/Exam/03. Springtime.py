def start_spring(**kwargs):
    my_dict = {}
    output = ""

    for key, value in kwargs.items():
        if value not in my_dict:
            my_dict[value] = [key]
        else:
            my_dict[value].append(key)

    for key, value in sorted(my_dict.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0])):
        output += f'{key}:\n'
        for el in sorted(value):
            output += f'-{el}\n'
    return output

example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
