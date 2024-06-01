# Financial Data Analyzer

Financial Data Analyzer provides a user-friendly UI for uploading financial data, performing analytics on historical data, and generating graphical representations based on user queries. It supports both CSV uploads and API-driven data retrieval, allowing users to explore financial data conveniently.

This project leverages the Generative AI technologies specifically Langchain to streamline the process of generating code for fetching and analyzing financial data. The integration of Generative AI enhances accessibility and usability, allowing users to derive valuable insights from financial data without the need for extensive programming knowledge.

### Project Video 
[Watch the video here](https://www.loom.com/share/c2068460e2cc4a0cb2d53d2ed3d74242?sid=c5356841-c47b-40c3-9909-60c84a26daa7)

## Features

- Upload financial data via CSV file or through an open-source financial API(I have used the alpha vantage API).
- Give query what you want from the data. 
- Graphical representation of data based on user queries.
- Conversion of graphs into images and upload to Cloudinary.

## Technology Used
- Streamlit: Used for building the user interface.
- Langchain: Utilized for code generation using GPT-3.5 Turbo model.
- OpenAI GPT-3.5 Turbo: Used for generating code based on user queries.
- Cloudinary: Used for uploading and storing generated images.


## Getting Started

### Prerequisites

- Python 3.10.12
- Streamlit (for UI)
- Cloudinary account (for image upload)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/umangrati110/Financial-Data-Analyzer.git
   ```
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

2. Upload your financial data either via CSV file or through the provided API.

3. Enter queries to generate graphical representations of the data.

4. Graphs will be converted into images and automatically uploaded to Cloudinary.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
