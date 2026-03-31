# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import requests
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
MY_API_KEY = os.environ.get("MY_API_KEY")
MY_LAT = os.environ.get("MY_LAT")
MY_LON = os.environ.get("MY_LON")

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": MY_API_KEY,
    "cnt": 4,
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_data = hour_data["weather"][0]["id"]
    if condition_data < 511:
        will_rain = True

if will_rain:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg=f"Subject: Take an Umbrella \n\n It's going to rain today.\nRemember to take an ☂"
    )
    connection.close()



