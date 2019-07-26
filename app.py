from flask import Flask,request,Response,url_for,redirect
import json
import os

app = Flask("myapp")

app.config['upload_path'] = 'static/upload'

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/args')
def getParam():
    s = request.args
    for item in s.keys():
        print(item,s[item])

    print(request.path)
    print(request.full_path)
    print(request.args.get("sex","nv"))
    print(request.args.getlist('num'))
    return request.args.__str__()

#接受formdata 请求
@app.route('/post',methods=['post'])
def getPost():
    print(request.headers)
    print(request.form)
    print(request.form.get("name"))
    print(request.form.getlist("num"))
    print(request.json)
    return 'success'

#接受 json 请求
@app.route('/json',methods=['post'])
def getPostJson():
    print(request.json)
    jsons=request.json
    res = Response(json.dumps(jsons),mimetype="application/json")
    res.headers.add("python","flash")
    return res

#上传单个文件
@app.route('/upload',methods=['post'])
def uploadFile():
    files = request.files['files']
    if not os.path.exists(app.config['upload_path']):
        os.makedirs(app.config['upload_path'])
    filepath = app.config['upload_path']+'/'+files.filename
    files.save(filepath)
    return 'success'

#上传多个文件
@app.route('/mulupload',methods=['post'])
def uploadMulFile():
    files = request.files.getlist('files')
    if not os.path.exists(app.config['upload_path']):
        os.makedirs(app.config['upload_path'])
    for file in files:
        filepath = app.config['upload_path']+'/'+file.filename
        file.save(filepath)
    return 'success'

#获取/user/{id}请求
@app.route('/url/<name>',methods=['get'])
def getUrl(name):
    return name

#获取/user/{id}请求,参数为 int
@app.route('/url/id/<int:id>',methods=['get'])
def getintUrl(id):
    print(type(id))
    return str(id)

#获取/user/{id}请求,参数为 int
@app.route('/url/test/<int:id>_<int:id2>',methods=['get'])
def getint2Url(id,id2):
    print(type(id))
    print(id)
    print(id2)
    return 'success'

#生成url
@app.route('/genurl',methods=['get'])
def genUrl():
    s=url_for('getint2Url',id=55,id2=66)
    print(s)
    ss=url_for('getParam',p=5)
    print(ss)
    return 'success'

#重定向
@app.route('/redict',methods=['get'])
def genRedict():
    s=url_for('getint2Url',id=55,id2=66)
    return redirect(s)



if __name__ == '__main__':
    app.run(host='127.0.0.1',port=9898,debug=True)
