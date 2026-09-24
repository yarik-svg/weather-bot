import requests
import pyttsx3

engine = pyttsx3.init()

# Получаем все доступные голоса
voices = engine.getProperty('voices')

def list_voices():
    """Выводит список голосов с индексами и языком"""
    print("\nДоступные голоса:")
    for i, voice in enumerate(voices):
        # Пытаемся определить язык по languages; если пусто — пишем «неизвестен»
        lang_info = ", ".join(voice.languages) if voice.languages else "неизвестен"
        print(f"{i}: {voice.name} (язык: {lang_info})")
    print()

def select_voice():
    """Запрашивает у пользователя выбор голоса по индексу"""
    list_voices()
    while True:
        try:
            choice = input("Введите номер голоса для озвучки (число): ").strip()
            idx = int(choice)
            if 0 <= idx < len(voices):
                engine.setProperty('voice', voices[idx].id)
                print(f"Выбран голос: {voices[idx].name}")
                break
            else:
                print("Такой номер отсутствует. Попробуйте ещё раз.")
        except ValueError:
            print("Пожалуйста, введите целое число.")

# Настраиваем скорость и громкость
engine.setProperty('rate', 122)
engine.setProperty('volume', 0.9)

def get_weather(city: str) -> str:
    base_url = f"https://wttr.in/{city}?format=%C+%t"
    try:
        response = requests.get(base_url, timeout=10)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return "Не удалось получить данные о погоде. Попробуйте позже."
    except requests.RequestException:
        return "Ошибка соединения. Проверьте интернет и попробуйте позже."

def speak(text: str):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    # Сначала выбираем голос
    if len(voices) > 0:
        select_voice()
    else:
        print("В системе нет доступных голосов для синтеза речи.")

    city = input("Введите название города: ")
    weather_info = get_weather(city)
    print(weather_info)
    speak(weather_info)
