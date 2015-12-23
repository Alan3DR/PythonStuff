from BreakfastSerial import Arduino, RGBLed
from time import sleep

board = Arduino()
led = RGBLed(board, { "red": 6, "green": 5, "blue": 3 })

led.red()
sleep(1)

led.green()
sleep(1)

led.blue()
sleep(1)

led.yellow()
sleep(1)

led.cyan()
sleep(1)

led.purple()
sleep(1)

led.white()
sleep(1)

led.off()