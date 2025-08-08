import sys
from pathlib import Path
from colorama import Fore, Style, Back


def get_directory_iteration(path: Path, tabs=0):
    """
    Main Function which print structure on the screen
    :param path: path of your folder
    :param tabs: iteration and count of tabs
    :return: return nothing but print structure
    """
    try:
        print(Fore.RED + '_' * tabs, str(path).split('\\')[-1], '\\' + Style.RESET_ALL, sep='')
        tabs = tabs + 1
        iter_dir = list(path.iterdir())
        if len(iter_dir) == 0: # if folder is empty
            print(Fore.BLACK + Back.WHITE + '   Folder is empty' + Style.RESET_ALL)
        else:
            for item in iter_dir:
                if item.is_dir(): # for next iteration in child directory
                    get_directory_iteration(item, tabs)
                else: # for any other files in folder
                    print(Fore.BLUE + '_' * tabs, str(item).split('\\')[-1] + Style.RESET_ALL)
    # Exceptions if folder is not exists or it`s a file
    except FileNotFoundError:
        print('No such file or directory')
    except NotADirectoryError:
        print('Not a directory')

if __name__ == '__main__':
    dir_path = Path(sys.argv[1])
    get_directory_iteration(dir_path)