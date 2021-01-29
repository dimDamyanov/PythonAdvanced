import os

directory_path = '.'
files_list = [f for f in os.listdir(directory_path) if os.path.isfile(f)]
files = {}
for file in files_list:
    if (extension := file[file.rfind('.'):]) not in files:
        files[extension] = []
    files[extension].append(file)

for key in files:
    files[key] = sorted(files[key])
files = sorted(files.items(), key=lambda x: x[0])
file_path = os.path.join(os.path.normpath(os.path.expanduser("~/Desktop")), 'report.txt')
report_file = open(file_path, 'w')
for extension, files in files:
    print(extension, file=report_file)
    for file in files:
        print(f'- - - {file}', file=report_file)
