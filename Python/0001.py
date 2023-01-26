"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import numpy as np

array = np.array(range(1, 1000))

multiples_of_three_predicate = array % 3 == 0
multiples_of_five_predicate = array % 5 == 0

multiples_of_three = array[multiples_of_three_predicate]
multiples_of_five = array[multiples_of_five_predicate]

combined_arrays = np.concatenate((multiples_of_three, multiples_of_five))
unique_values = np.unique(combined_arrays)

sum_of_values = sum(unique_values)
print(sum_of_values)
