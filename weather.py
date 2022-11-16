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

    date = datetime.fromisoformat(iso_string)
    format = date.strftime("%A %d %B %Y")

    return format

print(convert_date)

    # """Converts and ISO formatted date into a human readable format.

    # Args:
    #     iso_string: An ISO date string..
    # Returns:
    #     A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    # """
    # pass


def convert_f_to_c(temp_in_fahrenheit):

    celsius = round((float(temp_in_fahrenheit) - 32) * (5 / 9), 1)

    return celsius

print(convert_f_to_c)

    # """Converts an temperature from farenheit to celcius.
    
    # Args:
    #     temp_in_farenheit: float representing a temperature.
    # Returns:
    #     A float representing a temperature in degrees celcius, rounded to 1dp.
    # """
    # pass


def calculate_mean(weather_data):

    count = 0

    for numbers in weather_data:
        count += float(numbers)
    
    mean = float(count / len(weather_data))

    return mean

print(calculate_mean)

    
    # """Calculates the mean value from a list of numbers.

    # Args:
    #     weather_data: a list of numbers.
    # Returns:
    #     A float representing the mean value.
    # """
    # pass


def load_data_from_csv(csv_file):

    with open(csv_file) as data_file:
        reader = csv.reader(data_file)
        next(reader)

        data = []

        for line in reader:
            if not (line):
                continue
            data.append(line[0])
            data.append(int(line[1]))
            data.append(int(line[2]))
        
        split_lists = [data[x:x+3] for x in range(0, len(data), 3)]

        # I found above code online. I'm sure there is a simpler way to do this.
        
        return split_lists


print(load_data_from_csv)
    
    # """Reads a csv file and stores the data in a list.

    # Args:
    #     csv_file: a string representing the file path to a csv file.
    # Returns:
    #     A list of lists, where each sublist is a (non-empty) line in the csv file.
    # """
    # pass


def find_min(weather_data):

    temp = []

    for item in weather_data:
        temp.append(float(item))
    
    if temp == []:
        return ()

    min_temp = min(temp)
    
    for i in range(len(temp)):
        if temp[i] == min_temp:
            position = i

    return (min_temp, position)
    
print(find_min)

    # """Calculates the minimum value in a list of numbers.

    # Args:
    #     weather_data: A list of numbers.
    # Returns:
    #     The minium value and it's position in the list.
    # """
    # pass


def find_max(weather_data):

    temp = []

    for item in weather_data:
        temp.append(float(item))
    
    if temp == []:
        return ()

    max_temp = max(temp)
    
    for i in range(len(temp)):
        if temp[i] == max_temp:
            position = i

    return (max_temp, position)
    
print(find_max)

    # """Calculates the maximum value in a list of numbers.

    # Args:
    #     weather_data: A list of numbers.
    # Returns:
    #     The maximum value and it's position in the list.
    # """
    # pass


def generate_summary(weather_data):

    min_temp = [item[1] for item in weather_data]
    c_min_temp = convert_f_to_c(min(min_temp))
    max_temp = [item[2] for item in weather_data]
    c_max_temp = convert_f_to_c(max(max_temp))
    avg_min = calculate_mean(min_temp)
    c_avg_min = convert_f_to_c(avg_min)
    avg_max = calculate_mean(max_temp)
    c_avg_max = convert_f_to_c(avg_max)

    for i in weather_data:
        if i[1] == min(min_temp):
            date_min = i[0]
    
    for j in weather_data:
        if j[2] == max(max_temp):
            date_max = j[0]


    return f"{len(weather_data)} Day Overview\n  The lowest temperature will be {format_temperature(c_min_temp)}, and will occur on {convert_date(date_min)}.\n  The highest temperature will be {format_temperature(c_max_temp)}, and will occur on {convert_date(date_max)}.\n  The average low this week is {format_temperature(c_avg_min)}.\n  The average high this week is {format_temperature(c_avg_max)}.\n"

print(generate_summary)

    # """Outputs a summary for the given weather data.

    # Args:
    #     weather_data: A list of lists, where each sublist represents a day of weather data.
    # Returns:
    #     A string containing the summary information.
    # """
    # pass

    # print(generate_summary)


def generate_daily_summary(weather_data):

    summary_list = []
    daily_summary = []

    for row in weather_data:
        date = convert_date(row[0])
        min_temp = format_temperature(convert_f_to_c(row[1]))
        max_temp = format_temperature(convert_f_to_c(row[2]))
        summary_list.append([date, min_temp, max_temp])
    
    for item in summary_list:
        summary = f'---- {item[0]} ----\n  Minimum Temperature: {item[1]}\n  Maximum Temperature: {item[2]}\n\n'
        daily_summary.append(summary)

    result = ''.join(daily_summary)

    return result

    # """Outputs a daily summary for the given weather data.

    # Args:
    #     weather_data: A list of lists, where each sublist represents a day of weather data.
    # Returns:
    #     A string containing the summary information.
    # """

print(generate_daily_summary)
