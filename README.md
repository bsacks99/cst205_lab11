player = Player()

key = Item('key', 'unlock')

player.pickUp(key)

printNow(player.listItems())

printNow("There is a locked door in front of you")

choice = requestString("What would you like to do: ")

if choice.lower() == 'use key':
    if player.useItem('key') == 'unlock':
        printNow("You have unlocked the door")

Etc.
