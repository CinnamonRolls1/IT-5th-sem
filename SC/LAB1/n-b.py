import pandas as pd 
"""
def naive_bayes_predict(data_x, data_y, x):
    probabilities = [([0] * data_x.shape[1]).copy() for i in range(2)]
    p_count = 0
    n_count = 0
    for i in range(len(data_x)):
        if data_y[i] == 1:
            p_count += 1
        else:
            n_count += 1
            
        for j in range(data_x.shape[1]):
            if data_y[i] == 1 and data_x[i][j] == 1:
                probabilities[1][j] += 1
            if data_y[i] == 0 and data_x[i][j] == 1:
                probabilities[0][j] += 1
    for i in range(data_x.shape[1]):
        probabilities[1][i] /= p_count
        probabilities[0][i] /= n_count
    
    res_y = [0] * len(x)
    
    for i in range(len(x)):
        p_yes = p_count / len(data_x)
        p_no = n_count / len(data_x)
        for j in range(data_x.shape[1]):
            p_yes *= probabilities[1][j] if x[i][j] == 1 else 1 - probabilities[1][j]
            p_no *= probabilities[0][j] if x[i][j] == 1 else 1 - probabilities[0][j]
        if p_yes > p_no:
            res_y[i] = 1
"""
df=pd.read_csv('SPECT.csv')
x = df.drop(['Class'],axis=1)
y = df.iloc[:, 0] == 'Yes'
df['Class']=y
#print(df)

#for i in range(10):
