'''
This module is a collection of common used functions in motor
control design.
'''
import math

# common used constant
PI = math.pi

def rpm2rad(rpm = 0):
    '''
    rpm to rad/s convertion.
    '''
    return rpm/60*2*math.pi

def rad2rpm(rad = 0):
    '''
    rpm to rad/s convertion.
    '''
    return rad*60/2/math.pi    












if __name__ == '__main__':
    pass