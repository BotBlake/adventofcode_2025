import logging
logging.basicConfig(level=logging.INFO)

class Dial:
    """
    A class representing a circular dial with positions from 0 to 99.
    """

    def __init__(self, logger: logging.Logger):
        self.pointer = 50  # The dial starts by pointing at 50.
        self.logger = logger
        self.zero_stops = 0
        self.zero_passed = 0
    
    def move(self, direction: str, amount: int) -> None:
        """
        Move the dial pointer according to the direction and amount.
        Keeps the pointer within 0-99.
        """
        pointer = self.pointer

        while amount > 0: # Handle one step at a time
            if direction == "R":
                pointer += 1
            elif direction == "L":
                pointer -= 1

            # Keep the dial pointer within 0-99
            if pointer >= 100:
                pointer = 0
            elif pointer < 0:
                pointer = 99

            if pointer == 0:
                self.zero_passed += 1
                self.logger.debug(f"Dial has passed zero. Total count: {self.zero_passed} times.")

            amount -= 1

        if pointer == 0:
            self.zero_stops += 1
            self.logger.debug(f"Dial has pointed to zero. Total count: {self.zero_stops} times.")

        self.pointer = pointer
        self.logger.debug(f"Dial moved {direction}{amount}, now at {self.pointer}")

    def get_zero_passed(self) -> int:
        """
        Return the number of times the dial has pointed to zero.
        """
        return self.zero_passed
    
    def get_zero_stopped(self) -> int:
        """
        Return the number of times the dial has stopped at zero.
        """
        return self.zero_stops
    
    def get_pointer(self) -> int:
        """
        Return the current position of the dial pointer.
        """
        return self.pointer

def main() -> None:
    logger = logging.getLogger("day_01")
    dial = Dial(logger)

    with open("days/01/puzzle_input.txt") as f:
        for line in f:
            direction = line[0]
            amount = int(line[1:].strip())
            dial.move(direction, amount)
    
    print("-"*10 + "SOLUTION DAY 01" + "-"*10)
    print(f"Part1: Dialed stopped at zero {dial.get_zero_stopped()} times.")
    print(f"Part2: Dial passed zero {dial.get_zero_passed()} times.")
    print("-"*35)
    return None

if __name__ == "__main__":
    raise RuntimeError("Please run this script through main.py")
