from os import listdir, path


def traverse_dir(current_path):
    for element in listdir(current_path):
        if path.isdir(path.join(current_path, element)):
            traverse_dir(path.join(current_path,element))
        else:
            extension = element.split('.')[-1]
            if extension not in files_by_ext:
                files_by_ext[extension] = []
            files_by_ext[extension].append(element)


files_by_ext = {}
traverse_dir('.')

for extension, files in sorted(files_by_ext.items()):
    print(f'.{extension}')
    for file in sorted(files):
        print(f'--- {file}')