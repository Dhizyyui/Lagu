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
        ("Jangan Lah kau tinggalkan diriku ", 0.1),
        ("Tak kan mampu menghadapi semua ", 0.12),
        ("Hanya Bersama mu ku akan bisa ", 0.11),
        ("Kau Adalah Darahku ", 0.10),
        ("Kau Adalah jantungku ", 0.10),
        ("Kau adalah hidupku lengkapi diriku ", 0.10),
        ("Oh Sayang kau begituuu ", 0.1),
        ("Sempurnaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 0.1),
    ]
    delays = [0.3, 4.5, 9.3, 14.1, 18.8, 23.0, 28.0, 34.5 ]

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