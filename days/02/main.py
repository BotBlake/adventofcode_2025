import logging
logging.basicConfig(level=logging.DEBUG)

class RangeAnalyzer:
    """
    A Class to analyze ranges defined by start and end points for invalid IDs.
    """
    def __init__(self, logger: logging.Logger):
        self.logger = logger
        self.simple_invalid_id_sum = 0
        self.complicated_invalid_id_sum = 0

    def is_simply_invalid(self, id: int) -> bool:
        """
        Check if the given ID is made only of some sequence of digits repeated twice.
        """
        id_str = str(id)
        length = len(id_str)
        if length % 2 != 0:
            return False
        half = length // 2
        if id_str[:half] == id_str[half:]:
            return True
        return False

    def is_complicated_invalid(self, id: int) -> bool:
        """
        Check if the given ID is made only of some sequence of digits repeated multiple times.
        Works by itterating through each Character and checks if it has been seen in sequence before.
        """
        id_str = str(id)
        
        s = id_str
        n = len(s)

        # Try every possible repeating block length
        for size in range(1, n // 2 + 1):
            if n % size == 0:
                block = s[:size]
                if block * (n // size) == s:
                    return True
        return False


    def analyze_range(self, start: int, end: int) -> None:
        for id in range(start, end + 1):
            if self.is_simply_invalid(id):
                self.simple_invalid_id_sum += id
                self.logger.debug(f"Found simple invalid ID: {id}")
            if self.is_complicated_invalid(id):
                self.complicated_invalid_id_sum += id
                self.logger.debug(f"Found complicated invalid ID: {id}")

    def get_simple_invalid_id_count(self) -> int:
        return self.simple_invalid_id_sum
    
    def get_complicated_invalid_id_sum(self) -> int:
        return self.complicated_invalid_id_sum

def main() -> None:
    logger = logging.getLogger("day_01")
    analyzer = RangeAnalyzer(logger)

    with open("days/02/puzzle_input.txt") as f:
        ranges = f.read().split(",")
        for range in ranges:
            start_str, end_str = range.split("-")
            start, end = int(start_str), int(end_str)
            analyzer.analyze_range(start, end)
    
    print("-"*10 + "SOLUTION DAY 02" + "-"*10)
    print(f"Part1: Easy invalid ID sum {analyzer.get_simple_invalid_id_count()}.")
    print(f"Part2: All invalid ID sum {analyzer.get_complicated_invalid_id_sum()}.")
    print("-"*35)
    return None

if __name__ == "__main__":
    raise RuntimeError("Please run this script through main.py")