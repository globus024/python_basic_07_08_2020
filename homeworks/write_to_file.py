# Azamat Khankhodjaev
# 24.09.2020

def write_file(path: str, text: str) -> bool:
    '''
    This program is intended for writing to a data file
    :param path: str. Full path to the file
    :param text: str.
    :return: return True on successful recording else return False
    '''
    try:
        with open(path, 'w', encoding='UTF-8') as file:
            file.write(text)
        return True
    except:

        file.close()
        return False
