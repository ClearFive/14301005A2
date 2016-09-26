def app(environ, start_response):
    """ A barebones WSGI application.
    This is a starting point for you own Web Framework :)
    """
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello aaa\n']