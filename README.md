# API-INTEGRATION-AND-DATA-VISUALIZATION
COMPANY : CODTECH IT SOLUTION

NAME : KARINA RATHOD

INTERN ID : CT04DG2833

DOMAIN : PYTHON PROGRAMMING

DURATION : 4 WEEKS

MANTOR : NEELA SANTOSH 

requests: For sending an HTTP request to the weather API.matplotlib.pyplot: For plotting the chart. seaborn: For improved and stylish visualizations. datetime: For converting string dates from the API into datetime objects (which matplotlib understands).CITY: The city name for which you want the forecast. API_KEY: Your personal API key from OpenWeatherMap. UNITS: Set to "metric" to get temperature in Celsius.
API_URL: Constructs the full URL for the API call using the city, key, and units. Sends the request and gets the response. Converts the response to a Python dictionary using .json(). print(data) will show the entire JSON data in the console (useful for debugging). The forecast contains a "list" of weather entries, each for a 3-hour interval. For each entry: dt_txt: The date and time (like "2025-06-29 15:00:00"). temp: The temperature at that time. datetime.strptime(): Converts string to Python datetime object so it can be plotted. dates and temps lists are filled with data for the graph. plt.figure(figsize=(12, 6)): Sets the figure size (width × height). sns.lineplot(): Plots the temperature line, with circle markers and blue color. plt.title(): Adds a title to the chart. plt.xlabel() & plt.ylabel(): Label the axes. plt.xticks(rotation=45): Rotates the x-axis labels to prevent overlapping. plt.grid(True): Adds a grid to make the graph easier to read. plt.tight_layout(): Adjusts spacing so labels and titles don't get cut off. plt.show(): Displays the graph window

output :

![Image](https://github.com/user-attachments/assets/4351bb70-75e6-4d3f-984e-ae603c7d5036)
