import cgi
from scipy import compress, transpose
from scipy.linalg import svd, det
import json

def calculate_nullspace(A, eps=1e-15):
    u, s, vh = svd(A)
    null_mask = (s <= eps)
    null_space = compress(null_mask, vh, axis=0)
    return transpose(null_space)

def calculate_eigenvalues(A, eps=1e-15):
    u, s, vh = svd(A)
    return s

def application(environ, start_response):
    parameters = cgi.parse_qs(environ.get('QUERY_STRING', ''))

    query_string = str(parameters['matrix'][0])
    matrix = query_string.splitlines()
    for index, row in enumerate(matrix):
        matrix[index] = row.split()

    while len(matrix) < len(matrix[0]):
        matrix.append([0]*len(matrix[0]))

    nullspace = calculate_nullspace(matrix)
    if nullspace.max() != 0:
        nullspace = nullspace / nullspace.max()

    eigenvalues = calculate_eigenvalues(matrix)
    determinant = det(matrix)

    output = json.dumps({
        'nullspace' : str(nullspace),
        'eigenvalues' : str(eigenvalues),
        'determinant' : str(determinant)
        })

    output_len = sum(len(line) for line in output)
    start_response('200 OK', [('Content-type', 'application/json'),
                              ('Content-Length', str(output_len))])
    return output
