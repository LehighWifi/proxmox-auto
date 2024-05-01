from flask import Flask, request, make_response
import toml

app = Flask(__name__)

@app.route('/pve<int:node_id>', methods=['POST'])
def handle_post(node_id):
    # Build the fqdn using the node_id from the URL
    fqdn = f"pve{node_id}.dc01.lehighwifi.network"

    # Data to be converted to TOML, using the dynamic fqdn
    data = {
        'global': {
            'keyboard': 'en-us',
            'country': 'us',
            'fqdn': fqdn,
            'mailto': 'proxmox@lehighwifi.com',
            'timezone': 'America/New_York',
            'root_password': 'u9o2Wt8zc4WF',
            'root_ssh_keys': [
                'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIA9VtDKXxFuKqam6cC3Xim8a4Y9j8E1+SOASJSBVfO2S AnthonyP'
            ]
        },
        'network': {
            'source': 'from-dhcp'
        }
    }

    # Convert dictionary to TOML
    toml_string = toml.dumps(data)

    # Create a response with the TOML string as the body
    response = make_response(toml_string)
    response.headers['Content-Type'] = 'application/toml'

    return response

if __name__ == '__main__':
    app.run(debug=True)
