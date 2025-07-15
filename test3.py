import os

dir_path = r'/Users/zanaprimc/Desktop/bergfex-uvp-projektna/smucisca_html'
count = 0
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
print('File count:', count)
