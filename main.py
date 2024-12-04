from src.utils import *

try:
    from colorama import Fore, Style
except:
    from os import system
    system("pip install colorama --break")
    from colorama import Fore, Style

config = load_config('../config.json')
path = config['apps_path']


files = [parse_info(file.path) for file in iterate_dir(path)]
print(f'Detected desktop files: {len(files)}\n'
      f'{Fore.GREEN}Green - displayed\n{Fore.RED}Red - undisplayed\n')

for file in files:
    print(f'{Fore.GREEN if file.get_display() else Fore.RED}{file.get_name()} ({file.get_path()})')

action = input(f'{Style.RESET_ALL}Actions\n1. Edit manualy entries\n>> ')

if action == '1':
    filter = input(f'Show undisplayed entries?\n({Fore.GREEN}y{Style.RESET_ALL}'
                   f'/{Fore.RED}n{Style.RESET_ALL}) >> ') == 'y'

    for file in files:
        display = file.get_display()

        if not filter:
            if not display:
                continue

        while True:
            action = input(f'{Fore.GREEN if display else Fore.RED}{file.get_name()} ({file.get_path()})\n'
                           f'{Style.RESET_ALL}'
                           f'1. Mark as displayed\n'
                           f'2. Mark as undisplayed\n'
                           f'>> ')
            if action == '1':
                file.set_display('false')
                break
            elif action == '2':
                file.set_display('true')
                break
            else:
                print('Choose a valid action')
else:
    print('Choose right action')
