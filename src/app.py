from flask import Flask
from flask_mongoengine import MongoEngine 
from config import config

app= Flask(__name__)
#client = MongoClient(config['MONGO_URI'])

app.config['MONGODB_HOST'] = config['MONGO_URI']
db = MongoEngine()
db.init_app(app)

@app.route('/')
def index():
    return "<b>Hola, bienvenido al curso del ciclo 4a</b>"




if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()