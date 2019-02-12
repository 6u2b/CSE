class Phone(object)
    def__init__(self):
    # These are attribute that a phone has.
    # These should all be relevant to our program
    self.screen = True
    self.camera = 2
    self.microphone = True
    self.carrier = carrier
    self.battery_left = charge_left

    def charge(self time):
        self.battery_left += time
        if self.battery_left > 100:
            self.battery_left = 100

    def make_call(self, duration):
        if not self.screen:
            print("You can't maek a phone call.")
            print("Your screen is broken.")
            return
        battery_loss_per_minute = 5
        self.battery_left <= 0:
            print("Your phone dies during the conversation")
        elif self.battery_left == 0:
    