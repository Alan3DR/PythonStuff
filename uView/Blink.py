from BreakfastSerial import Arduino, Led
from time import sleep

#board = Arduino("/dev/cu.usbserial-DA01GEHQ")
board = Arduino()
pin = 3
led = Led(board, pin)

print("Im going to Blink...")
sleep(1)
led.blink(500)
print("Blinking!")
sleep(10)

#led.on()
#sleep(1)
led.off()
print("Turnign off")


