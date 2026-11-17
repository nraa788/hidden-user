
import os
import sys
import time
import random

# WARNA
R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
B = "\033[94m"
M = "\033[95m"
C = "\033[96m"
W = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"

def ketik(teks, delay=0.04):
    for huruf in teks:
        sys.stdout.write(huruf)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading(teks):
    for i in range(0, 101, 5):
        sys.stdout.write(
            f"\r{G}{teks} {i}%{RESET}"
        )
        sys.stdout.flush()
        time.sleep(0.4)
    print()

# PEMBUKA
os.system("clear")

print(C + "=" * 38)
print(BOLD + R + "       SYSTEM SECURITY CENTER")
print(C + "=" * 38 + RESET)

time.sleep(1)

input(Y + "\n[!] Tekan ENTER untuk memulai scan..." + RESET)

os.system("clear")

ketik(G + "[+] Menghubungkan ke sistem..." + RESET)
time.sleep(2)

loading("[+] Scanning perangkat")

print()
ketik(C + "[+] Menganalisis data..." + RESET)
time.sleep(3)

ketik(R + "\n[!] AKTIVITAS MENCURIGAKAN TERDETEKSI!" + RESET)
time.sleep(3)

ketik(Y + "\nHP SUDAH DI RETAS!" + RESET)
time.sleep(3)

ketik(M + "\nCoba lihat pojok kiri..." + RESET)

# JEDA PRANK
time.sleep(10)

# JUMPSCARE
os.system("clear")
time.sleep(0.5)

print("\n" * 2)

print(M + BOLD + r"""
██╗  ██╗██╗██╗  ██╗██╗   ██╗
██║  ██║██║██║  ██║██║   ██║
███████║██║███████║██║   ██║
██╔══██║██║██╔══██║██║   ██║
██║  ██║██║██║  ██║╚██████╔╝
╚═╝  ╚═╝╚═╝╚═╝  ╚═╝ ╚═════╝
""" + RESET)

print("\n")

print(R + BOLD + r"""
██╗  ██╗██╗██╗  ██╗██╗   ██╗
██║  ██║██║██║  ██║██║   ██║
███████║██║███████║██║   ██║
██╔══██║██║██╔══██║██║   ██║
██║  ██║██║██║  ██║╚██████╔╝
╚═╝  ╚═╝╚═╝╚═╝  ╚═╝ ╚═════╝
""" + RESET)

print("\n")

ketik(R + BOLD + "       H I H U ! ! !" + RESET, 0.12)

time.sleep(0.5)

# BUNGA BERMUNCULAN
flowers = ["🌸", "🌺", "🌷", "🌼", "💮", "🌻", "🌹"]

for i in range(8):
    baris = "  ".join(
        random.choice(flowers) for _ in range(7)
    )
    print(M + BOLD + baris + RESET)
    time.sleep(0.3)

print("\n")

ketik(Y + BOLD + "    WKWKWKWK 😭💗" + RESET)
ketik(G + "     PRANK !" + RESET)
ketik(C + "    SORRY YAKK❤️" + RESET)

print("\n" + M + "       🌸 HAVE A NICE DAY 🌸" + RESET)
