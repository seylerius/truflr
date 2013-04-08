from flask import Flask
from flask.ext.mongoengine import MongoEngine
app = Flask(__name__)
app.config["MONGODB_DB"] = "DataRoomba"
app.config["MONGODB_HOST"] = "dharma.mongohq.com"
app.config["MONGODB_PORT"] = 10019
app.config["MONGODB_USER"] = "dataroomba"
app.config["MONGODB_PASS"] = "There is no data"
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)

if __name__ == '__main__':
    app.run()