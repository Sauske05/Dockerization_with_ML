import sys
print(sys.executable)
import pickle
def loading_pickle_model():
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = loading_pickle_model()
prediction = model.predict([[1.1]])
print(f'Prediction made is: {prediction[-1][-1]}')