## CLICK (Command line application development)

Installation: `$ pip install click`

#### Working with "option"
`option` is an optional parameter for any command
- @click.option(large_name, small_name, default_value, help_text)
```python
import click
@click.command()
@click.option('--name', '-n', default="Sinha", help='your name please')
def main(name):
    print(f"Hello, {name}")
```
```shell
$ python app.py
$ Hello, Sinha
-----------------------------
$ python app.py --name Mrinal
$ Hello, Mrinal
-----------------------------
NOTE: if default value is not
given then when you run:
$ python app.py
$ Hello, None
```
- if you want to pass certain no of arguments use "nargs"
```python
@click.option('--coordinates', '-c', nargs=2)
# if the option --coordinates is passed it will be
$ python app.py --coordinates 101 201
# if it is less than or greater than 2 it will throw error
```
- passing multiple values for any particular option
```python
@click.option('--places', '-p', multiple=True)
# then you can pass -p multiple times eg:
$ python app.py -p India -p USA -p Peru
```
- specifying type of input explicitly
```python
@click.option('--salary', '-s', type=int)
$ python app.py -s "102" -> 102
$ python app.py -s 102 -> 102
$ python app.py -s "abc" -> throw error
```
----------------------------------------------------
#### Working with "argument"
`argument` are mandatory parameter unless you are not passing default value
- argument(input_name, default=None)
```python
@click.command()
@click.argument('name')
@click.argument('age', type=int)
@click.argument('pan', default="ABCD1234E")
def main(name, pan, age):
    click.echo(f"Hello, {name} ({age} - yrs young!)")
    click.echo(f"Your PAN number is: {pan}")
    click.echo(f"VALID PAN HOLDER") \
        if age >= 18 else click.echo(f"INVALID PAN HOLDER")
```
working with `nargs`
- If you pass `nargs = -1` (it will take any number of arguments in)
- If you pass anything else, it will take that amount fixed (as seen above)
```python
@click.argument('places', nargs=-1)
@click.argument('birth_places', nargs=1)
def main(places, birth_places):
    click.echo(f"places: {places}")
    click.echo(f"birth place: {birth_places}")

$ python app.py a b c d e
$ places: (a, b, c, d)
$ birth place: e
```
------------------------
#### Working with "prompt & user input"
`prompt` is used when you want to take user input
```python
@click.command()
@click.option('--name', '-n', prompt=True, help="Please, your name?")
@click.option('--age', '-a', type=int, prompt="What is your age?")
def main(name, age):
    click.echo(f"Hello, {name} >|< Age: {age}")
```
```shell
$ python app.py
$ Name: Mrinal           ## will prompt for name
$ What is your age?: 25  ## will ask for age with custom message
Hello, Mrinal >|< Age: 25
----------------------------------------------------------------
Other way if you pass values as options it will not prompt eg:
$ python app.py --name Mrinal --age 25 ## it will not prompt
Hello, Mrinal >|< Age: 25
```
- taking input in hidden manner using `hide_input`, eg for passwords
```python
@click.option('--password', '-p', prompt=True, hide_input=True)

$ python app.py
$ Password: <take input in hidden manner>
```
- taking password and also confirming `hide_input` & `confirmation_prompt` (re-prompt for confirmation)
```python
@click.option('--password', '-p', prompt=True, hide_input=True, confirmation_prompt=True)

$ python app.py
$ Password: <take input in hidden manner>
$ Repeat for confirmation: <takes input in hidden manner>
# if both do not match it will throw an error and ask again to enter.
```

---------------------------------------------------------------
#### creating command groups
```shell
$ python app.py

Commands:
  leet     Leet given string
  reverse  Reverse given string
  shuffle  shuffle given string
```
so in order to build command groups in python, you create a main
parent head, so everything is going to be grouped under this
parent head, It is going to be the main command and others are
going to be it's sub commands.

