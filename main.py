# -*- coding: utf-8 -*-
"""
Use case A.I. Square Connect
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

from sklearn.metrics import r2_score
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet

import uuid



def main(file):

    # #############################################################################
    # assign a guid to each processed item
    guid = str(uuid.uuid4())
    png_file_name = guid + '.png'
    csv_file_name = guid + '.csv'


    # #############################################################################
    # read data 
    fileContent = pd.read_csv(file)
    input_df = fileContent
    n_samples, n_features = input_df .shape
    X = input_df.iloc[:,:-1].values
    
    # Add noise
    y = input_df.iloc[:,-1].values
    
    # Split data in train set and test set
    n_samples = X.shape[0]
    X_train, y_train = X[:n_samples // 2], y[:n_samples // 2]
    X_test, y_test = X[n_samples // 2:], y[n_samples // 2:]
    
    # #############################################################################
    # Lasso
    alpha = 0.1
    lasso = Lasso(alpha=alpha)
    
    y_pred_lasso = lasso.fit(X_train, y_train).predict(X_test)
    r2_score_lasso = r2_score(y_test, y_pred_lasso)
    print("r^2 on test data : %f" % r2_score_lasso)
    
    # #############################################################################
    # ElasticNet
    enet = ElasticNet(alpha=alpha, l1_ratio=0.7)
    
    y_pred_enet = enet.fit(X_train, y_train).predict(X_test)
    r2_score_enet = r2_score(y_test, y_pred_enet)
    #print(enet)
    print("r^2 on test data : %f" % r2_score_enet)
    
    m, s, _ = plt.stem(np.where(enet.coef_)[0], enet.coef_[enet.coef_ != 0],
                       markerfmt='x', label='Elastic net coefficients',
                       use_line_collection=True)
    plt.setp([m, s], color="#2ca02c")
    m, s, _ = plt.stem(np.where(lasso.coef_)[0], lasso.coef_[lasso.coef_ != 0],
                       markerfmt='x', label='Lasso coefficients',
                       use_line_collection=True)
    plt.setp([m, s], color='#ff7f0e')
    
    plt.legend(loc='best')
    plt.title("Lasso $R^2$: %.3f, Elastic Net $R^2$: %.3f"
              % (r2_score_lasso, r2_score_enet))
    plt.savefig(png_file_name)
    output_df = pd.DataFrame({'Lasso coeff': lasso.coef_,
        'Elastic coeff': enet.coef_})
    output_df.to_csv(csv_file_name, index=False)
    return guid


#%%
if __name__ == "__main__":
    # if len(sys.argv) < 2:
    #     print('missing argument filename, syntax is process [filename])')
    #     sys.exit(1)
    filename = "C:\\Users\\Spoorthi\\Downloads\\project\\project\\input.csv"
    main(filename)
    sys.exit(0)
