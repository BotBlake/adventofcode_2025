import datetime
import importlib
import sys


def get_today_day() -> int:
    """Return AoC day number based on today's date."""
    today = datetime.date.today()
    if today.month != 12:
        raise ValueError("It is not December; please specify a day explicitly.")
    return today.day


def load_and_run(day: int) -> None:
    """Load days/XX/main.py and run its main() function."""
    day_str = f"{day:02d}"
    module_path = f"days.{day_str}.main"

    try:
        mod = importlib.import_module(module_path)
    except ModuleNotFoundError:
        print(f"ERROR: No module found for day {day_str} at {module_path}")
        sys.exit(1)

    if not hasattr(mod, "main"):
        print(f"ERROR: {module_path} has no function main()")
        sys.exit(1)

    mod.main()


def main():
    # Allow passing day manually
    if len(sys.argv) > 1:
        try:
            day = int(sys.argv[1])
        except ValueError:
            print("Usage: python main.py [day]")
            sys.exit(1)
    else:
        day = get_today_day()

    print(f"Running Advent of Code 2025 Day {day:02d}")
    load_and_run(day)


if __name__ == "__main__":
    main()