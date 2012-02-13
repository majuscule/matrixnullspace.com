import urlparse

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

	output = "<pre>"
	#output += post_data
	output += "<br>"

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

	output += "<h1>"
	output += "nullspace:<br>"
	output += str(null_space)
	output += "<br><br>"
	output += "eigenvalues:<br>"
	output += str(eigenvalues(given_matrix))
	output += "<br><br>"
	output += "determinant:<br>"
	output += str(determinant)
#	output += "<br><br>"
#	output += "eigenvalues:<br>"
#	output += str(l1)
#	output += "<br><br>"
#	output += "eigenvectors:<br>"
#	output +=  str(v[:,0][0])
	output += "</h1>"

    # send results
    output_len = sum(len(line) for line in output)
    start_response('200 OK', [('Content-type', 'text/html'),
                              ('Content-Length', str(output_len))])
    return output
