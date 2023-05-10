#Import necessary libraries
from flask import Flask, render_template, request

import numpy as np
import os

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model


from flask import Flask, request, render_template, url_for, jsonify,redirect,url_for,session,logging
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy

filepath = 'medicinal.h5'
model = load_model(filepath)
print(model)

# Create flask instance
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///register.db'
db = SQLAlchemy(app)




model =load_model('medicinal.h5')
print('Model loaded. Check http://127.0.0.1:5000/')

print("Model Loaded Successfully")

def pred_medicinal_leaf(medicinal_plant):
  test_image = load_img(medicinal_plant, target_size = (128, 128)) # load image 
  print("@@ Got Image for prediction")
  
  test_image = img_to_array(test_image)/255 # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  
  result = model.predict(test_image) # predict diseased palnt or not
  print('@@ Raw result = ', result)
  
  pred = np.argmax(result, axis=1)
  print(pred)
  if pred==0:
      return "Alexandrian_Laurel", 'Alexandrian_Laurel.html'

  elif pred==1:
      return "Ankol", 'Ankol.html'
        
  elif pred==2:
      return "Arive-Dantu", 'Arive-Dantu.html'
        
  elif pred==3:
      return "Asparagus", 'Asparagus.html'
       
  elif pred==4:
      return "Basale", 'Basale.html'
        
  elif pred==5:
      return "Benyan_Tree", 'Benyan_Tree.html'
        
  elif pred==6:
      return "Betel", 'Betel.html'
        
  elif pred==7:
      return "Bharangi", 'Bharangi.html'
  elif pred==8:
      return "Birch_leaved_cat_tail", 'Birch_leaved_cat_tail.html'
  elif pred==9:
      return "Black_Rosewood", 'Black_Rosewood.html'
        
  elif pred==10:
      return "Blue_Ginger", 'Blue_Ginger.html'
  elif pred==11:
      return "Brahmi", 'Brahmi.html'
  elif pred==12:
      return "Butterfly_Pea", 'Butterfly_Pea.html'
  elif pred==13:
      return "Calabash", 'Calabash.html'
  elif pred==14:
      return "Caper_Bush", 'Caper_Bush.html'
  elif pred==15:
      return "Cardamom", 'Cardamom.html'
  elif pred==16:
      return "Chathuramulla", 'Chathuramulla.html'
  elif pred==17:
      return "Chebulic_Myrobalan", 'Chebulic_Myrobalan.html'
  elif pred==18:
      return "Chunga", 'Chunga.html'
  elif pred==19:
      return "Cobra_Saffron", 'Cobra_Saffron.html'
  elif pred==20:
      return "Common_ Grape", 'Common_ Grape.html'
  elif pred==21:
      return "Coromandel_Boxwood", 'Coromandel_Boxwood.html'
  elif pred==22:
      return "Cowplant", 'Cowplant.html'
  elif pred==23:
      return "Crape_Jasmine", 'Crape_Jasmine.html'
  elif pred==24:
      return "Crepe_Ginger", 'Crepe_Ginger.html'
  elif pred==25:
      return "Curry", 'Curry.html'
  elif pred==26:
      return "Devil_Pepper", 'Devil_Pepper.html'
  elif pred==27:
      return "Drumstick", 'Drumstick.html'
  elif pred==28:
      return "Fenugreek", 'Fenugreek.html'
  elif pred==29:
      return "Frangipani_Vine", 'Frangipani_Vine.html'
  elif pred==30:
      return "Glabrous", 'Glabrous.html'
  elif pred==31:
      return "Green_Chirayta", 'Green_Chirayta.html'
  elif pred==32:
      return "Guava", 'Guava.html'
  elif pred==33:
      return "Hibiscus", 'Hibiscus.html'
  elif pred==34:
      return "Hill_Pepper", 'Hill_Pepper.html'
  elif pred==35:
      return "Indian _Gooseberry", 'Indian _Gooseberry.html'
  elif pred==36:
      return "Indian_Bael", 'Indian_Bael.html'
  elif pred==37:
      return "Indian_Beech", 'Indian_Beech.html'
  elif pred==38:
      return "Indian_Crocus", 'Indian_Crocus.html'
  elif pred==39:
      return "Indian_Madder", 'Indian_Madder.html'
  elif pred==40:
      return "Indian_Mustard", 'Indian_Mustard.html'
  elif pred==41:
      return "Indian_PENNYwort", 'Indian_PENNYwort.html'
  elif pred==42:
      return "Indian_Pulai", 'Indian_Pulai.html'
  elif pred==43:
      return "Indian_bdellium_tree", 'Indian_bdellium_tree.html'
  elif pred==44:
      return "Iruveli", 'Iruveli.html'
  elif pred==45:
      return "Jackfruit", 'Jackfruit.html'
  elif pred==46:
      return "Jamaica_Cherry-Gasagase", 'Jamaica_Cherry-Gasagase.html'
  elif pred==47:
      return "Jamun", 'Jamun.html'
  elif pred==48:
      return "Jasmine", 'Jasmine.html'
  elif pred==49:
      return "Java_Plum", 'Java_Plum.html'
  elif pred==50:
      return "Jimsonweed", 'Jimsonweed.html'
  elif pred==51:
      return "Karanda", 'Karanda.html'
  elif pred==52:
      return "Kokum", 'Kokum.html'
  elif pred==53:
      return "Krishna_Fig", 'Krishna_Fig.html'
  elif pred==54:
      return "Lark_Daisy", 'Lark_Daisy.html'
  elif pred==55:
      return "Lemon", 'Lemon.html'
  elif pred==56:
      return "Long_Pepper", 'Long_Pepper.html'
  elif pred==57:
      return "Malabar_Ironwood", 'Malabar_Ironwood.html'
  elif pred==58:
      return "Malabar_Neem", 'Malabar_Neem.html'
  elif pred==59:
      return "Malabar_Nut", 'Malabar_Nut.html'
  elif pred==60:
      return "Mango", 'Mango.html'
  elif pred==61:
      return "Mexican_Mint", 'Mexican_Mint.html'
  elif pred==62:
      return "Mint", 'Mint.html'
  elif pred==63:
      return "Miracle_Leaf", 'Miracle_Leaf.html'
  elif pred==64:
      return "Nanjari", 'Nanjari.html'
  elif pred==65:
      return "Narrow_Leaved_Turmeric", 'Narrow_Leaved_Turmeric.html'
  elif pred==66:
      return "Neem", 'Neem.html'
  elif pred==67:
      return "Oleander", 'Oleander.html'
  elif pred==68:
      return "Orchid_Tree", 'Orchid_Tree.html'
  elif pred==69:
      return "Pacific_Rosewood", 'Pacific_Rosewood.html'
  elif pred==70:
      return "Paradise_Tree", 'Paradise_Tree.html'
  elif pred==71:
      return "Parijata", 'Parijata.html'
  elif pred==72:
      return "Peacocks_tail", 'Peacocks_tail.html'
  elif pred==73:
      return "Peepal", 'Peepal.html'
  elif pred==74:
      return "Pomegranate", 'Pomegranate.html'
  elif pred==75:
      return "Pride_of_India", 'Pride_of_India.html'
  elif pred==76:
      return "Pseudarthria", 'Pseudarthria.html'
  elif pred==77:
      return "Putranjiva", 'Putranjiva.html'
  elif pred==78:
      return "Rasna", 'Rasna.html'
  elif pred==79:
      return "Red_Sandalwood", 'Red_Sandalwood.html'
  elif pred==80:
      return "Rose_apple", 'Rose_apple.html'
  elif pred==81:
      return "Roxburgh_fig", 'Roxburgh_fig.html'
  elif pred==82:
      return "Sabah_Snake_Grass", 'Sabah_Snake_Grass.html'
  elif pred==83:
      return "Saim_Weed", 'Saim_Weed.html'
  elif pred==84:
      return "Sal_Leaved_Desmodium", 'Sal_Leaved_Desmodium.html'
  elif pred==85:
      return "Sandalwood", 'Sandalwood.html'
  elif pred==86:
      return "Snuhi", 'Snuhi.html'
  elif pred==87:
      return "Soursop", 'Soursop.html'
  elif pred==88:
      return "Tadehagi_Triquetrum", 'Tadehagi_Triquetrum.html'
  elif pred==89:
      return "Tender_wild_jack", 'Tender_wild_jack.html'
  elif pred==90:
      return "Thottea", 'Thottea.html'
  elif pred==91:
      return "Three_leaved _caper", 'Three_leaved _caper.html'
  elif pred==92:
      return "Touch_me_not_plant", 'Touch_me_not_plant.html'
  elif pred==93:
      return "Tree_turmeric", 'Tree_turmeric.html'
  elif pred==94:
      return "Tulsi", 'Tulsi.html'
  elif pred==95:
      return "Venezuelan_tree_bine", 'Venezuelan_tree_bine.html'
  elif pred==96:
      return "Water_Hemp", 'Water_Hemp.html'
  elif pred==97:
      return "West_Indian_Jasmine", 'West_Indian_Jasmine.html'
  elif pred==98:
      return "Wild_Guava", 'Wild_Guava.html'
  elif pred==99:
      return "Wild_Hops", 'Wild_Hops.html'

    




