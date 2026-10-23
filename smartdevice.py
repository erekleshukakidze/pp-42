class SmartDeveice:
    def __init__(self, brand):
        self.brand = brand
        self.__is_on = False

    def turn_on(self):
        self.__is_on = True
        print(f"The {self.brand} device has been turned on. ")


    def turn_off(self):
        self.__is_on = False
        print(f"The {self.brand} device has been turned off.")

    def get_status(self):
        return self.__is_on

class SmartLight(SmartDeveice):
    def __init__(self, brand, brightness=45):
        super().__init__(brand)
        self.brightness = brightness

    def turn_on(self):
        super().turn_on
        print(f"SmartLight Brand: {self.brand}, Brightness{self.brightness}%")

my_light = SmartLight(brand="Apple", brightness=70)
my_light.turn_on
print(f"Device status (is on): {my_light.get_status()}")