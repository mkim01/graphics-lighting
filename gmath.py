import math
from display import *


  # IMPORANT NOTE

  # Ambient light is represeneted by a color value

  # Point light sources are 2D arrays of doubles.
  #      - The fist index (LOCATION) represents the vector to the light.
  #      - The second index (COLOR) represents the color.

  # Reflection constants (ka, kd, ks) are represened as arrays of
  # doubles (red, green, blue)

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    normalize(normal)
    normalize(light[LOCATION])
    normalize(view)

    a = calculate_ambient(ambient, areflect)
    d = calculate_diffuse(light, dreflect, normal)
    s = calculate_specular(light, sreflect, view, normal)

    i = [0, 0, 0]
    i[0] = int(a[0] + d[0] + s[0])
    i[1] = int(a[1] + d[1] + s[1])
    i[2] = int(a[2] + d[2] + s[2])

    limit_color(i)

    return i

def calculate_ambient(alight, areflect):
    a = [0, 0, 0]
    a[0] = alight[0] * areflect[0]
    a[1] = alight[1] * areflect[1]
    a[2] = alight[2] * areflect[2]
    return a

def calculate_diffuse(light, dreflect, normal):
    d = [0, 0, 0]

    dProduct = dot_product(normal, light[0])

    if dProduct < 0:
        dProduct = 0

    d[0] = light[1][0] * dreflect[0] * dProduct
    d[1] = light[1][1] * dreflect[1] * dProduct
    d[2] = light[1][2] * dreflect[2] * dProduct
    return d
def calculate_specular(light, sreflect, view, normal):
    s = [0, 0, 0]
    n = [0, 0, 0]

    r = 2 * dot_product(normal, light[0])
    n[0] = (normal[0] * r) - light[0][0]
    n[1] = (normal[1] * r) - light[0][1]
    n[2] = (normal[2] * r) - light[0][2]

    r = dot_product(n, view)
    if r < 0:
        r = 0
    r = pow(r, SPECULAR_EXP)

    s[0] = light[1][0] * sreflect[0] * r
    s[1] = light[1][1] * sreflect[1] * r
    s[2] = light[1][2] * sreflect[2] * r

    return s
def limit_color(color):
    if color[RED] > 255:
        color[RED] = 255
    if color[RED] < 0:
        color[RED] = 0

    if color[GREEN] > 255:
        color[GREEN] = 255
    if color[GREEN] < 0:
        color[GREEN] = 0

    if color[BLUE] > 255:
        color[BLUE] = 255
    if color[BLUE] < 0:
        color[BLUE] = 0

#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = math.sqrt( vector[0] * vector[0] +
                           vector[1] * vector[1] +
                           vector[2] * vector[2])
    for i in range(3):
        vector[i] = vector[i] / magnitude

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
