
def reader(path):
    with open(path) as f:
        contents = f.read()
        contents = contents.split("matrix\n")
        matrix = "".join(contents).split("vector\n")[0]
        vector = "".join(contents).split("vector\n")[1]
        matrix = "".join(matrix)
        vector = "".join(vector)
        matrix = transform_matrix(matrix)
        vector = transform_vector(vector)
        return matrix, vector
def transform_matrix(matrix):
    l = matrix.splitlines()
    for i in range(len(l)):
        l[i] = l[i].split()
    for i in range(len(l)):
        for j in range(len(l[0])):
            l[i][j] = float(l[i][j])
    return l


def transform_vector(vector):
    l = vector.split()
    for i in range(len(l)):
        l[i] = float(l[i])
    return l
