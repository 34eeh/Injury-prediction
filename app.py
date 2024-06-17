import pickle 
import streamlit as st


st.set_page_config(page_title="Injury Prediction",layout="wide", initial_sidebar_state="expanded")

# st.set_page_config(page_title="Career Recommender", page_icon="static/img/icon4.png",layout="wide", initial_sidebar_state="expanded")
st.title(" Injury Prediction")
# Load custom CSS
# def load_css(file_name):
#     with open(file_name) as f:
        
#         st.markdown(f'', unsafe_allow_html=True)

# load_css('static/style.css')


# loading the pre-trained model
pickle_in = open('model.pkl', 'rb')
classifier = pickle.load(pickle_in)

@st.cache()
# defining the function which will make the prediction using the data which the user inputs

def prediction(Player_Age, Player_Weight, Player_Height, Previous_Injuries,Training_Intensity, Recovery_Time, BMI_Classification_Normal,BMI_Classification_Obesity_I, BMI_Classification_Obesity_II,BMI_Classification_Overweight, BMI_Classification_Underweight):
    Player_Age=Player_Age
    Player_Weight=Player_Weight
    Player_Height=Player_Height
    Previous_Injuries=Previous_Injuries
    Training_Intensity=Training_Intensity
    Recovery_Time=Recovery_Time
    BMI_Classification_Normal=BMI_Classification_Normal
    BMI_Classification_Obesity_I=BMI_Classification_Obesity_I
    BMI_Classification_Obesity_II=BMI_Classification_Obesity_II
    BMI_Classification_Overweight=BMI_Classification_Overweight
    BMI_Classification_Underweight=BMI_Classification_Underweight

    # Make recommendations
    prediction = classifier.predict([[Player_Age, Player_Weight, Player_Height, Previous_Injuries,Training_Intensity, Recovery_Time, BMI_Classification_Normal,BMI_Classification_Obesity_I, BMI_Classification_Obesity_II,BMI_Classification_Overweight, BMI_Classification_Underweight]])
    if prediction == 0:
        
        pred = "Unlikely"
    elif prediction==1:
        pred='Likely'
    
    return pred


                
# this is the main function in which we define our webpage
def main():
    # front end elements of the web page
    html_temp = """ 
    
    
     Injury Prediction WebAPP 
     
    
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)
    
    # following lines create boxes in which user can enter data required to make prediction

    Player_Age=st.number_input("Player_Age")
    Player_Weight=st.number_input("Player_Weight")
    Player_Height=st.number_input("Player_Height")
    Previous_Injuries=st.number_input("Previous_Injuries")
    Training_Intensity=st.number_input("Training_Intensity")
    Recovery_Time=st.number_input("Recovery_Time")
    BMI_Classification_Normal=st.number_input("BMI_Classification_Normal")
    BMI_Classification_Obesity_I=st.number_input("BMI_Classification_Obesity_I")
    BMI_Classification_Obesity_II=st.number_input("BMI_Classification_Obesity_II")
    BMI_Classification_Overweight=st.number_input("BMI_Classification_Overweight")
    BMI_Classification_Underweight=st.number_input("BMI_Classification_Underweight")


   
    result=""
    print(result)
    # when 'recommend' is clicked, make the recommendation and store it
    if st.button("Recommend"):
        result = prediction(Player_Age, Player_Weight, Player_Height, Previous_Injuries,Training_Intensity, Recovery_Time, BMI_Classification_Normal,BMI_Classification_Obesity_I, BMI_Classification_Obesity_II,BMI_Classification_Overweight, BMI_Classification_Underweight)
        
        
        st.success('Injury Likelihood?  {}'.format(result))
        print(result)
if __name__ == '__main__':
    main()