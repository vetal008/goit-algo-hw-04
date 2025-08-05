from pathlib import Path

def get_cats_info(path: Path) -> dict or None:
    """
    Main Function which make all the calculations
    :param path:
    :return: list of data about cats or None obj
    """
    try:
        row_num = 0
        cats_info = list()
        with open(path, 'r', encoding='utf-8') as cat_file:
            for line in cat_file:
                row_num += 1
                # here in one lane we transform line from file into dict object
                # with using: map, lambda, zip, split, strip
                cat_dict = dict(zip(('id', 'name', 'age'), map(lambda x: x.strip(), line.split(','))))
                # check for valid data in rows
                if len(cat_dict) == 3:
                    cats_info.append(cat_dict)
                else:
                    print(f'Check file data in row {row_num}')
        return cats_info
    except FileNotFoundError:
        print('File not found')
        return None

if __name__ == '__main__':  # Start script
    cat_path = Path('cat_data.txt')
    try:
        print(*get_cats_info(cat_path), sep='\n')
    except TypeError:
        pass