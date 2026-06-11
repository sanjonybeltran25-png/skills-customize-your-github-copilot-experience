def add(a: float, b: float) -> float:
    return a + b


def safe_divide(a: float, b: float) -> float:
    # TODO: update this function to handle division by zero cleanly
    return a / b


def format_full_name(first_name: str, last_name: str) -> str:
    return f"{first_name.strip().title()} {last_name.strip().title()}"


if __name__ == "__main__":
    print(add(2, 3))
    print(safe_divide(10, 2))
    print(format_full_name("jane", "doe"))
