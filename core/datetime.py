from datetime import datetime
from core.speech import speak


def current_time():
    current_time = datetime.now().strftime("%-I %-M %p")
    speak(f"Current time: {current_time}")


def current_date():
    today_date = datetime.now().strftime("%d %b , %Y")
    speak(f"Today's date:  {today_date}")


if __name__ == "__main__":
    current_time()
