App file contains the frontend code asking the user to chose the method of fetching data either from the API fetch or by uploading the CSV file 

csv_upload file conatins the code of analyzing the data and plotting the graph if user uploads the csv file 

api_url file cotains the code of analyzing the data and plotting the graph if user wants to fecth the data from the API request

propmt file conatins the sample json data and the prompt which is passed to the llm for generating the code of fectching the data and plotting the graph 

ImageUpload file conatins the code for uploading the generated graph to the coudinary.

command to run this application is 
streamlit run app.py 