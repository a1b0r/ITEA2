from threading import Thread
import random
import time


def random_generator(num, thread_name):
    for i in range(num):
        time.sleep(random.randint(0, 5))
        print(f"I'm executing from {thread_name}")
    print(f"The end of {thread_name}")


thread1 = Thread(target=random_generator, args=(5, "thread1"))
thread2 = Thread(target=random_generator, args=(5, "thread2"))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

random_generator(5, "main_thread")
