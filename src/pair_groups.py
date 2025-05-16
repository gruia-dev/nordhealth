from collections import defaultdict
from typing import Dict, List, Tuple


def group_pairs_by_sum(numbers: List[int]) -> Dict[int, List[Tuple[int, int]]]:
    """
    Groups all unique pairs from the list of numbers by their sum.

    Args:
        numbers (List[int]): List of integers to analyze.

    Returns:
        Dict[int, List[Tuple[int, int]]]: A dictionary where each key is a sum,
            and the value is a list of all pairs (as tuples) that produce this sum.

    Raises:
        ValueError: If the list contains fewer than 2 elements.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements.")

    sum_to_pairs: Dict[int, List[Tuple[int, int]]] = defaultdict(list)

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            total = numbers[i] + numbers[j]
            sum_to_pairs[total].append((numbers[i], numbers[j]))

    return {k: v for k, v in sum_to_pairs.items() if len(v) > 1}


def print_grouped_pairs(numbers: List[int]) -> None:
    """
    Prints all groups of pairs with equal sums.

    Args:
        numbers (List[int]): List of integers.
    """
    try:
        grouped = group_pairs_by_sum(numbers)
        for s in sorted(grouped):
            formatted = " ".join(f"( {a}, {b})" for a, b in grouped[s])
            print(f"Pairs : {formatted} have sum : {s}")
    except ValueError as e:
        print(f"Error: {e}")


def main() -> None:
    dataset_1 = [6, 4, 12, 10, 22, 54, 32, 42, 21, 11]
    dataset_2 = [4, 23, 65, 67, 24, 12, 86]

    print_grouped_pairs(dataset_1)
    print("-" * 30)
    print_grouped_pairs(dataset_2)


if __name__ == "__main__":
    main()
