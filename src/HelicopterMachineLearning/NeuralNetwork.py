'''
Created on Mar. 2, 2019

@author: Dylan Calado

This module contains the logic for the
Helicopter Game deep neural network.

To install TensorFlow and TFLearn use the following commands:
pip install tensorflow
pip install tflearn
'''
import tflearn
from tflearn.layers.core import input_data, fully_connected, dropout
from tflearn.layers.estimator import regression
#import computer vision module

learning_rate = 0.01
#X_Inputs to feed to model for training. 
data = None
test_x = None
#Y_Targets to feed to model for training. Represents ascend or descend actions.
labels = [1,0]
test_y = None


class HelicopterNeuralNetwork:
    
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate
        
    def execute_machine_learning_procedure(self):
        global data, labels, learning_rate
        
        #Generate our neural network model.
        network_model = self.build_neural_network_model()
        
        #Train our neural network model.
        #Validation_set is the % of training data used to test the performance of your model. 
        #The remaining percent of the data is used for training purpose.
        network_model.fit({'input':data}, {'targets':labels}, n_epoch=10,
                          validation_set=0.20, snapshot_step=1000, show_metric=True, run_id='helicopter_game')
        
        network_model.save('tflearndnn.model')
        
        #network_model.load('tflearndnn.model')
        
        #Here we need the data tuples from our game screen.
        #Model prediction for given input data will give the probability 
        #that the helicopter will ascend or descend.
        predicted_probability_of_action = network_model.predict()
        
        print(predicted_probability_of_action[0][0])
        
    #Builds the neural network.
    def build_neural_network_model(self):
        #Specifies the shape of our input layer data.
        network = input_data(shape = [None, 4], name='input_layer')
        
        #Creates fully connected layers.                     
        network = fully_connected(network, 10, activation='relu', name='hidden_layer')
        network = dropout(network, 0.8, name='dropout')
        network = fully_connected(network, 2, activation='softmax', name='output_layer')   
        
        #Applies a regression to the provided input.
        #Optimizer minimizes the loss function.
        network = regression(network, optimizer='adam', learning_rate=self.learning_rate, loss='categorical_crossentropy', name='estimator_layer')

        #Creates a deep neural network model.
        network_model = tflearn.DNN(network)
        
        return network_model 

if __name__ == "__main__":
    HelicopterNeuralNetwork(learning_rate).execute_machine_learning_procedure()                