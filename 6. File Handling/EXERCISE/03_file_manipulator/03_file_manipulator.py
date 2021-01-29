import os


def create_file(file_name):
    with open(f'{file_name}', 'w'):
        pass


def add_file(file_name, content):
    with open(f'{file_name}', 'a') as file:
        file.writelines(content+'\n')


def replace_file(file_name, old_string, new_string):
    try:
        with open(f'{file_name}', 'r+') as file:
            text = ''.join(file.readlines())
            replaced_content = text.replace(old_string, new_string)
            file.seek(0)
            file.truncate()
            file.writelines(replaced_content)
    except FileNotFoundError:
        print('An error occurred')


def delete_file(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print('An error occurred')


mapper = {
    'Create': create_file,
    'Add': add_file,
    'Replace': replace_file,
    'Delete': delete_file,
}


while True:
    command = input()
    if command == 'End':
        break
    else:
        command_data = command.split('-')
        mapper[command_data[0]](*command_data[1:])
