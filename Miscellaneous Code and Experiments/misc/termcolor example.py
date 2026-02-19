import sys
from termcolor import colored, cprint

texto = colored('Hello Universe Del CUlo!!!', 'green', attrs=['reverse', 'blink', 'underline'])
print(texto)

cprint('Kelley so good', "red")
cprint('leo', "yellow")
cprint('xxxxx', "blue")

print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
print_red_on_cyan('Hello, World!')
print_red_on_cyan('Hello, Universe!')

for i in range(10):
    cprint(i, 'magenta', end=' ')

cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)
type(texto)
