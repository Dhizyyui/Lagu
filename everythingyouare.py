import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.08):
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
        ("\n""menantang dunia", 0.08),
        ("Merayakan muda tuk satu jam saja", 0.1),
        ("Kita hampir mati dan kau selamatkan aku", 0.09),
        ("Dan ku menyelamatkanmu dan sekarang aku tahu", 0.11),
        ("\n""Cerita kita tak jauh berbeda", 0.25),  # lebih lambat biar sesuai
        ("Got beat down by the world sometimes I wanna fold", 0.1),
        ("Namun suratmu kan ku ceritakan ke anak-anakku nanti\n", 0.1),
        
    ]

    
    delays = [
        0.5,    # menantang dunia
        3.5,    # Merayakan muda tuk satu jam saja
        7.5,    # Kita hampir mati ...
        12.0,   # Dan ku menyelamatkanmu ...
        19.8,   # Cerita kita tak jauh berbeda (lebih panjang)
        26.4,   # Got beat down ...
        29.5,   # Namun suratmu ...
    ]

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
