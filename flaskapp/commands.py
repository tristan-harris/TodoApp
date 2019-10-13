import click
from flaskapp.models import Todo
from flaskapp import app, db

@app.cli.command('create-todo')
@click.option('-c', '--content', help='The title of the todo task')
def create_todo(content):
    print(content)
    new_todo = Todo(content=content)
    db.session.add(new_todo)
    db.session.commit()
    click.echo(f'{new_todo} has been added')

