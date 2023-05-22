import time
import Bwork_voice
now_start = "Запустить сейчас"
x = 0 
for i in range(1):
    Bwork_voice.speek_text("Ожидаем сигнала")
    time.sleep(3)
    if x >= 1:
        Bwork_voice.speek_text(now_start)
    x = x + 1
