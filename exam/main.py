def filter_and_sort_positive(numbers):
    """
    Приймає список чисел, повертає відсортований список лише з додатніх значень.
    """
    positives = [num for num in numbers if num > 0]
    return sorted(positives)


if __name__ == "__main__":
    sample_list = [1, -5, 2, 0, 6, 8, 3]
    result = filter_and_sort_positive(sample_list)
    print("Результат:", result)
