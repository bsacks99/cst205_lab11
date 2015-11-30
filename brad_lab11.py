class Item:
  name = None
  action = None
  
  def __init__(self, name, action):
    self.name = name
    self.action = action
  
  def getName(self):
    return self.name
    
  def getAction(self):
    return self.action

class Knapsack:
  contents = [];
    
  def add(self, item):
    self.contents.append(item)
        
  def discard(self, item):
    count = 0
    for item in self.contents:
      if item.getName() == name:
        self.contents.pop(count) 
      count = count + 1

  def has(self, name):
    for item in self.contents:
      if item.getName() == name: 
        return True
    return False

  def use(self, name):
    for item in self.contents:
      if item.getName() == name:  
        return item.getAction()
  
  def list(self):
    for item in self.contents:
      printNow(item.getName() + ", cabability: " + item.getAction())
    
class Player:
  knapsack = None;
  
  def __init__(self):
    self.knapsack = Knapsack()
    
  def pickUp(self, item):
    self.knapsack.add(item)

  def hasItem(self, item):
    return self.knapsack.has(item)

  def discardItem(self, item):
    self.knapsack.discard(item)
    
  def useItem(self, item):
    return self.knapsack.use(item)
    
  def listItems(self):
    self.knapsack.list()
    
def welcome():
  printNow("Hello. Welcome to the Winchester Mystery House.")
  printNow("Each time you enter a new room you will be facing north.")
  printNow("Find your way to the staircase that leads to the second floor, and you will have won the game.")
  printNow("At any time you may type exit to end the game")
  printNow("When requested, type the direction you would like to go.")
  printNow("To see this message again type help anytime.")
  return 

def entry():

  player = Player()
  
  welcome()
  printNow("You are now in the entryway")
  printNow("You may enter the house by going north.")
  direction = requestString("Which direction would you like to go: ")
  
  while direction.lower() != "north" and direction.lower() != "exit" and direction.lower() != "help":
    direction = requestString("Please enter a valid direction: ")
  
  if direction.lower() == "help":
    welcome()
  
  if direction.lower() == "north":  
    grandFoyer(player)
  elif direction.lower() == "exit":  
    sys.exit("Goodbye. Thank you for playing.")
    
def grandFoyer(player):

  key = Item('key', 'unlock')
  
  printNow("You have entered the Grand Foyer.")
  printNow("On a small table in the Foyer, you see a tiny golden key.")
  printNow("You may go north into the Middle Hallway, west into the Library, east into the Art Gallery, south to exit the House, or you may 'pick up the key'.")
  direction = requestString("What would you like to do: ")
  
  while direction.lower() != "north" and direction.lower() != "east" and direction.lower() != "west" and direction.lower() != "south" and direction.lower() != "pick up the key" and direction.lower() != "exit" and direction.lower() != "help":
    direction = requestString("Please enter a valid direction: ")
  
  if direction.lower() == "help":
    welcome()
    
  if direction.lower() == "north":
    middleHallway()
  elif direction.lower() == "east":
    artGallery()
  elif direction.lower() == "west":
    library()
  elif direction.lower() == "south":
    entry()
  elif direction.lower() == "pick up the key":
    player.pickUp(key)
    printNow("You have picked up the key")
    printNow("You now have:")
    printNow(player.listItems())
  elif direction.lower() == "exit":  
    sys.exit("Goodbye. Thank you for playing.")
    
entry()
