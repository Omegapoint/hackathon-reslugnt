from departureboard import DepartureBoard
from config import Config
from machine import Timer, Pin, I2C
import ssd1306
import boot

p0 = Pin(0, Pin.OUT)    # create output pin on GPIO0
p0.off()                 # set pin to "off" (low) level
p0.on()

i2c = I2C(-1, scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

board = DepartureBoard(Config.trafiklab_departure_board_api, Config.trafiklab_stop_id, Config.trafiklab_stop_id_direction, 3)

def printDepartureLine(line, data):
    name = data["Departure"][line]["Product"]["name"]
    number = data["Departure"][line]["Product"]["num"]
    time = data["Departure"][line]["Stops"]["Stop"][0]["depTime"]
    print(name + " " + time)
    oled.text(number + " " + time, 0, line*10)

def updateDisplay():
    oled.fill(0)
    if not boot.sta_if.isconnected():
        print("Not connected to wifi")
        oled.text("Not connected to wifi", 0, 0)
        oled.show
        return
    data = board.get_data()
    if not "Departure" in data:
        print("No results found")
        oled.text("No results found", 0, 0)
        oled.show
        return
    departures = len(data["Departure"])
    print("Departures found: " + str(departures))
    for departure in range(departures):
        printDepartureLine(departure, data)
    oled.show()

updateDisplay()
tim = Timer(-1)
tim.init(period=60000, mode=Timer.PERIODIC, callback=lambda t:updateDisplay())


