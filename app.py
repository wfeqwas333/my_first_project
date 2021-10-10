from flask import Flask, render_template 

app = Flask(__name__)

####################################################

#Твой код

@app.route('/1')
@app.route('/home1')
def home():
    return render_template('index.html')

@app.route('/')
@app.route('/home')
def download():
	return render_template('download.html')

@app.route('/wallpaper')
def wallpaper():
	return render_template('wallpaper.html')
####################################################

if __name__ == "__main__":
  app.run(debug=True)