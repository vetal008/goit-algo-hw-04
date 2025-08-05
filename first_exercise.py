from pathlib import Path


def total_salary(path: Path) -> (float, float) or (None, None):
    """
    Main function which calculates the total salary
    and average salary from a given file.

    :param path:
    :return: (number, number) or (None, None) in case of mistakes
    """
    try:  # Mistakes check
        with open(path, 'r', encoding='utf-8') as salary_file:  # file open
            lines_list = salary_file.readlines()
            new_list = list()
            for line in lines_list:
                new_list.append(float(line.split(',')[1]))
        suma = sum(new_list)
        middle_value = suma / len(new_list)
        # If we have whole number func will return 'int'
        # Else return 'float'
        if suma % 1 == 0:
            suma = int(suma)
        if middle_value % 1 == 0:
            middle_value = int(middle_value)
        return suma, middle_value
        #  Main mistakes
    except FileNotFoundError:
        print('File not found')
        return None, None
    except ValueError:
        print('Value error')
        return None, None
    except ZeroDivisionError:
        print('Division error')
        return None, None

if __name__ == '__main__':  # Start script
    first_exercise = Path('month_salary.txt')
    total, average = total_salary(first_exercise)
    print('Total sum of month salary is {}, average salary is {}'.format(total, average))
