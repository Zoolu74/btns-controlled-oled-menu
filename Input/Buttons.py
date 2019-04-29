from RPi import GPIO


class Buttons:

    def __init__(self, btn_left, btn_ok, btn_right, menu=None):
        self.btn_left = btn_left
        self.btn_ok = btn_ok
        self.btn_right = btn_right
        self.btn_timer = None
        self.menu = None
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.btn_left, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.btn_ok, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.btn_right, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        if menu is not None:
            self.set_menu(menu)

    def set_menu(self, menu):
        self.menu = menu
        GPIO.add_event_detect(self.btn_left, GPIO.RISING, callback=self.__turnLeft, bouncetime=50)
        GPIO.add_event_detect(self.btn_right, GPIO.RISING, callback=self.__turnRight, bouncetime=50)
        GPIO.add_event_detect(self.btn_ok, GPIO.RISING, callback=self.__pressOK, bouncetime=50)

    def __turnLeft(self, channel):
        self.menu.change_highlight(-1)
        self.menu.render()
        self.btn_timer = None

    def __turnRight(self, channel):
        self.menu.change_highlight(1)
        self.menu.render()
        self.btn_timer = None

    def __pressOK(self, channel):
        self.btn_timer = None
