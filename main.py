import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33,
    board.IO34,
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
while True:
    volume = microphone.value
    for x in leds:
        x.value = 0;
    

    print(volume)
    num_lights = len(leds)
    
    if volume < 5000:
        leds[0].value = 1;
        leds[1].value = 0;
        leds[2].value = 0;
        leds[3].value = 0;
        leds[4].value = 0;
        leds[5].value = 0;
        leds[6].value = 0;
        leds[7].value = 0;
        leds[8].value = 0;
        leds[9].value = 0;
        leds[10].value = 0;
    
    elif volume < 10000:
        leds[0].value = 1;
        leds[1].value = 1;
        leds[2].value = 0;
        leds[3].value = 0;
        leds[4].value = 0;
        leds[5].value = 0;
        leds[6].value = 0;
        leds[7].value = 0;
        leds[8].value = 0;
        leds[9].value = 0;
        leds[10].value = 0;
    
    elif volume < 15000:
        leds[0].value = 1;
        leds[1].value = 1;
        leds[2].value = 1;
        leds[3].value = 0;
        leds[4].value = 0;
        leds[5].value = 0;
        leds[6].value = 0;
        leds[7].value = 0;
        leds[8].value = 0;
        leds[9].value = 0;
        leds[10].value = 0;
    
    elif volume < 20000:
        leds[0].value = 1;
        leds[1].value = 1;
        leds[2].value = 1;
        leds[3].value = 1;
        leds[4].value = 0;
        leds[5].value = 0;
        leds[6].value = 0;
        leds[7].value = 0;
        leds[8].value = 0;
        leds[9].value = 0;
        leds[10].value = 0;
    
    elif volume < 25000:
        leds[0].value = 1;
        leds[1].value = 1;
        leds[2].value = 1;
        leds[3].value = 1;
        leds[4].value = 1;
        leds[5].value = 0;
        leds[6].value = 0;
        leds[7].value = 0;
        leds[8].value = 0;
        leds[9].value = 0;
        leds[10].value = 0;
    
    elif volume < 30000:
        leds[0].value = 1;
        leds[1].value = 1;
        leds[2].value = 1;
        leds[3].value = 1;
        leds[4].value = 1;
        leds[5].value = 1;
        leds[6].value = 0;
        leds[7].value = 0;
        leds[8].value = 0;
        leds[9].value = 0;
        leds[10].value = 0;
    
    elif volume < 35000:
        leds[0].value = 1;
        leds[1].value = 1;
        leds[2].value = 1;
        leds[3].value = 1;
        leds[4].value = 1;
        leds[5].value = 1;
        leds[6].value = 1;
        leds[7].value = 0;
        leds[8].value = 0;
        leds[9].value = 0;
        leds[10].value = 0;
        
    
    elif volume < 40000:
        leds[0].value = 1;
        leds[1].value = 1;
        leds[2].value = 1;
        leds[3].value = 1;
        leds[4].value = 1;
        leds[5].value = 1;
        leds[6].value = 1;
        leds[7].value = 1;
        leds[8].value = 0;
        leds[9].value = 0;
        leds[10].value = 0;
    
    elif volume < 45000:
        leds[0].value = 1;
        leds[1].value = 1;
        leds[2].value = 1;
        leds[3].value = 1;
        leds[4].value = 1;
        leds[5].value = 1;
        leds[6].value = 1;
        leds[7].value = 1;
        leds[8].value = 1;
        leds[9].value = 0;
        leds[10].value = 0;
    
    elif volume < 50000:
        leds[0].value = 1;
        leds[1].value = 1;
        leds[2].value = 1;
        leds[3].value = 1;
        leds[4].value = 1;
        leds[5].value = 1;
        leds[6].value = 1;
        leds[7].value = 1;
        leds[8].value = 1;
        leds[9].value = 1;
        leds[10].value = 0;
    
    else :
        leds[0].value = 1;
        leds[1].value = 0;
        leds[2].value = 1;
        leds[3].value = 1;
        leds[4].value = 1;
        leds[5].value = 1;
        leds[6].value = 1;
        leds[7].value = 1;
        leds[8].value = 1;
        leds[9].value = 1;
        leds[10].value = 0;



    sleep(0.05)

    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?
