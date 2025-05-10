from core.detection import color, text, object
from core import datetime
from core.speech import speak
from pynput.keyboard import Key, Listener

CURRENT_MENU_SELECTED = 0

OPTIONS = [
    "Color Detection",
    "Text Detection",
    "Object Detection",
    "Current Time",
    "Current Date",
]


def select_mode(option):
    match option:
        case 0:
            return color.detect()
        case 1:
            return text.detect()
        case 2:
            return object.detect()
        case 3:
            return datetime.current_time()
        case 4:
            return datetime.current_date()
        case _:
            return color.detect()


def show_menu():
    for i, option in enumerate(OPTIONS):
        if i == CURRENT_MENU_SELECTED:
            print(f"-> {option}")
        else:
            print(f"   {option}")


def on_press(key):
    global CURRENT_MENU_SELECTED

    try:
        if key == Key.up:
            CURRENT_MENU_SELECTED = (CURRENT_MENU_SELECTED - 1) % len(OPTIONS)
            speak(OPTIONS[CURRENT_MENU_SELECTED])
            # show_menu()

        elif key == Key.down:
            CURRENT_MENU_SELECTED = (CURRENT_MENU_SELECTED - 1) % len(OPTIONS)
            speak(OPTIONS[CURRENT_MENU_SELECTED])
            # show_menu()

        elif key == Key.right:
            select_mode(CURRENT_MENU_SELECTED)

    except AttributeError:
        pass


if __name__ == "__main__":
    speak(OPTIONS[CURRENT_MENU_SELECTED])
    with Listener(on_press=on_press) as listener:
        listener.join()
