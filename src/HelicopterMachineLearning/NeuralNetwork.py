'''
Created on Mar. 2, 2019

@author: Dylan

This module contains the logic for the
Helicopter Game neural network.

To install TensorFlow and TFLearn use the following commands:
pip install tensorflow
pip install tflearn
'''
import numpy
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

    def neural_network_model(self):
        network = input_data(shape = [None, 4, 2], name = 'input')
                                   
        network = fully_connected(network, 10, activation='relu')   
        
        network = fully_connected(network, 10, activation='relu')  

        network = regression(network, optimizer='adam', learning_rate=self.learning_rate, loss='mean_square', name='target')

        nn_model = tflearn.DNN(network)
        
        return nn_model
    
    '''The input of our neural network could consist of an array of 4 numbers:

    Is the roof directly above of the helicopter (1-yes, 0-no)
    Is there an obstacle in front of the helicopter (1-yes, 0-no)
    Is the ground directly below the helicopter (1-yes, 0-no)
    Suggested action (1 — ascend, 0 — descend)'''
    
    def generate_training_date(self):
        training_data = []
        
        '''for x in range(self.initial_games):
            game = HelicopterGame()
            prev_observation = self.generate_observation()
            for y in range(self.goal_steps):
                action = self.generate_action()
                if done:
                    #Need to figure out what the training data structure will be still.
                    training_data.append([self.add_action_to_observation(prev_observation, action)])
                    break
                else:
                    training_data.append([self.add_action_to_observation(prev_observation, action)])
                    prev_observation = self.generate_observation()'''
        
        return training_data

    def train_model(self, training_data, model):
        X = numpy.array([i[0] for i in training_data]).reshape(-1, 4, 1)
        y = numpy.array([i[1] for i in training_data]).reshape(-1, 1)
        model.fit(X,y, n_epoch = 1, shuffle = True, run_id = self.filename)
        model.save(self.filename)
        return model
 
if __name__ == "__main__":
    HelicopterNeuralNetwork().train_model()                