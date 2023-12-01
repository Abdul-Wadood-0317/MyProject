import threading
import time

from concurrent.futures import ThreadPoolExecutor

#Indicates some task being done
def func (seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds
def main():
    time1 = time.perf_counter()
    func(4)
    func(2)
    func(1)

    #Smae code using thread
    #code bro code,Talk is cheap,show me code ,coding is other type of magic!,h
