'''
Complete the matchmake function that simulates players joining and leaving the matchmaking queue. The function should take a list of player names and their actions (either "join" or "leave") as a tuple:

player = ('Bob', 'join')
player = ('Alice', 'leave')
Copy icon
For each call to matchmake:

If the action is "leave", search the queue for the player and remove them if they are in the queue.
If the action is "join", push the player's name onto the queue.
Lastly, check if the queue has at least 4 players in it. If so, pop the first 2 players from the queue and return the following string:
"{player1} matched {player2}!"

Where player1 is the first player popped and player2 is the second player popped.

If there were less than 4 players in the queue, return the following string: "No match found"
'''


def matchmake(queue, player):
    if player[1] == 'join':
        queue.push(player[0])
    elif player[1] == 'leave':
        queue.search_and_remove(player[0])

    if queue.size() >= 4:
        player_one = queue.pop()
        player_two = queue.pop()
        return f'{player_one} matched {player_two}!'
    else:
        return 'No match found'


# don't touch below this line
class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if len(self.items) == 0:
            return None
        temp = self.items[-1]
        del self.items[-1]
        return temp

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def search_and_remove(self, item):
        if item not in self.items:
            return None
        self.items.remove(item)
        return item

    def __repr__(self):
        return f"[{', '.join(self.items)}]"