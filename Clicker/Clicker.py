import mouse
import keyboard
import time

def auto_clicker(click_interval):
    print("Автокликер запущен! Нажми 'Esc' для остановки.")
    while True:
        if keyboard.is_pressed('esc'):
            print("Автокликер остановлен.")
            break
        mouse.click()
        time.sleep(click_interval)

if __name__ == "__main__":
    interval = float(input("Введите интервал между кликами (в секундах): "))
    print("Вставьте курсор в нужное место...")
    time.sleep(5)  # Время на подготовку
    auto_clicker(interval)
