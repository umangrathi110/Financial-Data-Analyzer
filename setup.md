## Setup Guide

### Project Overview
This project consists of several components designed to provide a user-friendly interface for analyzing financial data and generating graphical representations.

### File Structure
1. **app.py**: Contains the frontend code for the application, prompting users to choose the data fetching method (API or CSV upload).
2. **csv_upload.py**: Handles data analysis and graph plotting when the user uploads a CSV file.
3. **api_url.py**: Manages data analysis and graph plotting when the user fetches data from an API request.
4. **prompt.py**: Includes sample JSON data and prompts passed to the Langchain Language Model (LLM) for generating code to fetch data and plot graphs.
5. **ImageUpload.py**: Handles the uploading of generated graphs to Cloudinary.

### Additional Notes
- Ensure you have the necessary dependencies installed before running the application.
- Set up environment variables, including API keys or credentials, as required for fetching data from APIs and uploading graphs to Cloudinary.

