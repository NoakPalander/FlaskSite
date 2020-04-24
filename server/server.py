'''
    -- server.py
    -- The backend server for the WebHistory project using flask
'''

from flask import Flask, request, jsonify
import traceback
import json

MIME = {
    '.html' : 'html/',
    '.css' : 'css/',
    '.js' : 'js/',
    '.png' : 'resources/',
    '.jpg' : 'resources/',
    '.ico' : 'resources/',
    '.json' : 'resources/'
}

app = Flask(__name__, static_folder='../public')

@app.errorhandler(404)
def PageNotFound(e = None):
    return '<h1>404 page not found</h1>'

@app.errorhandler(500)
def InternalServerError(e = None):
    return '<p>Flask 500<pre>' + traceback.format_exc()

def SendHistory(date: str, img: str):
    out = {}
    
    with open('public/resources/data.json') as jsonReader:
        objects = json.load(jsonReader)
        out['header'] = objects[date]['header']
        out['text'] = ''.join(objects[date]['text'])
        out['img'] = img

    with open('public/html/history.html') as htmlReader:        
        data = htmlReader.readlines()

        for index, line in enumerate(data):
            # <h1 id="header"></h1>
            if 'id="header"' in line:
                indention = len(line[:line.find('<')])
                data[index] = f'{" " * indention}<h1 id="header">{out["header"]}</h1>\n'

            # <p id="text"></p>
            elif 'id="text"' in line:
                indention = len(line[:line.find('<')])
                data[index] = f'{" " * indention}<p id="text">{out["text"]}</p>\n'

            # <img id="image">
            elif 'id="image"' in line:
                indention = len(line[:line.find('<')])
                data[index] = f'{" " * indention}<img id="image" src="{out["img"]}">\n'

        return ''.join(data)


# Returns a static resource file from the public folder
@app.route('/<path:path>')
def GetStaticFile(path: str, methods=['GET', 'POST']):
    try:
        file = MIME[path[path.find('.'):]] + path 
    
        year = request.args.get('year')
        image = request.args.get('img')
        
        if year != None and image != None:
            return SendHistory(date=year, img=image)

        return app.send_static_file(file)

    except KeyError:
        return PageNotFound()
    
    except:
        return InternalServerError()

@app.route('/')
def Home():
    # Reroutes to the base file
    return GetStaticFile('/index.html')

if __name__ == '__main__':
    app.run(host=SOMEIPSTRING, port=SOMEPORTNUM)
