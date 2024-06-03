import sys
import requests

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap
from ui_main import Ui_WeatherAPI


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_WeatherAPI()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.click_buttion)

    def click_buttion(self):
        self.change_the_city(city=self.ui.lineEdit.text())

    def change_the_city(self, city="Сызрань"):
        '''Функция для изменения показаний при нажатии кнопки Обновить'''

        # используется открытый API от компании OpenWeatherMap v.2.5
        url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + \
            '&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'

        try:
            weather_data = requests.get(url).json()

            temp_real = weather_data['main']['temp']
            temp_feel = weather_data['main']['feels_like']
            wind_speed = weather_data['wind']['speed']
            pressure_gPa = weather_data['main']['pressure']
            # данные даются в гига Паскалях, переводим в привычные мм.рт.ст.
            pressure = pressure_gPa*0.750064

            self.ui.text1.setText(f'Температура в г. {city} {temp_real}°C')
            self.ui.text2.setText(f'По ощущению {temp_feel}°С')
            self.ui.text3.setText(f'Скорость ветра {wind_speed} м/с')
            self.ui.text4.setText(f'Давление {pressure:.0f} мм.рт.ст.')

            icons = {
                'Thunderstorm': "icons/thunderstorm_48dp_FILL0_wght400_GRAD0_opsz48.png",  # гроза
                'Drizzle': "icons/drizzle_rain_icon_216564.png",  # небольшой дождь
                'Rain': "icons/rainy_48dp_FILL0_wght400_GRAD0_opsz48.png",  # сильный дождь
                'Snow': "icons/cloudy_snowing_48dp_FILL0_wght400_GRAD0_opsz48.png",  # снег
                'Mist': "icons/mist_48dp_FILL0_wght400_GRAD0_opsz48.png",  # туман
                'Haze': "icons/foggy_48dp_FILL0_wght400_GRAD0_opsz48.png",  # легкий туман
                'Dust': "icons/sand-dust-dust-mask-icon-with-png-and-vector-format-for-free-723569.png",  # пыль
                'Fog': "icons/foggy_48dp_FILL0_wght400_GRAD0_opsz48.png",  # густой туман
                'Clear': "icons/wb_sunny_48dp_FILL0_wght400_GRAD0_opsz48.png",  # чисто
                'Clouds': "icons/cloud_48dp_FILL0_wght400_GRAD0_opsz48.png",  # облачно
            }
            icon = icons.get(weather_data['weather'][0]['main'],
                             'icons/wb_sunny_48dp_FILL0_wght400_GRAD0_opsz48.png')
            self.ui.picture.setPixmap(QPixmap(icon))
        except:
            self.ui.text1.setText(f'Ошибка в написании города')
            self.ui.text2.setText(f' ')
            self.ui.text3.setText(f' ')
            self.ui.text4.setText(f' ')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
