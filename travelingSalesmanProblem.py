'''
ALGORITHM
Get the matrix of possible paths using the permutations function. This matrix holds all possible paths through the given cities. For example, permutations([1,2,3]) would result in:
[
    [1, 2, 3],
    [2, 1, 3],
    [3, 2, 1],
    [2, 3, 1],
    [3, 1, 2],
    [1, 3, 2]
]
Copy icon
Where the first path, [2, 1, 3] represents moving from city 2 -> city 1 -> city 3

Loop over each path
Loop over each city in the path keeping a sum of all the distances between each city.
If the total distance in the path is less than the given dist return true
If no short paths were found, return false
'''

def tsp(cities, paths, dist):
    possible_paths = permutations(cities)

    for path in possible_paths:
        sum = 0
        for i, city in enumerate(path):
            if i < len(path) - 1:
                sum += paths[path[i]][path[i +1]]
        if sum < dist:
            return True

    return False