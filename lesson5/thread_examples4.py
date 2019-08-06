from threading import Thread
import random


def file_writer(filename, num_of_lines):
    with open(filename, 'w') as f:
        for l in range(num_of_lines):
            f.write((str(random.randint(0, 5000)) + '\n'))


list_of_threads = []

for i in range(10):
    t = Thread(target=file_writer,
               args=(str(random.randint(0, 1000)) + '.txt',
                     random.randint(0, 1000)))

    list_of_threads.append(t)
    t.start()

print(list_of_threads)
