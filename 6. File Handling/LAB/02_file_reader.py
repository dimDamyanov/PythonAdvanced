with open('../File Handling Resources/File Reader/numbers.txt') as file:
    print(sum([int(el.strip()) for el in file.readlines()]))