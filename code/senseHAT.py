from sense_emu import SenseHat
from currentweather import getWeather

def display(self):
    sense_hat_emulator = SenseHat()
    condition, temp, min_temp, max_temp, pressure, humidity, wind = getWeather('paris')
    message = (f'PARIS: Temperature: {max_temp}, humidity: {humidity}, wind: {wind}')
    sense_hat_emulator.show_message(message)
if __name__ == "__main__":
    display()