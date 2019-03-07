'''
Created on Mar. 2, 2019

@author: Dylan

This module contains the logic for the
Helicopter Game neural network.

To install TensorFlow and TFLearn use the following commands:
pip install tensorflow
pip install tflearn
'''
import numpy as np
import tflearn
from tflearn.layers.core import input_data, fully_connected, dropout
from tflearn.layers.estimator import regression
import random
#import whatever computer vision will output for us

initial_games = 1000 
goal_steps = 200
learning_rate = 1e-2
filename = 'helicopter_nn.tflearn'

class HelicopterNeuralNetwork:
    
    def __init__(self, initial_games, test_games, goal_steps, learning_rate, filename):
        self.initial_games = initial_games
        self.test_games = test_games
        self.goal_steps = goal_steps
        self.learning_rate = learning_rate
        self.filename = filename

    #Builds the neural network.
    def build_neural_network_model(self):
        #Specifies the shape of our input data.
        network = input_data(shape = [None, 4], name = 'input_shape')
        #Creates fully connected layers.                  
        network = fully_connected(network, 4, name = 'input_layer')   
        network = fully_connected(network, 10, name = 'hidden_layer')
        network = fully_connected(network, 1, name='output_layer')   
        network = regression(network, optimizer='adam', learning_rate=self.learning_rate, loss='mean_square', name='target')

        #Creates a deep neural network model.
        network_model = tflearn.DNN(network)
        
        return network_model
    
    '''The input of our neural network could consist of an array of 4 numbers:

    Is the roof directly above of the helicopter (1-yes, 0-no)
    Is there an obstacle in front of the helicopter (1-yes, 0-no)
    Is the ground directly below the helicopter (1-yes, 0-no)
    Suggested action (1 — ascend, 0 — descend)'''
    

    def train_model(self, training_data, model):
        model.fit()
 
if __name__ == "__main__":
    HelicopterNeuralNetwork().train_model()                