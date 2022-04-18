def wsgi_app(environ, start_response):
	status = "200 OK"
	headers = [
		("Content-Type", "text/plain")
	]
	query_string = environ["QUERY_STRING"]
	body = [bytes(i + "\n", "ascii") for i in query_string.split("&")]
	start_response(status, headers)
	return body
