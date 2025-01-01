# FDE Technical Screen

## Objective

Develop a function for Thoughtful’s robotic automation factory that dispatches packages to the correct stack based on their volume and mass.

## Rules

### Classification Criteria

- **Bulky**:
  - Volume (Width x Height x Length) ≥ 1,000,000 cm³
  - **OR** any dimension (Width, Height, Length) ≥ 150 cm

- **Heavy**:
  - Mass ≥ 20 kg

### Dispatch Stacks

- **STANDARD**:
  - Packages that are **not** bulky **and** **not** heavy

- **SPECIAL**:
  - Packages that are **either** bulky **or** heavy

- **REJECTED**:
  - Packages that are **both** bulky **and** heavy

## Implementation

### Function Signature

```python
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
