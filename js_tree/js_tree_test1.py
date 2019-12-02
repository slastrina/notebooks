# use in python3

import os
import pprint
import json
from jinja2 import Environment
from jinja2 import FileSystemLoader

### Consts
SCAN_DIRECTORY = [('jupyter', '../')]
TOOL_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

### Tree Structure Generator
exclusion_list = [
    '.ipynb_checkpoints',
    '.DS_Store',
    '#recycle',
    '.git',
    '.idea',
    '.gitignore'
]

def build_tree(dir):

    temp = []

    all_directory = [x for x in os.listdir(dir) if x not in exclusion_list]
    dirs = [x for x in all_directory if os.path.isdir(os.path.join(dir, x))]
    files = [x for x in all_directory if os.path.isfile(os.path.join(dir, x))]
    
    for dir_name in dirs:
        temp.append({"text": dir_name, 
                     'icon': 'jstree-folder', 
                     "children" : build_tree(os.path.join(dir, dir_name))})
    for file_name in files:
        temp.append({"text": file_name, 
                     'icon': 'jstree-file'})
        
    return(temp)

### JINJA2 Template Code
for scan in SCAN_DIRECTORY:

    directory_tree = build_tree(scan[1])

    j2_env = Environment(loader=FileSystemLoader(os.path.join(TOOL_DIRECTORY, 'templates')), trim_blocks=True)

    template = j2_env.get_template('index.html.j2')

    rendered_template = template.render(data=directory_tree)

    with open('./{}.html'.format(scan[0]), 'w') as f:
        f.write('{}'.format(rendered_template))
    
    with open('./{}.json'.format(scan[0]), 'w') as f:
        json.dump(directory_tree, f, sort_keys=True, indent=4, default=str)
        
print('done')