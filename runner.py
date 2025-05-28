from core.detection import color, text, object
from core import datetime

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

if __name__ == "__main__":
    while True:
        key = input("key: ")
        if key == "exit":
            exit()

        select_mode(int(key))
