# Usage
```python
# main.py
import sys
from src.Console import Console

def hello_callback():
    print ('Hello world!')

c = Console()
c.router.route('hello', hello_callback)
c.listen()
```
Now if you run:
```shell
python main.py hello
```

You will get the message
`Hello world!`
in your screen.

## What if...
```shell
python main.py
```

calling the script directly
will start the console
in interactive mode

you will see something like:

```
$
```

### Interactive mode activated!

Now lets run help:
```shell
$ help
```

this will print a message like this one:

```shell
$ help
Available commands:
  hello
  exit
  die
```

and if we run:

```shell
$ hello
```

We got our hello world!

```shell
$ hello
Hello world!
```