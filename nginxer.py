#!./env/bin/python
import click
from var_dump import var_dump
import sqlite3


# def help2():
#     """Simple program that greets NAME for a total of COUNT times."""
#     for x in range(count):
#         click.echo('Hello %s!' % name)


class Database(object):
    # CREATE TABLE domains(id int, name string)
    database = "db.sqlite"
    connection = None
    cursor = None

    def __init__(self):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()

    # An instance method. All methods take "self" as the first argument
    def get_list(self):
        for row in self.cursor.execute('SELECT * FROM domains'):
            print row



@click.command()
@click.option('--list', '-l', is_flag=True, help="Will print verbose messages.")
@click.option('--install', '-i', is_flag=True, help="Will print verbose messages.")
@click.option('--remove', '-r', is_flag=True, help="Will print verbose messages.")
@click.option('--status', '-s', is_flag=True, help="Will print verbose messages.")
@click.option('--name', '-n', multiple=True, default='', help='Who are you?')
def initial(list, install, remove, status, name):
    db = Database()
    if True is list and 0 == len(name):
        db.get_list()


if __name__ == '__main__':
    initial()

