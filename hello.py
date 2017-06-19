bind = '0.0.0.0:8080'


def get_body(environ):
	body = environ["QUERY_STRING"].replace('&', '\n')
	return body.encode('utf-8')


def wsgi_application(environ, start_response):
	status = "200 OK"
	headers = [("Content-Type", 'text/plain')]
	body = get_body(environ)
	start_response(status, headers)
	return [body]
