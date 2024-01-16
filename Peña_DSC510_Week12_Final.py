# DSC 510
# Week 12
# Programming Assignment Week 12
# Author Miles Peña
# 11/18/2023


import requests

# Define a function to retrieve latitude and longitude using city name and state code

def get_location_city():
    app_id = "d492d3e0aa42af8a5fbf90127bd1b24d"
    city = input("Please enter city name: ")  # Request user for city
    state = input("Please enter state code: ")  # Request state code to ensure correct city is being searched
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},us&limit=1&appid={app_id}&units=imperial"

    response = requests.get(url)
    res = response.json()
    # print(res)
    lat = res[0]['lat']
    lon = res[0]['lon']
    name = res[0]['name']
    return lat, lon, name

# Define a function to retrieve latitude and longitude using zip code

def get_location_zip():
    app_id = "d492d3e0aa42af8a5fbf90127bd1b24d"
    zip_code = input("Please enter zip code: ")  # Request user for zip
    url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},us&appid={app_id}&units=imperial"

    response = requests.get(url)
    res = response.json()
    # print(res)
    lat = res['lat']
    lon = res['lon']
    name = res['name']
    return lat, lon, name


def get_weather(lat, lon):
    app_id = "d492d3e0aa42af8a5fbf90127bd1b24d"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={app_id}&units=imperial"
    response = requests.get(url)
    res = response.json()
    name = res['name']
    temp = res['main']['temp']
    feels_like = res['main']['feels_like']
    high_temp = res['main']['temp_max']
    low_temp = res['main']['temp_min']
    pressure = res['main']['pressure']
    humidity = res['main']['pressure']
    description = res['weather'][0]['description']
    print(f'The current temperature in {name} is: {temp}°F')
    print(f'Feels Like: {feels_like}°F')
    print(f'High Temp: {high_temp}°F')
    print(f'Low Temp: {low_temp}°F')
    print(f'Pressure: {pressure}hPa')
    print(f'Humidity: {humidity}%')
    print(f'Description: {description}')


def main():
    print('Welcome to the Weather Program!')  # Print welcome statement
    while True:  # Loop to allow for multiple searches
        try:
            user_answer = input("Please type city to search by city and state, zip to search by zip code or Q to quit: ")
            if user_answer.lower() == "q":
                print("Thank you for using the weather app!")
                break
            elif user_answer.lower() == "zip":
                lat, lon, name = get_location_zip()
                print(get_weather(lat, lon))
            elif user_answer.lower() == "city":
                lat, lon, name = get_location_city()
                print(get_weather(lat, lon))
            else:
                print("Please enter valid response!")
        except ValueError:
            print("Unfortunately, we cannot find the city name nor zip code.")
            break
        except requests.exceptions.HTTPError as error:  # try for errors
            print(error)
            break
        except requests.URLRequired as error:
            print(error)
            break
        except requests.ConnectionError as error:
            print(error)
            break


if __name__ == "__main__":
    main()
