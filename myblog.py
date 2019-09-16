from app import app, db
from app.models import User, Post


# настройка flask shell
# облегчаем себе жизнь при импорте БД и User & Post
# обязательно обновить переменную export FLASK_APP=myblog.py
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
