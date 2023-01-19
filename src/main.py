from vk import script
from concurrent.futures import ThreadPoolExecutor

if __name__ == '__main__':
    with ThreadPoolExecutor(3) as executor:
        executor.submit(script.run)
