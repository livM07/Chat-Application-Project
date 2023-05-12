from app import db

class user(db.Model):
    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)


# will store messages as a JSON object in conv_json
class conversations(db.Model):
    conversationID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    conv_json = db.Column(db.Text)
    userID = db.Column(db.Integer, db.ForeignKey('user.userID'), nullable=False)

