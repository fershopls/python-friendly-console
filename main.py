import os
from src.Console import Console


class HelloController:

    def __call__(self, ctx):
        print("Helo dude! you said:")
        print(ctx.command)
        print(ctx.argv)
        c = Console('XD > ')
        c.router.route('babe', lambda x: print('Hello'))
        c.listen(ctx.nested_command)



def run():
    c = Console()
    c.router.route('hi', HelloController(), text="Te dire hola crayola")
    c.listen()


if __name__ == '__main__':
    run()

