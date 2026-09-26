# 🌤 Weather Information App

A Python-based Weather Information Application developed to retrieve and display real-time weather information using a REST API.

# 1. Project Overview

Weather information is frequently required for travel, planning, outdoor activities, transportation, and various other day-to-day applications. Modern applications can obtain real-time weather information through publicly available weather APIs.

The objective of this project is to develop a Python application that accepts a city name from the user, communicates with a weather API, retrieves real-time weather information, processes the API response, and presents the relevant information to the user.

The application uses the **OpenWeather API** to obtain weather information for the requested city.

# 2. Project Objectives

The main objectives of this project are:

- To develop a Python-based weather application.
- To understand and implement REST API integration.
- To send HTTP requests using Python.
- To retrieve real-time weather information.
- To process JSON responses received from the API.
- To extract relevant weather parameters from API responses.
- To implement input validation.
- To handle API and connection errors.
- To securely manage API credentials.
- To understand the practical use of external APIs in Python applications.

# 3. Problem Statement

Users often need quick access to current weather information for a particular location.

The problem addressed by this project is to develop a simple application where a user can enter a city name and retrieve its current weather information without manually visiting a weather website.

The application communicates directly with a weather service through a REST API and processes the returned data automatically.

# 4. Proposed Solution

The proposed solution is a Python application that performs the following operations:

1. Accepts a city name from the user.
2. Creates a request to the OpenWeather API.
3. Sends the request using the Python `Requests` library.
4. Receives the response from the API.
5. Converts the response into JSON data.
6. Extracts the required weather information.
7. Displays the information to the user.
8. Handles invalid requests and API errors appropriately.

# 5. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Requests | Sending HTTP requests |
| OpenWeather API | Retrieving real-time weather data |
| JSON | Processing API responses |
| python-dotenv | Managing environment variables |
| Tkinter | Graphical user interface, where applicable |
| Visual Studio Code | Development environment |
| Git | Version control |
| GitHub | Source code management and documentation |

# 6. API Used

## OpenWeather API

The application uses the OpenWeather REST API to retrieve current weather information.

The API accepts parameters such as:

- City name
- API key
- Unit of measurement

The application requests temperature values in Celsius by using metric units.

Example API request structure:
https://api.openweathermap.org/data/2.5/weather
