def sort(width, height, length, mass):
    """
    Determines the appropriate stack for a package based on its dimensions and mass.

    Parameters:
    - width (float): Width of the package in centimeters.
    - height (float): Height of the package in centimeters.
    - length (float): Length of the package in centimeters.
    - mass (float): Mass of the package in kilograms.

    Returns:
    - str: The name of the stack ('STANDARD', 'SPECIAL', or 'REJECTED').
    """
    # Calculate volume
    volume = width * height * length

    # Determine if the package is bulky
    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150

    # Determine if the package is heavy
    is_heavy = mass >= 20

    # Determine the appropriate stack using a ternary operator
    return "REJECTED" if is_bulky and is_heavy else ("SPECIAL" if is_bulky or is_heavy else "STANDARD")


if __name__ == "__main__":
    # Example usage
    examples = [
        {"width": 100, "height": 100, "length": 100, "mass": 10},  # STANDARD
        {"width": 160, "height": 100, "length": 100, "mass": 10},  # SPECIAL (bulky)
        {"width": 100, "height": 100, "length": 100, "mass": 25},  # SPECIAL (heavy)
        {"width": 160, "height": 100, "length": 100, "mass": 25},  # REJECTED (bulky and heavy)
    ]

    for idx, pkg in enumerate(examples, 1):
        stack = sort(pkg["width"], pkg["height"], pkg["length"], pkg["mass"])
        print(f"Example {idx}: Stack = {stack}")
