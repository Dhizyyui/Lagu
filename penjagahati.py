import time
from threading import Thread
import sys

def animate_text(text, delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("Biarkan aku menjaga perasaan ini ", 0.1),
        ("Menjaga segenap cinta yang telah kau beri ", 0.10),
        ("Engkau Pergi, aku takkan pergi ", 0.10),
        ("Kau menjauh , aku takkan jauh ", 0.09),
        ("Sebenarnya diriku masih mengharapkanmuuuuuuuuuuuuuuuuuuuuuuu ", 0.07),
    ]
    delays = [ 0.2, 6.2, 13.2, 17.2, 20.4 ]

    threads = []
    for i in range(len(lyrics)):

        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()