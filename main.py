from bottle import route, run, template, static_file, request, redirect


@route('/')
def index():
    return template('view/index')

@route('/search')
def index():
    keywords = request.query.get('keywords')
    results = ['a', 'b', 'c']
    return template('view/search', keywords = keywords, results= results)



@route('/bootstrap/css/<filename>')
def server_static(filename):
    return static_file(filename, root='./bootstrap/css')

@route('/bootstrap/js/<filename>')
def server_static(filename):
    return static_file(filename, root='./bootstrap/js')



run(host='localhost', port=8080)
