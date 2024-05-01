from flask import Flask, request, send_file, jsonify, render_template

app = Flask(__name__,
            static_folder='static',
            template_folder='templates')

@app.route('/pve1', methods=['POST'])
def pve1 ():
    return (send_file: 
