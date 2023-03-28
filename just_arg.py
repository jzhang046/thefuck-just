import re
from thefuck.utils import for_app, memoize, which

@memoize
def just_available(): 
    return bool(which('just'))

@for_app('just', at_least=1)
def match(command):
    is_proper_command = ('error' in command.output and 
                         'Found argument' in command.output and
                         'which wasn\'t expected, or isn\'t valid in this context' in command.output and
                         'Did you mean' in command.output)
    return is_proper_command


def get_new_command(command):
    matcher = re.search('error: Found argument \'([^\']+)\' which wasn\'t expected, or isn\'t valid in this context\\n\\tDid you mean (.+)\\?', command.output)
    return [
        command.script.replace(matcher.group(1), matcher.group(2)),
        "just --help",
        "just --list"
    ]

enabled_by_default = just_available()

requires_output = True
