from flask import Flask, render_template, request
import os
from getBlock import getBlockData

STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
app.use_static_for_root = True

@app.route("/", methods= ["GET", "POST"])
def home():   
    if request.method == "GET":
        return render_template('index.html')
    else:
        blockNumber = request.form.get("blockNumber")
        blockData = getBlockData(int(blockNumber))
        return render_template('index.html', blockData = blockData)
       
if __name__ == '__main__':
    app.run(debug = True, port=4000)