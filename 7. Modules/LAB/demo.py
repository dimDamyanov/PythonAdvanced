from termcolor import colored
from pyfiglet import figlet_format

text = colored('Hello World!', 'red', attrs=['bold', 'underline'])
print(text)

text = figlet_format('Python', font='isometric1')
print(text)
