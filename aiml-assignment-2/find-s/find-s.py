import pandas as pd
import numpy as np

data = pd.read_csv('dataset.csv')

concepts = np.array(data)[:,:-1]
targets = np.array(data)[:,-1]

print("Concepts \n{}".format(concepts))
print("Targets \n{}".format(targets))

def train(con, tar):
    # initialize the specific hypothesis to the first positive instance
    for i in range(len(tar)):
        if tar[i] == 'yes':
            specific_hypothesis = con[i].copy()
            print("Initial Specific Hypothesis : {}\n".format(specific_hypothesis))
            break

    for j in range(len(con)):
        curr_instance = con[j]
        print("Instance - {} : {}".format(j,curr_instance))
        if tar[j] == 'yes':
            for attribute in range(len(specific_hypothesis)):
                if curr_instance[attribute] != specific_hypothesis[attribute]:
                    specific_hypothesis[attribute] = '?'
                else:
                    pass
            print("Specific Hypothesis : {}\n".format(specific_hypothesis))
        else:
            print("Negative instance\n")
    
    return specific_hypothesis

def is_instance_accepted(hypothesis, instance):
    for attribute in range(len(hypothesis)):
        if hypothesis[attribute] != '?' and hypothesis[attribute] != instance[attribute]:
            return False
    
    return True

final_hypothesis = train(concepts, targets)
print("Final specific hypothesis : ",final_hypothesis)

new_instance = input("Enter a new instance to see if it matches the hypothesis : ").split(',')
print("Entered instance : ",new_instance)

if is_instance_accepted(final_hypothesis, new_instance):
    print("The instance is accepted")
else:
    print("The instance is not accepted")