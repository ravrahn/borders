'''
Scoring functiongs will go in this file. They probably will involve sparse 
matrices
'''

import numpy as np
from model import UserInput


def area(user_input):
    ''' Calculates the enclosed area of a border. This is going to have to count
    the number of enclosed points. Assumes that all borders are enclosed.
    '''
    return np.sum(user_input) #returns number of true elements


def compare_matrix(user_input, country):
    ''' Compares 2 arrays of same size and returns sum/list of different
    elements.
    '''

    diff = np.logical_xor(user_input, country)
    similar = np.logical_and(user_input, country)

    pass


def perimiter():
    ''' Calculates number of edge elements in matrix
    '''
    pass


def most_similar(user_input, map_list):
    '''
    goes through a loop of countries and compares them???
    '''
    pass
