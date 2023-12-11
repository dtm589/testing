'''
TSP IN NP
Even though it takes factorial time to solve TSP, TSP is in NP because we can verify a solution much faster. Let's write a TSP verifier!

ASSIGNMENT
Complete the verify_tsp function by implementing the algorithm above. Notice that it runs in polynomial time.

ALGORITHM
Loop over each city in the actual path
Sum the distance between each city in the actual path
If the sum is less than dist, return True, otherwise return False
'''

def verify_tsp(paths, dist, actual_path):
    sum = 0
    for i, city in enumerate(actual_path):
        if i + 1 < len(actual_path):
            sum += paths[actual_path[i]][actual_path[i +1]]
    if sum < dist:
        return True
    return False