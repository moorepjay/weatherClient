import requests
import bs4


def main():
    # todo: use www.wunderground.com/api
    print_header()

    user_zip = input("What zipcode do you want the weater for (90210)? ")

    html = get_html(user_zip)

    if AttributeError:
        print("Not a valid zip code!")
        exit()

    get_weather_from_html(html)

    # display forecast


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

    print("It's currently {} in {} and it feels like {}{}.".format(weather_conditions, location,
                                                                    weather_temp, weather_scale))


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == "__main__":
    main()
