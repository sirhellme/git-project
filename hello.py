# People growth equation
# P(t) = P0 * e^(r * t)
# where:
#   P0 = initial population
#   r  = growth rate per year (as a decimal)
#   t  = time in years

import math


def population_growth(initial_population, growth_rate, years):
    """Return projected population after a number of years."""
    return initial_population * math.exp(growth_rate * years)


if __name__ == "__main__":
    p0 = 1000
    r = 0.03
    t = 10
    final_population = population_growth(p0, r, t)

    print(f"Initial population: {p0}")
    print(f"Growth rate: {r * 100:.2f}% per year")
    print(f"Years: {t}")
    print(f"Projected population: {final_population:.2f}")
