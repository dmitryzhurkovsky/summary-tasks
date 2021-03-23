"""Task1"""
import time


def count_time(name_decorator_function):

    def wrapper_func(func):
        def wrapper(*args):
            start = time.time()
            result = func(*args)
            end = time.time() - start
            print(f"Lead time {name_decorator_function} is {end}")
            return result
        return wrapper
    return wrapper_func


# O(log(n))
@count_time('find_index')
def find_index(in_data):
    low = 0
    high = len(in_data)

    while low <= high:
        mid = int((low + high) / 2)
        guess = int(in_data[mid])
        try:
            guess_next = int(in_data[mid + 1])
        except IndexError:
            return None
        if guess == 1 and guess_next == 0:
            return mid
        if guess == 0:
            high = mid - 1
        else:
            low = mid + 1
    return None


# O(n)
@count_time('find_index_python_method')
def find_index_python_method(in_data):
    try:
        result = in_data.index('0')
    except ValueError:
        return None
    if result == 0:
        return None
    return result - 1


"""Task2"""
import requests
from bs4 import BeautifulSoup


def parcing_page(alphabet='russian'):
    """It gets list of animals from Wikipedia. Alphabet parameter allows selecting display language."""
    if alphabet == 'english':
        a = ord('A')
        literals = [chr(a) for a in range(a, a + 26)]
    else:
        a = ord('А')
        literals = [chr(a) for a in range(a, a + 32)]
    for literal in literals:
        href = f'https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&from={literal}'
        r = requests.get(href)
        soup = BeautifulSoup(r.text, 'lxml')
        containers = soup.find_all('div', {'class': 'mw-category-group'})
        for count, tag in enumerate(containers, start=0):
            if tag.h3.string == f'{literal}':
                contain = containers[count]
                result = contain.find_all("a")
        print(f'{literal}: {len(result)}')
        result.clear()
