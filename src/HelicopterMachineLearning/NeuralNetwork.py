'''
Created on Mar. 2, 2019

@author: Dylan Calado

This module contains the logic for the
Helicopter Game neural network.

To install TensorFlow and TFLearn use the following commands:
pip install tensorflow
pip install tflearn
'''
import numpy as np
import tflearn
from tflearn.layers.core import input_data, fully_connected
from tflearn.layers.estimator import regression

#import whatever computer vision will output for us
learning_rate = 1e-2

#X_Inputs to feed to model for training. 
#This will be a numpy array generated via Computer Vision.
data = None

#Y_Targets to feed to model for training. Represents ascend or descend actions.
labels = [1,0]

class HelicopterNeuralNetwork:
    
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate

    #Sets the numpy array generated from CV to a global variable.
    def set_data_from_CV(self, cv_data):
        global data
        data = cv_data
        
    def execute_machine_learning_procedure(self):
        global data, labels
        #set_data_from_CV(data_from_CV)
        
        #Generate our neural network model.
        network_model = self.build_neural_network_model()
        
        #Train our neural network model.
        network_model.fit(data, labels, show_metric=True)
        
        #Here we need data from our game screen (as numpy array)...
        screenshot_data = [[1,0,0,1,0], [1,0,0,1,0]]#...
        
        #Model prediction for given input data.
        predicted_probability_of_action = network_model.predict(screenshot_data)
        
        print(predicted_probability_of_action[0][0])
        
    #Builds the neural network.
    def build_neural_network_model(self):
        #Specifies the shape of our input data.
        network = input_data(shape = [None, 4], name='input_shape')
        #Creates fully connected layers.                  
        network = fully_connected(network, 10, name='input_layer')   
        network = fully_connected(network, 10, name='hidden_layer')
        network = fully_connected(network, 2, name='output_layer')   
        
        #Applies a regression to the provided input.
        #Optimizer minimizes the loss function.
        network = regression(network, optimizer='adam', learning_rate=self.learning_rate, loss='mean_square', name='estimator_layer')

        #Creates a deep neural network model.
        network_model = tflearn.DNN(network)
        
        return network_model 
    
    '''The input of our neural network could consist of an array of n numbers:
    Survived? (1-yes, 0-no)
    Is the roof directly above of the helicopter (1-yes, 0-no)
    Is there an obstacle in front of the helicopter (1-yes, 0-no)
    Is the ground directly below the helicopter (1-yes, 0-no)
    Suggested action (1-ascend, 0-descend)'''

 
if __name__ == "__main__":
    HelicopterNeuralNetwork().execute_machine_learning_procedure()                