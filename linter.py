from SublimeLinter.lint import Linter


class Ruff(Linter):
    cmd = ('ruff', '-')
    regex = r'^(?P<file>.+):(?P<line>\d+):(?P<col>\d+): (?P<message>.+)$'
    multiline = False
    defaults = {
        'selector': 'source.python'
    }
