import logging
logging.basicConfig(level=logging.INFO)


def largest_subsequence_number(digits, k) -> list[int]:
    """
    Select exactly k digits from 'digits' (list of ints) in order
    to form the largest possible number.
    """
    stack = []
    to_remove = len(digits) - k  # digits to discard

    for d in digits:
        # Pop while current digit is better AND there are still digits to remove
        while stack and to_remove > 0 and stack[-1] < d:
            stack.pop()
            to_remove -= 1
        stack.append(d)

    # Trim to k if too long
    return stack[:k]


def max_joltage_k_digits(bank_str, k) -> int:
    digits = [int(ch) for ch in bank_str.strip()]
    chosen = largest_subsequence_number(digits, k)
    # convert list of digits back to integer
    return int("".join(str(d) for d in chosen))


def main() -> None:
    logger = logging.getLogger("day_03")

    total_2 = 0 
    total_12 = 0

    with open("days/03/puzzle_input.txt") as f:
        for line in f:
            line = line.strip()

            best2 = max_joltage_k_digits(line, 2)
            best12 = max_joltage_k_digits(line, 12)

            logger.debug(f"Bank: {line}")
            logger.debug(f"Best 2-digit joltage:  {best2}")
            logger.debug(f"Best 12-digit joltage: {best12}")

            total_2 += best2
            total_12 += best12

    print("-" * 10 + " SOLUTION DAY 03 " + "-" * 10)
    print(f"Part 1: (2 digits):   {total_2}")
    print(f"Part 2: (12 digits):  {total_12}")
    print("-" * 35)

    return None


if __name__ == "__main__":
    raise RuntimeError("Please run this script through main.py")
