#!/usr/bin/env python

import os, glob, yaml, zipfile

# Append yaml dependences in yaml_file ('import' files) to another yaml file (full_yaml_file)
def addDependencies(style_files, filename):
    # print "Append all dependences of " + filename
    style_files.append(os.path.normpath(filename))
    folder = os.path.dirname(filename)
    yaml_file = yaml.safe_load(open(filename))

    if 'import' in yaml_file:
        
        if (type(yaml_file['import']) is str):
            addDependencies(style_files, folder + '/' + yaml_file['import'])
        else:
            for file in yaml_file['import']:
                addDependencies(style_files, folder + '/' + file)

def zip(files, dst):
    zf = zipfile.ZipFile("%s.zip" % (dst), "w", zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(src)
    for dirname, subdirs, files in os.walk(src):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            print 'zipping %s as %s' % (os.path.join(dirname, filename),
                                        arcname)
            zf.write(absname, arcname)
    zf.close()

# ================================== Main functions

# Folders to compress
folders = ['components', 'layers']

# Styles to programatically add
style_folder = 'styles'


# GET all the style dependencies
style_dependecies = []
for filename in glob.glob(style_folder+'/*.yaml'):
    addDependencies(style_dependecies, filename)

files  = list(set(style_dependecies))
# print files, len(files)

for folder in folders:
    for dirname, subdirs, files in os.walk(folder):
        for filename in files:
            absname = os.path.normpath(os.path.join(dirname, filename))
            print absname
            
            # print dirname, subdirs, files
#             files.append(absname)

print files, len(files)