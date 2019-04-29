from RPi import GPIO


class Buttons:

    def __init__(self, btn_left, btn_ok, btn_right, menu=None):
        self.btn_left = btn_left
        self.btn_ok = btn_ok
        self.btn_right = btn_right
        self.menu = None
        self.btn_left_LastState = None
        self.btn_ok_LastState = None
        self.btn_right_LastState = None
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.btn_left, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.btn_ok, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.btn_right, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        if menu is not None:
            self.set_menu(menu)

    def set_menu(self, menu):
        self.menu = menu
        GPIO.add_event_detect(self.btn_left, GPIO.RISING, callback=self.__changePage, bouncetime=200)
        GPIO.add_event_detect(self.btn_right, GPIO.RISING, callback=self.__changePage, bouncetime=200)
        GPIO.add_event_detect(self.btn_ok, GPIO.RISING, callback=self.__pressOK, bouncetime=200)
        self.btn_left_LastState = GPIO.input(self.btn_left)
        self.btn_ok_LastState = GPIO.input(self.btn_ok)
        self.btn_right_LastState = GPIO.input(self.btn_right)

    def __changePage(self, channel):
        btn_left_state = GPIO.input(self.btn_left)
        btn_right_state = GPIO.input(self.btn_right)
        if btn_left_state != self.btn_left_LastState:
            self.menu.change_highlight(-1)
        if btn_right_state != self.btn_right_LastState:
            self.menu.change_highlight(1)
        self.menu.render()

    def __pressOK(self, channel):
        print('Button OK pushed on GPIO{}'.format(channel))
