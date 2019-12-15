from app import app, db
from app.models import User, Post


@app.shell_context_processor
def make_shell_context(): # invoked everytime flask shell is inputted 
    return {'db': db, 'User': User, 'Post': Post}
