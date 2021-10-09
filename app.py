from flask import Flask, render_template

app = Flask(__name__)

####################################################

#Твой код

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/video_<id>')
def user(id):
    return f"This is page of video with id:{id}"

####################################################

if __name__ == "__main__":
  app.run(debug=True)