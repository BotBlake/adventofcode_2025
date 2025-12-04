def remove_accessible_rolls(paper_map) -> tuple[int, list[list[str]]]:
    """
    Removes all rolls that are currently accessible.
    Returns the number of rolls removed in this step.
    """
    # Create mutable grid
    grid = [list(row) for row in paper_map]

    height = len(grid)
    width = len(grid[0])

    adjacent_offsets = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0),  (1, 1)
    ]

    rolls_to_remove = []

    # Find accessible rolls
    for row in range(height):
        for col in range(width):
            if grid[row][col] != '@':
                continue

            adjacent_rolls = 0

            for d_row, d_col in adjacent_offsets:
                n_row = row + d_row
                n_col = col + d_col

                if 0 <= n_row < height and 0 <= n_col < width:
                    if grid[n_row][n_col] == '@':
                        adjacent_rolls += 1

            if adjacent_rolls < 4:
                rolls_to_remove.append((row, col))

    # Remove them
    for r, c in rolls_to_remove:
        grid[r][c] = '.'

    return len(rolls_to_remove), grid



def remove_all_rolls(paper_map) -> int:
    """
    Repeatedly removes accessible rolls until no more can be removed.
    """

    # Create mutable grid
    grid = [list(row) for row in paper_map]

    total_removed = 0

    # LOOP until remove_accessible_rolls returns 0
    while True:
        removed_this_round, grid = remove_accessible_rolls(grid)
        if removed_this_round == 0:
            break   # nothing more to remove

        total_removed += removed_this_round

    return total_removed


def main():
    with open("days/04/puzzle_input.txt") as f:
        paper_roll_grid = [line.strip() for line in f]
    print("-" * 10 + " SOLUTION DAY 04 " + "-" * 10)
    removable_rolls, grid_removed = remove_accessible_rolls(paper_roll_grid)
    print(f"Part 1: Accessible removable Paper Rolls: {removable_rolls}")
    print(f"Part 2: All removable Paper Rolls:  {remove_all_rolls(paper_roll_grid)}")
    print("-" * 35)
