# Stress-Free Weekend Trip Planner

This is a simple web application that helps you plan a stress-free weekend trip. It uses Google's Gemini AI to generate a personalized itinerary based on your preferences and real-time conditions.

## Features

-   Generates a detailed 2-day, 1-night weekend trip plan.
-   Personalizes the plan based on your budget, destination, activities, dining preferences, and accommodation type.
-   Considers real-time conditions, including the current weather at your destination.
-   Provides a budget-friendly and stress-free itinerary with backup options.
-   Includes a tabular format for the estimated budget.

## File Breakdown

This project is composed of the following files:

-   **`weekend.py`**: The main application file. It uses Flask to create a web server.
    -   It has a single route (`/`) that handles both GET requests (to display the form) and POST requests (to generate and display the trip plan).
    -   The `generate_trip_plan` function constructs a detailed prompt for the Gemini AI model, incorporating user input and weather data.
    -   It uses the `python-dotenv` library to load the `GEMINI_API_KEY` from a `.env` file.

-   **`openweather.py`**: A simple module that contains the `get_weather_data` function.
    -   This function takes a city name as input and returns the current temperature in Celsius.
    -   It makes a request to the OpenWeatherMap API.
    -   **Note:** The API key is currently hardcoded in this file. For production use, it's recommended to move this to an environment variable.

-   **`requirements.txt`**: This file lists all the Python dependencies required for the project. The key dependencies are:
    -   `Flask`: For the web framework.
    -   `google-generativeai`: To interact with the Gemini AI.
    -   `requests`: To make HTTP requests to the OpenWeatherMap API.
    -   `python-dotenv`: To manage environment variables.

-   **`templates/`**: This directory contains the HTML templates used by Flask.
    -   **`index.html`**: The main page of the application. It contains a form for users to input their trip preferences.
    -   **`result.html`**: This page displays the generated trip plan. It uses the `marked.js` library to render the Markdown output from the Gemini AI and `DOMPurify` to sanitize the HTML.
    -   **`error.html`**: A simple page to display an error message if the trip plan generation fails.
    -   **`decision_tree_results.html`**: This file appears to be an unused remnant of a previous feature. It's a template to display the results of a decision tree model, but it is not currently used anywhere in the application.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/chinmayc0707/travel_planner.git
    cd travel_planner
    ```

2.  **Create and activate the virtual environment:**

    First, create the virtual environment:
    ```bash
    python -m venv .venv
    ```

    Then, activate it. The command differs depending on your operating system.

    -   **On macOS and Linux:**
        ```bash
        source venv/bin/activate
        ```

    -   **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a file named `.env` in the root of the project and add your Google Gemini API key:
    ```
    GEMINI_API_KEY=your_gemini_api_key
    ```
    You can get a Gemini API key from [Google AI Studio](https://aistudio.google.com/).

5.  **OpenWeatherMap API Key:**
    The OpenWeatherMap API key is currently hardcoded in `openweather.py`. It is recommended to replace it with your own key. You can get a free API key from [OpenWeatherMap](https://openweathermap.org/appid).

## Usage

To run the application, execute the following command:

```bash
python weekend.py
```

Then, open your web browser and go to `http://127.0.0.1:5000`.

## Technologies Used

-   **Backend:** Python, Flask
-   **AI Model:** Google Gemini
-   **APIs:** OpenWeatherMap API
-   **Frontend:** HTML, CSS, JavaScript, marked.js, DOMPurify
-   **Dependencies:** See `requirements.txt`
