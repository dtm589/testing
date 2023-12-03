'''
Complete the exponential_growth function. Given the initial followers count n, growth factor factor, and number of days days, return a list containing the exponential growth of followers for each day, up to and including the target day.

For example:

- Initial followers: 10
- Growth factor: 2
- Days: 4

Growth sequence: [10, 20, 40, 80, 160]
'''

def exponential_growth(n, factor, days):
    growth_sequence = []
    growth_sequence.append(n)
    growth = n
    for i in range(days):
        growth = growth * factor
        growth_sequence.append(growth)
    return growth_sequence