class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))
    contactno = db.Column(db.String(80))

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

# render index.html page
@app.route("/index", methods=['GET', 'POST'])
def index():
        return render_template('index.html')
    
 
# get input image from client then predict class and render respective .html page for solution
@app.route("/predict", methods = ['GET','POST'])
def predict():
     if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('static/upload/', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred, output_page = pred_medicinal_leaf(medicinal_plant=file_path)
              
        return render_template(output_page, pred_output = pred, user_image = file_path)


 

@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form["username"]
        passw = request.form["password"]
        
        login = user.query.filter_by(username=uname, password=passw).first()
        if login is not None:
            return redirect(url_for("index"))
        else:
            p='Invalid username or password'
            return render_template("login.html",p=p)
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['username']
        mail = request.form['email'] 
        passw = request.form['password']
        cno = request.form['cno']
        pwd = request.form['pwd']
        if passw == pwd:
            register = user(username = uname, email = mail, password = passw,contactno=cno)
            db.session.add(register)
            db.session.commit()
            return redirect(url_for("login")) 
        else:
            p='Password not match'
            return render_template("register.html",p=p)
    return render_template("register.html")  
    
# For local system & cloud
# if __name__ == "__main__":
#     app.run(threaded=False,port=8080) 
    
if __name__ == "__main__":
    # db.create_all() 
    # app.run(debug=True)    
    app.run(threaded=False,port=8080) 
