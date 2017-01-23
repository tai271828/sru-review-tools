""" supporting functionalities for UI commands"""

class TypeNameRegistry(dict):
    """
    Registry class for the name of types.
    """
    def register(self, type_obj):
        self[type_obj.__name__] = type_obj
        return type_obj

class CommandRegistry(TypeNameRegistry):
    def register(self, cmdtype):
        name = cmdtype.__name__
        if name.islower():
            return super(CommandRegistry, self).register(cmdtype)
        else:
            return None
cmdregy = CommandRegistry() # registry singleton

class CommandMeta(type):
    def __new__(cls, name, bases, namespace):
        newcls = super(CommandMeta, cls).__new__(cls, name, bases, namespace)
        # register a new class to the registry singleton
        cmdregy.register(newcls)
        return newcls

class Command(metaclass=CommandMeta):
    """
    base class for a real command class.
    """

    def __init__(self):
        import argparse

        parser = argparse.ArgumentParser()
        parser.add_argument_group('Global', 'Global argument parser')

        self.parser = parser
        self._opargs = None

    @property
    def opargs(self):
        if not self._opargs:
            args = self.parser.parse_args()
            narg = len(args)
            if narg >= 1:
                args = args[1:]
            else:
                args = []
            self_opargs = args

        return self._opargs

    def __call__(self):
        raise NotImplementedError

def run():
    """
    Command runner.
    """
    import sys
    import autoreview.command
    narg = len(sys.argv)
    if narg >= 2 and not sys.argv[1].startswith('-'):
        cmdcls = cmdregy.get(sys.argv[1], None)
    else:
        cmdcls = None
    if cmdcls == None:
        cmdcls = cmdregy['help']
    cmd = cmdcls()
    cmd()
