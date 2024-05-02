from langchain.prompts import PromptTemplate

input_json = {
    "Meta Data": {
        "1. Information": "Monthly Prices (open, high, low, close) and Volumes",
        "2. Symbol": "IBM",
        "3. Last Refreshed": "2024-05-01",
        "4. Time Zone": "US/Eastern"
    },
    "Monthly Time Series": {
        "2024-05-01": {
            "1. open": "165.6900",
            "2. high": "166.2700",
            "3. low": "164.3000",
            "4. close": "164.4300",
            "5. volume": "4030960"
        },
        "2024-04-30": {
            "1. open": "190.0000",
            "2. high": "193.2800",
            "3. low": "165.2605",
            "4. close": "166.2000",
            "5. volume": "98297181"
        },
        "2024-03-28": {
            "1. open": "185.4900",
            "2. high": "199.1800",
            "3. low": "185.1800",
            "4. close": "190.9600",
            "5. volume": "99921776"
        },
        "2024-02-29": {
            "1. open": "183.6300",
            "2. high": "188.9500",
            "3. low": "178.7500",
            "4. close": "185.0300",
            "5. volume": "88679550"
        }
        }
}


prompt_template = """You are an intelligent chatbot that learns and comphrehends the information provided. You learn quickly. You do not have a mind of your own. 

1. Understand the sample data provided in the json. That data provided in the input json are the extent of your knowledge. 
2. As per requested query you have to give the code to fecth the data from the input_json data.
3. Return a function with the name output which is accepting the json data whose sample is given to you that function is able to fetch the data according to the user query and also add the code to plot the graph (type of graph is also given to you) of the fetched data along with add the code save the graph with the name api_graph.png in the current folder and function is able to return the full url of this graph file in the string format. The input given to the function is in the json format.
4. if you cannot find any information from the existing json to a question asked , it becomes irrelevant and return , " I don't know! " instead of url of image.
5. You have to give only the code of the function without any comments in it
6. In case the user asks a question that you do not have an answer to, do not generate your own answer, instead return " I don't know! "

INPUT_JSON Format 
Sample Data: {input_json}

Query : {question}

chart : {chart}

Remember that the input_json given to you is the sample data but the actual data is very large so give the output accordingly and only give the function code without any comments. The orginal data will follow the same schema as the sample data.
U
Make xticks vertical and make it according to user query and make sure its font clearly visible in the image.

Follow the examples below,

Example #1

Hint: Find the difference between any price  Open, close, High and low then substract from one to another and calcuate the result.
Hint: Determine the difference between Open and Close then Substract Open-Close.

Hint: Determine the difference between High and Close then substract High-Close.


Finally, remember that if you cannot find any information from the exisisting json to a question asked , it becomes irrelevant and return , " I don't know! "
"""

PROMPT = PromptTemplate(
    input_variables=["context", "question", "chart"], 
    template=prompt_template
)