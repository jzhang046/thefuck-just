import re
from thefuck.utils import for_app, memoize, which

@memoize
def just_available(): 
    return bool(which('just'))

@for_app('just', at_least=1)
def match(command):
    is_proper_command = ('error' in command.output and 
                         'Justfile does not contain recipe' in command.output and
                         'Did you mean' in command.output)
    return is_proper_command


def get_new_command(command):
    matcher = re.search('error: Justfile does not contain recipe `(?:[^`]+)`.\\nDid you mean `(.+)`\\?', command.output)
    return ["just " + matcher.group(1)]

enabled_by_default = just_available()

requires_output = True
