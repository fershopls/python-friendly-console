import sys
from src.Console import Console

class JokeController:

    def __init__(self):
        self.index = 0
        self.jokes = [
            'Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them.',
            'Why do we tell actors to “break a leg?” Because every play has a cast.',
            'Helvetica and Times New Roman walk into a bar. “Get out of here!” shouts the bartender. “We don’t serve your type.”'
        ]

    def __call__(self, ctx):
        print(self.jokes[self.index])
        self.index += 1
        if self.index == len(self.jokes):
            self.index = 0


class NestedConsoleController:

    def __call__(self, ctx):
        c = Console(namespace='(NEST) $ ')
        c.router.route('nested1', lambda ctx: print('Hi! im 1'), text='Prints a really good command')
        c.router.route('nested2', lambda ctx: print('Hi! im 2'), text='Prints a second command')
        c.router.route('nested3', lambda ctx: print('Hi! im 3'), text='Prints a third command')
        c.listen(ctx.nested_command)


def run(nested_command):
    c = Console()
    c.router.route('hello', lambda ctx: print('Hello world!'), text='Prints hello world!')
    c.router.route('joke', JokeController(), text='Prints a funny joke')
    c.router.route('nested', NestedConsoleController(), text='Nested console! Really cool')
    c.listen(nested_command)


if __name__ == '__main__':
    run(sys.argv[1:])

