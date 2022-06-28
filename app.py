from flask import Flask
import os

app = Flask(__name__)

env_var = os.environ
  
# Print the list of user's
# environment variables
print("User's Environment variable:")
print(dict(env_var))

# tenant_id = os.environ['id_tenant']

@app.route('/')
def index():
    return dict(env_var)
    # return 'App Works!'+tenant_id
    
@app.route('/getdata')
def getdata():

    return 'this is the data '

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)