import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
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
        ("\nTak nak Pusing,Tak nak Tanya", 0.08),
        ("Aku kuat tanpa drama", 0.09),
        ("Aku dah lupa tak ingat lagi", 0.09),
        ("Nama kau pun hilang dari hati", 0.08),
        ("Aku Move on, hidup sendiri", 0.08),
        ("Takperlukau,aku happy\n", 0.07),
        ("Aku dah lupa tak ingat lagi", 0.08),
        ("Nama kau pun hilang dari hati", 0.09),
        ("Aku Move on, hidup sendiri", 0.08),
        ("Takperlukau,aku happy", 0.08),
        (".................................................", 0.20),
    ]

    # Delay untuk masing-masing baris lirik, jumlah harus sama dengan lyrics
    delay = [0.1, 0.1, 0.1, 0.1, 0.2, 0.3, 0.1, 0.1, 0.1, 0.1, 0.1,]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delay[i], speed))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
