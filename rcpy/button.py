import rcpy
import rcpy.gpio as gpio

import threading
import time

DEBOUNCE = 3
PRESSED = gpio.LOW
RELEASED = gpio.HIGH
    
class ButtonEvent(gpio.InputEvent):

    PRESSED = gpio.InputEvent.LOW
    RELEASED = gpio.InputEvent.HIGH

class Button(gpio.Input):

    def is_pressed(self, debounce = DEBOUNCE):
        return self.is_low(debounce)

    def is_released(self, debounce = DEBOUNCE):
        return self.is_high(debounce)
    
    def pressed_or_released(self, debounce = DEBOUNCE):
        return self.high_or_low(debounce)
                    
    def pressed(self, debounce = DEBOUNCE):
        return self.low(debounce)

    def released(self, debounce = DEBOUNCE):
        return self.high(debounce)
        
# definitions

# BUTTONs
pause = Button(gpio.PAUSE_BTN)
mode = Button(gpio.MODE_BTN)
