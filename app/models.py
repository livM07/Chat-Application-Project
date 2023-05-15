from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(userID):
    return user.query.get(int(userID))

# TO DO -> in create form incoporate flask msging to ensure all fields are completed
class user(db.Model, UserMixin):
    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return 'User: {}'.format(self.name, self.password)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_id(self):
        return (self.userID)

# will store messages as a JSON object in conv_json
class conversations(db.Model):
    conversationID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    conv_json = db.Column(db.Text)
    userID = db.Column(db.Integer, db.ForeignKey('user.userID'), nullable=False)

