'''
Scoring functiongs will go in this file. They probably will involve sparse 
matrices
'''

import numpy as np
from model import UserInput
from scipy import ndimage


def area(user_input):
    ''' Calculates the enclosed area of a border. This is going to have to count
    the number of enclosed points. Assumes that all borders are enclosed.
    '''
    return np.sum(user_input.get_data()) #returns number of true elements


def compare_matrix(user_input, country):
    ''' Compares 2 arrays of same size and returns sum/list of different
    elements.
    '''

    diff = np.logical_xor(user_input, country)
    similar = np.logical_and(user_input, country)

    pass


def perimiter(user_input):
    ''' Calculates number of edge elements in matrix assuming that all elements
    are connected.
    '''

    data = user_input.get_data()

    eroded_image = ndimage.binary_erosion(data).astype(data.dtype)
    edge = np.logical_xor(data, eroded_image)
    perimiter = np.sum(edge)

    return perimiter


def most_similar(user_input, map_list):
    '''
    goes through a loop of countries and compares them???
    '''
    pass
