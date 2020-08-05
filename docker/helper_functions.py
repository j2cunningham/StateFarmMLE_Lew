import numpy as np
import pandas as pd

def remove_dollar(x):
    '''
    Function to remove dollar sign and convert amount in parentheses to negative
    
    Input args: Dollar amount
    
    Returns: floating point dollar amount
    '''
    
    try:
        x = str(x)
        x = x.replace('$','')
        x = x.replace(',','')
        x = x.replace('(','-')
        x = x.replace(')','')
        
        return float(x)
    except:
        return np.nan

# Create a function to convert percentage to floating number
def per_float(x):
    '''Function to convert percentage input to floating point
    
    Input args: Percent
    
    Returns: floating point percentage
    '''
    
    try:
        x = str(x)
        x = x.replace('%', '')
        
        return float(x)/100
    except:
        return np.nan

def replace_missing_num_values(data,numeric_cols):
    '''
    Imputes missing values with a substitute value in a numeric columns
    
    Parameters:
    -----------
    
    data: pandas dataframe
    numeric_cols: index of numerical columns
    
    Returns:
    --------
    
    data: Imputed dataframe
      
    '''
    
    # Replace missing numerical value with a constant
    # Start with zero
    fill_constant = 0
    
    # In this case, we are filling it with a really large number
    for col in numeric_cols:
        data[col].fillna(fill_constant,inplace=True)
    
    return (data)
    
def extract_proba_to_dict(y_pred_proba):
    '''
    A helper function to extract probabilities of predictions and 
    dump it in format that is required
    
    Input args: y_pred_proba -> predicted probabilities
    
    Returns: my_list_proba -> json formated list output of Class 0 and 1 probabilities
    '''
    
    my_list_proba = []
    
    for row in y_pred_proba:
    
        imax = np.argmax(row)
        nmax = float(format(np.max(row), '.16f'))
        
        my_dict = {"class":str(imax), "probability": str(nmax)}
    
        my_list_proba.append(my_dict)
        
    return(my_list_proba)
