# Weather Data ETL Pipeline

## Project Overview

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using real-time weather data from the OpenWeather API.

The pipeline uses Python to extract weather information for three cities — Abuja, Lagos, and Port Harcourt — transform the raw API response into a clean and structured dataset using Pandas, and load the processed data into a CSV file for analysis.

The project also performs basic analysis to compare temperatures, identify the city with the highest humidity, and compare weather conditions across the three cities.

## Data Source

The weather data was collected using the OpenWeather API.

The API provides real-time weather information, including temperature, humidity, weather conditions, wind speed, and date/time.

### Cities Analyzed

- Abuja, Nigeria
- Lagos, Nigeria
- Port Harcourt, Nigeria

The data was extracted directly from the OpenWeather API using Python and the `requests` library.

## ETL Process

The project follows three main stages:

### 1. Extract

Weather data was extracted from the OpenWeather API using Python and the `requests` library.

The pipeline collected the following information for Abuja, Lagos, and Port Harcourt:

- City Name
- Temperature
- Humidity
- Weather Condition
- Wind Speed
- Date and Time

### 2. Transform

The extracted API response was converted into a structured format using Pandas.

The transformation process included:

- Selecting the required weather fields
- Organizing the data into a Pandas DataFrame
- Converting the API timestamp into a readable date and time format
- Checking data types
- Checking for missing values
- Checking for duplicate records

The final dataset contained 3 rows and 6 columns with no missing values or duplicate records.

### 3. Load

The transformed dataset was saved as a CSV file named `weather_data.csv`.

The saved CSV file was then loaded back into Python to confirm that the data had been stored successfully and was ready for analysis.

## Tools Used

- **Python** 
- **Pandas** 
- **Requests** 
- **OpenWeather API** 
- **VS Code** 
- **CSV**  
- **GitHub** 

## Steps Taken

1. Created an OpenWeather API account and generated an API key.
2. Set up a Python project in VS Code.
3. Installed and imported the required Python libraries.
4. Connected Python to the OpenWeather API using the `requests` library.
5. Extracted real-time weather data for Abuja, Lagos, and Port Harcourt.
6. Selected the required weather fields from the API response.
7. Converted the extracted data into a Pandas DataFrame.
8. Converted the API timestamp into a readable date and time format.
9. Checked the dataset for missing values, duplicate records, and data types.
10. Saved the transformed dataset as `weather_data.csv`.
11. Loaded the CSV file back into Python to verify that the data was stored successfully.
12. Performed basic analysis to compare temperatures, identify the city with the highest humidity, and compare weather conditions.

## Key Findings

The analysis of the collected weather data produced the following findings:

- **Lagos recorded the highest temperature** at 27.41°C.
- **Abuja recorded a temperature of 26.75°C.**
- **Port Harcourt recorded the lowest temperature** at 23.27°C.
- **Port Harcourt had the highest humidity** at 95%.
- **Abuja and Port Harcourt recorded rainy conditions**, while Lagos recorded cloudy conditions.

