x = 1

class exit():
    def run():
        x = 0

def runCommand(string):
    string.run()

while x == 1:
    playerInput = input("> ")
    runCommand(playerInput)
    