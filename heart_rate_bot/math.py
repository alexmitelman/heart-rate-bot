from decimal import Decimal
from typing import Tuple

# https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/exercise-intensity/art-20046887


def calculate_heart_rate(
    age: int, reasting_heart_rate: int
) -> Tuple[Decimal, Decimal]:
    max_heart_rate = 220 - age
    hrr = max_heart_rate - reasting_heart_rate
    target_low = Decimal(hrr * 0.7 + reasting_heart_rate)
    target_high = Decimal(hrr * 0.85 + reasting_heart_rate)
    return target_low, target_high
