from flask import Flask
app = Flask(__name__)

@app.route('/hell/<name>')
def hello_name(name):
   return 'Hello %s!' % name

if __name__ == '__main__':
   app.run()

from flask import Flask
app =Flask(__name__)
