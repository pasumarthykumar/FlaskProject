from flask import Flask, jsonify
from werkzeug.exceptions import BadRequest, Unauthorized, NotFound, InternalServerError

app = Flask(__name__)

# Custom error handling for HTTP status codes

# 400: Bad Request
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    response = jsonify(error=str(error.description))
    response.status_code = error.code
    return response

# 401: Unauthorized
@app.errorhandler(Unauthorized)
def handle_unauthorized(error):
    response = jsonify(error=str(error.description))
    response.status_code = error.code
    return response

# 404: Not Found
@app.errorhandler(NotFound)
def handle_not_found(error):
    response = jsonify(error=str(error.description))
    response.status_code = error.code
    return response

# 500: Internal Server Error
@app.errorhandler(InternalServerError)
def handle_internal_server_error(error):
    response = jsonify(error=str(error.description))
    response.status_code = error.code
    return response

# Custom error handling for other errors

# 403: Forbidden
@app.errorhandler(403)
def handle_forbidden(error):
    response = jsonify(error="Forbidden: You don't have permission to access this resource.")
    response.status_code = 403
    return response

# 422: Unprocessable Entity
@app.errorhandler(422)
def handle_unprocessable_entity(error):
    response = jsonify(error="Unprocessable Entity: The request was well-formed but semantically incorrect.")
    response.status_code = 422
    return response

# 429: Too Many Requests
@app.errorhandler(429)
def handle_too_many_requests(error):
    response = jsonify(error="Too Many Requests: You have exceeded your request rate limits.")
    response.status_code = 429
    return response

# Sample API route that triggers different errors
@app.route('/sample_error/<int:error_code>', methods=['GET'])
def sample_error_route(error_code):
    if error_code == 400:
        raise BadRequest("Bad Request")
    elif error_code == 401:
        raise Unauthorized("Unauthorized")
    elif error_code == 404:
        raise NotFound("Not Found")
    elif error_code == 500:
        raise InternalServerError("Internal Server Error")
    else:
        return jsonify({'message': 'No error triggered'}), 200

if __name__ == '__main__':
    app.run(debug=True)
