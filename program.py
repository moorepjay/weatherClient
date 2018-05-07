import collections

import requests
import bs4

WeatherReport = collections.namedtuple("WeatherReport",
                                       "cond, temp, scale, location")


def main():
    # todo: use www.wunderground.com/api
    print_header()

    user_zip = input("What zipcode do you want the weater for (90210)? ")
    html = get_html(user_zip)
    report = get_weather_from_html(html)

    print("The temp in {} is {}{}. Conditions: {}".format(report.location,
                                                          report.temp,
                                                          report.scale,
                                                          report.cond))


def print_header():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("      WEATHER APP")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()


def get_html(zipcode):
    url = "https://www.wunderground.com/weather-forecast/{}".format(zipcode)
    response = requests.get(url)

    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    location = soup.find(class_="region-content-header").find("h1").get_text().strip()
    weather_conditions = soup.find(class_="condition-icon").get_text()
    weather_temp = soup.find(class_="feels-like").find(class_="temp").get_text()
    weather_scale = soup.find(class_="wu-unit-temperature").find(class_="wu-label").get_text()

    location = cleanup_text(location)
    weather_conditions = cleanup_text(weather_conditions)
    weather_temp = cleanup_text(weather_temp)
    weather_scale = cleanup_text(weather_scale)

    report = WeatherReport(cond=weather_conditions, temp=weather_temp, scale=weather_scale, location=location)
    return report


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == "__main__":
    main()
