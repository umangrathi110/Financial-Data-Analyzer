# Financial Data Analysis Tool

This application allows users to upload financial data either via CSV file or through an open-source financial API. The uploaded data is then used to generate graphical representations based on user queries.

## Features

- Upload financial data via CSV file or through an open-source financial API.
- Give query what you want from the data. 
- Graphical representation of data based on user queries.
- Conversion of graphs into images and upload to Cloudinary.

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
