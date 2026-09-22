#Scope

enemies = 1 #Global

def increase_enemies():
    enemies = 2 #Local
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#Global usage
player_level = 1
def increase_level():
    global player_level
    player_level += 1

#Or do this:
def increase_multiple_levels(levels):
    return player_level + levels


print(f"The player's level: {player_level}")
increase_level()
print(f"The player leveled up to: {player_level}")
player_level = increase_multiple_levels(8)
print(f"The player leveled up to: {player_level}")

players = ["Casper", "Nikolaj", "Mathias"]

# No block variable
if len(players) < 4:
    new_player = "Ali"
    players.append(new_player)
print(new_player)