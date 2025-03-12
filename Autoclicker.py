import pyautogui
import time

# Fördröjning innan programmet startar (så du hinner byta fönster)
time.sleep(5)

print("Autoclicker startad! Tryck CTRL+C för att stoppa.")

try:
    while True:
        pyautogui.click()  # Klickar på musen
        time.sleep(0.1)  # Väntar 0.1 sek mellan klick (ändra om du vill snabbare/långsammare)
except KeyboardInterrupt:
    print("\nAutoclicker stoppad!")
