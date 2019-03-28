from bottle import route, run
from bottle import template

@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

@route ( '/ wiki / <pagename>' )             # соответствует / wiki / Learning_Python
def  show_wiki_page ( pagename ):
    ...

#@route ( '/ <action> / <пользователь>' )             # соответствует / follow / defnull
#def  user_api (action ,  пользователь):

#@route('/object/<id:int>')
#def callback(id):
#    assert isinstance(id, int)

#@route('/show/<name:re:[a-z]+>')
#def callback(name):
#   assert name.isalpha()

#@route('/static/<path:path>')
#def callback(path):
#   return static_file(path, ...)

run(host='localhost', port=8080, debug=True)