```python
@click.group()
def main():
    """ main parent head function """
    pass


@main.command()
@click.argument("text")
def leet(text):
    """
    Leet given string
    """
    # logic

@main.command()
@click.argument("text")
def reverse(text):
    """
    Reverse given string
    """
    # logic

@main.command()
@click.argument("text")
def shuffle(text):
    """
    shuffle given string
    """
    # logic
```
- `main()` is the parent command while `leet`, `reverse` and `shuffle` are the sub-commands.
---------------------------------

#### Adding style to cli tool

You need `colorama` installed -> `$ pip install colorama`
- in order to apply style you can do it directly using click
- `click.echo(click.style(...))` is equivalent to `click.secho(...)`
- all the options provided by this function is: fg, bg, bold, dim, underline, blink, reverse, reset
```python
@click.command()
@click.option('--name', '-n')
def main(name):
    click.echo(f"My name is {name}") # normal printing
    click.echo(
        click.style(
            f"My name is {name}", # text to print
            fg = "red",
            bg = "white",
        )
    )
    # print with all other options
    click.echo(
        click.style(
            f"My name is {name}", # text to print
            fg = "red",
            bg = "white",
            bold = True,
            dim=False,
            underline=True,
            blink=True,
            reverse=True,
            reset=True,
        )
    )

    # In order to apply style you can directly use secho from click
    click.secho(
        f"My name is {name}", # text to print
            fg = "red",
            bg = "white",
            bold = True,
            dim=False,
            underline=True,
            blink=True,
            reverse=True,
            reset=True,
    )
```
-------------------------------------
#### Reading data from configuration file
Firstly you need an additional python package
- `$ pip install click-config-file`

Now, let's say you have a CLI application that takes optional parameter name and salary as input but you don't want to pass those params from the command line rather you want to pass it from a configuration file. Example

```python
import click
import click_config_file

@click.command()
@click.option('--name', '-n', default="Sinha", help="specify name")
@click.option('--salary', '-s', type=int)
@click_config_file.configuration_option() # this will add an option of --config
def main(name, salary):
    click.echo(f"Hello, {name}. Your salary is: {salary}")

if __name__ == "__main__":
    main()
```
```shell
$ python app.py --help

Options:
  -n, --name TEXT       specify name
  -s, --salary INTEGER
  --config FILE         Read configuration from FILE.
  --help                Show this message and exit.
-----------------------------------------------------
one way to run it is:
$ python app_config.py --name Mrinal -s 12000000
$ Hello, Mrinal. Your salary is: 12000000
----------------------------------------------------
Now we want to pass/accept these param in as a config file
now create a configuration file:
$ nano config.conf
name="Mrinal Sinha"
salary="9999999999"
save it...

Now, to pass it in as a config file.
$ python app.py --config config.conf
$ Hello, Mrinal Sinha. Your salary is: 9999999999
```

-------------------------
#### Validating input from the CLI
firstly you need additional package for that
- `$ pip install click_params`

This package helps you with the type and that you can use to validate input, example
```python
import click
from click_params import EMAIL, DOMAIN, PUBLIC_URL

@click.group()
def main():
    pass

@main.command()
@click.option("--name", '-n')
@click.option("--email", '-e', type=EMAIL)
@click.option("--domain", '-d', type=DOMAIN)
@click.option("--website", '-w', type=PUBLIC_URL)
def add_user(name, email, domain, website):
    """
    command to add user
    """
    click.echo(f"Your name is: {name}")
    click.echo(f"Your email is: {email}")
    click.echo(f"Your domain is: {domain}")
    click.echo(f"Your website is: {website}")

if __name__ == "__main__":
    main()
```
```shell
$ python app.py add-user --name Mrinal --email mrinal@
advarisk.com --domain xyz.com --website https://xyz.com

Your name is: Mrinal
Your email is: mrinal@advarisk.com
Your domain is: xyz.com
Your website is: https://xyz.com
```
