import urlparse
import json

import scipy
import scipy.linalg
from scipy import *

def null(A, eps=1e-15):
    u, s, vh = scipy.linalg.svd(A)
    null_mask = (s <= eps)
    null_space = scipy.compress(null_mask, vh, axis=0)
    return scipy.transpose(null_space)

def eigenvalues(A, eps=1e-15):
    u, s, vh = scipy.linalg.svd(A)
    return s

def application(environ, start_response):
    if environ['REQUEST_METHOD'] == 'POST':
        post_data = environ['wsgi.input'].read()

	post_data = urlparse.parse_qsl(post_data, True, True)

        data_string = str(post_data[0][1])
        data_rows = data_string.splitlines()
        for index, row in enumerate(data_rows):
            data_rows[index] = row.split()

	given_matrix = data_rows
        null_space = null(given_matrix)
        try:
            null_space = null_space / null_space.max()
        except:
            pass

#        la, v = scipy.linalg.eig(given_matrix)
#	output += "eigenvalues:<br>"
#        for l in la:
#            output += str(l)
        determinant = scipy.linalg.det(given_matrix)

    output = json.dumps({
        'nullspace' : str(null_space),
        'eigenvalues' : str(eigenvalues(given_matrix)),
        'determinant' : str(determinant)
        })

    output_len = sum(len(line) for line in output)
    start_response('200 OK', [('Content-type', 'application/json'),
                              ('Content-Length', str(output_len))])
    return output
