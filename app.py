from flask import Flask
from flask_mongoengine import MongoEngine     # pip install flask-mongoengine

app=Flask(__name__)
app.config['MONGODB_SETTINGS']-{
    'db':'dbmongocrud',
    'host':'localhost',
    'port':27017
}

db=MongoEngine()
db.init-app(app)

class User(db.Document):
    name=db.StringField()
    email=db.StringField()
    
    def to_json(self):
        return {'name':self.name,
                'email':self.email}
        
@app.route('/')
def query_records():
    name='aditi'
    user=User.objects(name=name).first()
    
    if not user:
        return jsonify({'error':'data not found'})
    else:
        return jsonify(user.to_json())
    

@app.route('/add')
def create_records():
    user=User(name='aisha',
              email='aisha@gmail.com')
    user.save()
    return jsonify(user.to_json())

@app.route('/update')
def update_records():
    name='aditi'
    user=User.objects(name=name).first()
    if not user:
        return jsonify({'error':'data not found'})
    else:
        user.update(email='emailupdate@gmail.com')
        return jsonify(user.to_json())
    
@app.route('/delete')
def delete_records():
    name='aditi'
    user=User.objects(name=name).first()
    if not user:
        return jsonify({'error':'data not found'})
    else:
        user.delete()
        return jsonify(user.to_json())