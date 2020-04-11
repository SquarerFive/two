dirnames_to_include = [
    'AnimStarterPack',
    'Megascans',
    'ThirdParty'
    ]

import os

dirs = os.listdir(".")
ignore = []
for dir_ in dirs:
    if '.' not in dir_:
        if dir_ not in dirnames_to_include:
            print(dir_)
            ignore.append(dir_+"/")

with open('.gitignore', 'w+') as f:
    f.write('\n'.join(ignore))
