from flask import Flask, app, render_template

app = Flask(__name__)

#--------------------------------------------------------------#
# tableau metadata
import tableauserverclient as TSC
import pandas as pd
#set up authentication
import yaml

with open(r'/Users/skumar763/Documents/Github Repositories/full_stack_web_developement/config.yaml', 'r') as f:
    config = yaml.load(f)

server = TSC.Server(config['tableauconfig']['server_url'])
server.use_server_version()
tableau_auth = TSC.PersonalAccessTokenAuth(config['tableauconfig']['token_name'], config['tableauconfig']['api_token'], config['tableauconfig']['site_name'])
query = """
            {
            workbooks {
                name
            }
            }
        """
with server.auth.sign_in(tableau_auth):
    data = server.metadata.query(query)
wb_name = []
for i in range(len(data['data']['workbooks'])):
    wb_name.append(data['data']['workbooks'][i]['name'])

#--------------------------------------------------------------#

@app.route('/')
def index():
    first_name = 'sivakumar'
    last_name = 'kumaraguru'
    upper_first_name = first_name.upper()
    return render_template('basic.html', variable_first=[upper_first_name,last_name])

@app.route('/tableau')
def tableau():
    return render_template('tableau.html', wb_name=wb_name)

if __name__ == '__main__':
    app.run(debug=True)