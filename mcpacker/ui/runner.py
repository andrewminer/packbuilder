from mcpacker.model.core.world import World

import inspect
import sys


# Class ############################################################################################

class Runner:

    def __init__(self, world:World):
        self.world = world

    def abort(self, message:str, status:int=-1):
        print(message)
        sys.exit(status)

    def run(self, argv:list[str]):
        if len(sys.argv) < 2:
            abort("Please provide a command name")

        commandName = "_command_" + argv[1]
        for name, doCommand in inspect.getmembers(self):
            if name == commandName:
                doCommand(*argv[2:])
                sys.exit(0)

        abort("No command named: " + argv[1])
