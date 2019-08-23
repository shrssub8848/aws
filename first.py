from flask import request, Flask
import boto3

app = Flask(__name__)
@app.route("/subodh")
def home():
    return '''<form method=POST enctype=multipart/form-data action="upload">
    <input type=file name=subodhfile>
    <input type=submit>
    </form>'''

@app.route("/upload",methods=['POST'])
def upload():
    s3 = boto3.resource('s3')
    s3.Bucket('subodhbucket').put_object(
        Key= 'myfile1',
        Body=request.files['subodhfile']
    )
    #s3.meta.client.upload_file('/home/shuv/Downloads/landscape01.png','subodhbucket',  'file')
    return 'File Uploaded Successfully'

if __name__=="__main__":
    app.run(debug=True)