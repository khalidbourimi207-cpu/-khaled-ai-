


from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.form['message']
    return f"AI رد عليك: {user_msg}"

if __name__ == '__main__':
    app.run(debug=True)
  
