from flask import Flask, request, make_response, render_template
import toml

app = Flask(__name__,template_folder='templates')

@app.route('/pve<int:node_id>', methods=['POST'])
def handle_post(node_id):
    # Build the fqdn using the node_id from the URL
    fqdn = f"pve{node_id}.dc01.lehighwifi.network"
    
    return render_template('template.toml', fqdn=fqdn)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
