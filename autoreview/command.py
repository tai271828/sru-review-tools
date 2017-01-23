"""
Comamnds for users.

Implement the command by following these rules:
    1. the class name should be lower-cased, so the command registry could register them by names.
    2. the class should inherit from Command class of cmdutil module.
    3. the class should implement __call__ function.
"""

from .cmdutil import Command

class help(Command):
    """
    help command.
    """
    
    def __call__(self):
        print("The help command is called.")
        print("Let's do something else funnier.")


class smoketest(Command):
    """
    A prototype command to test this command pattern.
    """
    
    def __call__(self):
        print("The smoketest command is called.")
        print("Let's do something else funnier.")


class sid(Command):
    """
    Get submission ID from the html report by specifying CID
    """

    def __init__(self):
        super(sid, self).__init__()
        group = self.parser.add_argument_group('SID_CID', 'Get submission ID from the html report by specifying CID')
        group.add_argument('sid', action='store', type=str)
        group.add_argument('--cid', action='store', type=str, dest='cid', default=None, help='host CID')

    def __call__(self):
        cid = self.opargs
        #print("I get cid %s" % cid)
        print("I get cid " )
