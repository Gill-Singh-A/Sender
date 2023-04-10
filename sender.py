import keyboard, sys, time

if __name__ == "__main__":
    time.sleep(int(sys.argv[2]))
    for i in range(int(sys.argv[1])):
        keyboard.press_and_release('ctrl+v')
        keyboard.press_and_release('enter')
        time.sleep(int(sys.argv[3]))