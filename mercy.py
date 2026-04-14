import time

class TrafficLightController:
    def __init__(self):
        self.state = "NS_GREEN"

    def display(self):
        if self.state == "NS_GREEN":
            print("\nNorth-South: GREEN | East-West: RED")
        elif self.state == "NS_YELLOW":
            print("\nNorth-South: YELLOW | East-West: RED")
        elif self.state == "EW_GREEN":
            print("\nNorth-South: RED | East-West: GREEN")
        elif self.state == "EW_YELLOW":
            print("\nNorth-South: RED | East-West: YELLOW")

    def next_state(self):
        if self.state == "NS_GREEN":
            self.state = "NS_YELLOW"
        elif self.state == "NS_YELLOW":
            self.state = "EW_GREEN"
        elif self.state == "EW_GREEN":
            self.state = "EW_YELLOW"
        elif self.state == "EW_YELLOW":
            self.state = "NS_GREEN"

    def run(self):
        while True:
            self.display()

            if "GREEN" in self.state:
                time.sleep(5)
            else:
                time.sleep(2)

            self.next_state()


if __name__ == "__main__":
    controller = TrafficLightController()
    controller.run()