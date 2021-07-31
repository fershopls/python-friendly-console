class Console:

    def __init__(self, namespace='$ ', help_enabled=True):
        self.namespace = namespace
        self.router = Router()
        self.help_enabled = help_enabled

    def listen(self, command=''):
        if command:
            return self.call(command)

        while True:
            command = input(self.namespace)
            self.call(command)

            if command == 'help' and self.help_enabled:
                self.router.print_help()

            if command == 'exit':
                break

            if command == 'die':
                exit(0)

    def call(self, command):
        route = self.router.match(command)
        if route:
            self.__execute_route(command, route)

    def __execute_route(self, command, route):
        ctx = Context(command=command, console=self)
        try:
            route.run(ctx)
        except AssertionError as e:
            self.__error(e)

    def __error(self, e):
        print('<!> %s' % e)


class Context:

    def __init__(self, command=None, console=None):
        self.command = command
        self.argv = command.split(' ')
        self.console = console
        self.nested_command = '_'.join(self.argv[1:])


class Router:

    def __init__(self):
        self.routes = []

    def route(self, *args, **kwargs):
        route = Route(*args, **kwargs)
        self.routes.append(route)
        return self

    def match(self, pattern):
        for route in self.routes:
            if route.match(pattern):
                return route
        return None

    def print_help(self):
        print('Available commands:')
        for route in self.routes:
            print('  %s' % route.help())


class Route:

    def __init__(self, pattern, callback, text=''):
        self.pattern = pattern
        self.callback = callback
        self.text = text

    def match(self, command):
        return command.startswith(self.pattern)

    def run(self, *args, **kwargs):
        self.callback(*args, **kwargs)

    def __str__(self):
        return '<%s>' % self.pattern

    def help(self):
        command = self.pattern.ljust(14)
        if self.text:
            command += ' %s' % self.text
        return command
