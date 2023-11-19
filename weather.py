import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):

    # """Takes a temperature and returns it in string format with the degrees
    #     and celcius symbols.

    # Args:
    #     temp: A string representing a temperature.
    # Returns:
    #     A string contain the temperature and "degrees celcius."
    # """

    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):

    # """Converts and ISO formatted date into a human readable format.

    # Args:
    #     iso_string: An ISO date string..
    # Returns:
    #     A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    # """

    date = datetime.fromisoformat(iso_string)
    formatted_date = date.strftime("%A %d %B %Y")

    return formatted_date


def convert_f_to_c(temp_in_fahrenheit):

    # """Converts an temperature from farenheit to celcius.

    # Args:
    #     temp_in_farenheit: float representing a temperature.
    # Returns:
    #     A float representing a temperature in degrees celcius, rounded to 1dp.
    # """

    celsius = round((float(temp_in_fahrenheit) - 32) * (5 / 9), 1)

    return celsius


def calculate_mean(weather_data):

    # """Calculates the mean value from a list of numbers.

    # Args:
    #     weather_data: a list of numbers.
    # Returns:
    #     A float representing the mean value.
    # """

    count = 0

    for numbers in weather_data:
        count += float(numbers)

    mean = float(count / len(weather_data))

    return mean


def load_data_from_csv(csv_file):

    # """Reads a csv file and stores the data in a list.

    # Args:
    #     csv_file: a string representing the file path to a csv file.
    # Returns:
    #     A list of lists, where each sublist is a (non-empty) line in the csv file.
    # """

    with open(csv_file) as data_file:
        reader = csv.reader(data_file)
        next(reader)

        data = []

        for line in reader:
            if not (line):
                continue
            data.append([line[0], int(line[1]), int(line[2])])

        return data


def find_min(weather_data):

    # """Calculates the minimum value in a list of numbers.

    # Args:
    #     weather_data: A list of numbers.
    # Returns:
    #     The minium value and it's position in the list.
    # """

    temp = [float(item) for item in weather_data]

    if temp == []:
        return ()

    min_temp = min(temp)

    for i in range(len(temp)):
        if temp[i] == min_temp:
            position = i

    return (min_temp, position)


def find_max(weather_data):

    # """Calculates the maximum value in a list of numbers.

    # Args:
    #     weather_data: A list of numbers.
    # Returns:
    #     The maximum value and it's position in the list.
    # """

    temp = [float(item) for item in weather_data]

    if temp == []:
        return ()

    max_temp = max(temp)

    for i in range(len(temp)):
        if temp[i] == max_temp:
            position = i

    return (max_temp, position)


def generate_summary(weather_data):

    # """Outputs a summary for the given weather data.

    # Args:
    #     weather_data: A list of lists, where each sublist represents a day of weather data.
    # Returns:
    #     A string containing the summary information.
    # """

    min_temp_list = [item[1] for item in weather_data]
    max_temp_list = [item[2] for item in weather_data]
    min_temp = format_temperature(convert_f_to_c(min(min_temp_list)))
    max_temp = format_temperature(convert_f_to_c(max(max_temp_list)))
    avg_min = format_temperature(convert_f_to_c(calculate_mean(min_temp_list)))
    avg_max = format_temperature(convert_f_to_c(calculate_mean(max_temp_list)))

    for i in weather_data:
        if i[1] == min(min_temp_list):
            date_min = convert_date(i[0])

    for j in weather_data:
        if j[2] == max(max_temp_list):
            date_max = convert_date(j[0])

    return (f"{len(weather_data)} Day Overview\n"
            f"  The lowest temperature will be {min_temp}, and will occur on {date_min}.\n"
            f"  The highest temperature will be {max_temp}, and will occur on {date_max}.\n"
            f"  The average low this week is {avg_min}.\n"
            f"  The average high this week is {avg_max}.\n")


def generate_daily_summary(weather_data):

    # """Outputs a daily summary for the given weather data.

    # Args:
    #     weather_data: A list of lists, where each sublist represents a day of weather data.
    # Returns:
    #     A string containing the summary information.
    # """

    summary_list = []

    for row in weather_data:
        date = convert_date(row[0])
        min_temp = format_temperature(convert_f_to_c(row[1]))
        max_temp = format_temperature(convert_f_to_c(row[2]))
        summary_list.append([date, min_temp, max_temp])

    summary = ""

    for item in summary_list:
        summary += (f"---- {item[0]} ----\n"  
                   f"  Minimum Temperature: {item[1]}\n"
                   f"  Maximum Temperature: {item[2]}\n\n")

    return summary