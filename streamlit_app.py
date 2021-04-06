### streamlit run app.py

import joblib
from sklearn.svm import SVC
import streamlit as st

#loading the pickle file for creating the web app
model = joblib.load(open("model.pkl", "rb"))

@st.cache()

def prediction(sepal_len, sepal_width, petal_len, petal_width):
    pred_val = model.predict([[sepal_len, sepal_width, petal_len, petal_width]])
    pred = round(pred_val[0], 2)
    print('pred =', pred)
    
    if pred == 0:
        out = 'setosa'
    elif pred ==1:
        out = 'versicolor'
    else:
        out = 'virginica'
    return out

# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:white;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Iris Flower Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction
    
    sepal_len = st.number_input("sepal length")
    sepal_width = st.number_input("sepal width")
    petal_len = st.number_input("petal length")
    petal_width = st.number_input("petal width")
    
    result =""
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(sepal_len, sepal_width, petal_len, petal_width)
        st.success('The flower is {}'.format(result))
        print('sepal_len =', sepal_len)
     
if __name__=='__main__': 
    main()
