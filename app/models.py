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
        return 'User: {}{}{}{}'.format(self.name, self.password_hash, self.userID, self.email)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_id(self):
        return (self.userID)
    
    def get_name(self):
        return(self.name)
    
    def get_email(self):
        return(self.email)

# will store messages as a JSON object in conv_json
class conversations(db.Model):
    conversationID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    conv_json = db.Column(db.Text)
    userID = db.Column(db.Integer, db.ForeignKey('user.userID'), nullable=False)

    def __repr__(self):
        return 'Conversation ID: {}, Title: {}, UserID: {}'.format(self.conversationID, self.title, self.userID)

    def get_id(self):
        return (self.conversationID)
    
    def get_title(self):
        return(self.title)
    
    def get_json(self):
        return(self.conv_json)
    
    def set_title(self, title):
        self.title = title
    
    def set_json(self, json):
        self.conv_json = json

