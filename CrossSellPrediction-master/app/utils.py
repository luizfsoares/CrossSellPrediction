import pandas as pd
import numpy as np
#import pickle
import scipy.stats as stats

# path = '/app/model1.pkl'

# with open(path, 'rb') as file_:
#    model = pickle.load(file_)


def preprocess(data):
    '''
    Transform data to valid input

    Parameters
    ----------
    data : [type]
        [description]
    '''
    a1 = data['longitude']
    a2 = data['latitude']
    a3 = data['hma']
    a4 = data['totalR']
    a5 = data['totalB']
    a6 = data['population']
    a7 = data['households']
    a8 = data['medianI']
    a9 = data['mhv']
    a10 = data['ocean_p']
    a11 = data['status_age']
    final_features = pd.DataFrame({'a1': a1, 'a2': a2, 'a3': a3,
                                   'a4': a4, 'a5': a5, 'a6': a6,
                                   'a7': a7, 'a8': a8, 'a9': a9,
                                   'a10': a10, 'a11': a11}, index=[0])
    return final_features


def predict(final_features):

    final_features = stats.zscore(
        final_features.values.astype(np.double), axis=1)
    # prediction = model.predict(final_features)[0]
    prediction = "Modelo em Construção"

    return prediction
