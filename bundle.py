#!/usr/bin/env python

import os, glob, yaml, zipfile

# Append yaml dependences in yaml_file ('import' files) to another yaml file (full_yaml_file)
def addDependencies(file_list, filename):
    # print 'Checking for dependencies on:', os.path.normpath(filename)
    file_list.append(os.path.normpath(filename))
    folder = os.path.dirname(filename)
    yaml_file = yaml.safe_load(open(filename))

    # Search for fonts or textures urls
    if 'fonts' in yaml_file:
        for font in yaml_file['fonts']:
            if 'url' in yaml_file['fonts'][font]:
                file_list.append(os.path.normpath(folder + '/' + yaml_file['fonts'][font]['url']))

    if 'textures' in yaml_file:
        for font in yaml_file['textures']:
            if 'url' in yaml_file['textures'][font]:
                file_list.append(os.path.normpath(folder + '/' + yaml_file['textures'][font]['url']))

    # Search for inner dependemcies
    if 'import' in yaml_file:
        if (type(yaml_file['import']) is str):
            addDependencies(file_list, folder + '/' + yaml_file['import'])
        else:
            for file in yaml_file['import']:
                addDependencies(file_list, folder + '/' + file)

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

# # ================================== Main functions
main_scene_file = './tron.yaml'

all_dependencies = [] 
addDependencies(all_dependencies, main_scene_file)
files = list(set(all_dependencies))

print files, len(files)

zipf = zipfile.ZipFile('tron.zip', 'w', zipfile.ZIP_DEFLATED)
for file in files:
    zipf.write(file)
zipf.close()