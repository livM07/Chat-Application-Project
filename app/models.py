from app import db

class user(db.Model):
    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return 'User: {}'.format(self.name, self.password)

# will store messages as a JSON object in conv_json
class conversations(db.Model):
    conversationID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    conv_json = db.Column(db.Text)
    userID = db.Column(db.Integer, db.ForeignKey('user.userID'), nullable=False)

