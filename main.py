from pyowm import OWM
from datetime import date
from application.db.people import get_employees
from application.salary import calculate_salary
from config import token


def get_temperature(city, token):
    """
    Функция, возвращающая погодные условия конкретного города
    """
    owm = OWM(token)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    w = observation.weather
    detail = w.detailed_status
    wind = w.wind()
    hum = w.humidity
    temp = w.temperature('celsius')
    return f"Погодные условия в Донецке:\n {temp},\n {detail},\n {wind},\n {hum}"


def main():
    print('Текущая дата: ', date.today().strftime("%d/%m/%Y"))
    print(get_employees())
    print(calculate_salary())


print('Helloo world!')

if __name__ == '__main__':
    print(get_temperature('Donetsk,UA', token))
    main()