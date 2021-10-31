
import requests
from flask import Flask, request, render_template #import main Flask class and request object
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


#--------------------------------------------
@app.route('/html-example')
def query_example():
    language = request.args.get('language') #if key doesn't exist, returns None
    framework = request.args['framework'] #if key doesn't exist, returns a 400, bad request error
    website = request.args.get('website')

    return '''<h1>The language value is: {}</h1>
              <h1>The framework value is: {}</h1>
              <h1>The website value is: {}'''.format(language, framework, website)
#--------------------------------------------


@app.route('/data1', methods = ['POST'])
def postJsonHandler():
    print (request.is_json)
    content = request.get_json()
    print (content)
    return 'JSON posted'




#--------------------------------------------
@app.route('/title',methods=['POST'])
def fitbit_test():
    req_data = request.get_json()
    title =req_data['title'][:] #an index is needed because of the array
    return '''title: {}'''.format(title)
#--------------------------------------------


        
#--------------------------------------------
@app.route('/json-example', methods=['POST']) #GET requests will be blocked
def json_example():
    req_data = request.get_json()
    language = None
    if 'language' in req_data:
        language = req_data['language']

    language = req_data['language']
    framework = req_data['framework']
    python_version = req_data['version_info']['python'] #two keys are needed because of the nested object
    example = req_data['examples'][0] #an index is needed because of the array
    boolean_test = req_data['boolean_test']

    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)

#--------------------------------------------





#--------------------------------------------





if __name__ == "__main__":
       app.run(ssl_context=('certificate.pem', 'privkey.pem'))
