"""
Design classes, their objects and methods for the game Among Us in python using oops concepts

"""

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.is_impostor = False
        self.tasks = []

    def assign_task(self, task):
        self.tasks.append(task)
        print(f"{self.name} received task: {task.name} in {task.location}")

    def complete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"{self.name} completed task: {task.name} in {task.location}")
        else:
            print(f"{self.name} doesn't have task: {task.name} in {task.location}")

    def report(self, other_player):
        if self.is_impostor:
            print(f"{self.name} reported {other_player.name}")
        else:
            print(f"{self.name} is not an impostor and cannot report")

class Task:
    def __init__(self, name, location):
        self.name = name
        self.location = location

class Spaceship:
    def __init__(self, tasks):
        self.tasks = tasks
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def start_game(self):
        impostor = self.players[0]
        impostor.is_impostor = True
        print(f"Game started! {impostor.name} is the impostor.")

# Creating tasks
tasks = [
    Task("Fix Wiring", "Electrical"),
    Task("Empty Garbage", "Storage"),
    Task("Swipe Card", "Admin")
]

# Creating players
players = [
    Player("Player1", "Red"),
    Player("Player2", "Blue"),
    Player("Player3", "Green")
]

# Creating spaceship
spaceship = Spaceship(tasks)
for player in players:
    spaceship.add_player(player)

spaceship.start_game()

players[0].assign_task(tasks[0])
players[0].complete_task(tasks[0])
players[1].report(players[0])
