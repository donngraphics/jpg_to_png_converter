import sys
import os
from PIL import Image

# name = sys.argv[1]

directory = sys.argv[1]
new_directory = sys.argv[2]
parent_dir = 'C:'
path = os.path.join(parent_dir, new_directory)


isdir = os.path.isdir(new_directory)
print(isdir)

while True:
    try:
        if isdir == False:
            os.mkdir(new_directory)
            print('The new folder {} has been created!'.format(new_directory))
            break
        else:
            print('Folder already exist.')
            # sys.exit('Terminating the Script.')
            break
    except OSError as error:
        print(error)


for filename in os.listdir(directory):
    path2 = os.path.join(parent_dir, directory, filename)
    save_file_path = os.path.join(parent_dir, new_directory, filename[:-4])
    if filename.endswith('.jpg'):
        imgs = Image.open(path2)
        imgs.save(save_file_path + '.png', 'png')
        print(filename)
        print(imgs.mode)


print('Here are your inputs: {}, {}'.format(directory, new_directory))


# print('The name of this program is:', sys.argv[0])
# print("Argument List:", str(sys.argv))
# print(os.name)
# print(os.getcwd())
# print(os.listdir('.'))

# Grab first and second argument x
# check if \new exist, it not create x
# loop through Pokedex
# Convert images to png
# save to new foloder
