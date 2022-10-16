import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')

    # Getting user input for the city he/she wants to filter with:
    city = ""

    while city not in CITY_DATA.keys():
        city = input(f"Please Enter A City Name:\n ( {' - '.join(CITY_DATA.keys())} )\n").lower()

        # Checking if user input exists in the data dict
        if city in CITY_DATA.keys():
            print(f'The City You Entered Is {city}')
        else:
            print("You entered an invalid entry please, try again!")

    # Getting user input for the month he/she wants to filter with:
    month = ""

    months = ["all", "january", "february", "march", "april", "may", "june"]

    while month not in months:
        month = input(f"Please choose a month to filter by:\n( {' - '.join(months)} )\n").lower()

        # Checking if user input exists in the data dict:
        if month in months:
            print(f"The Month You Choose is {month} ")
        else:
            print("Please try again with a valid entry!")

    # Getting user input for the day of week he/she wants to filer with:
    day = ""

    week_days = ["all", "saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]

    while day not in week_days:
        day = input(f"Please enter a day to filter by:\n( {' - '.join(week_days)} )\n").lower()

        # Checking if user input exists in the data dict:
        if day in week_days:
            print(f"The day you choose is {day}")
        else:
            print("Please try again with a valid entry")

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Passing the csv file for pandas to read:
    df = pd.read_csv(CITY_DATA[city])

    # Converting to date-time format:
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Creating new column for month/week-days:
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Months filter:
    if month != 'all':
        # Indexing with the month input to get the month:
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Creating a new DataFrame with filtered month:
        df = df[df['month'] == month]

    # Weeks-day filter:
    if day != 'all':
        # Creating a new DataFrame with filtered dy:
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Getting the most common month:
    most_common_month = df["month"].mode()[0]
    print(f"The Most Common Month: {most_common_month}")

    # Getting the most common day of the week:
    most_common_day = df["day_of_week"].mode()[0]
    print(f"The Most Common day: {most_common_day}")

    # Getting the most common hour:
    df["hour"] = df["Start Time"].dt.hour

    most_common_hour = df["hour"].mode()[0]
    print(f"The Most Common Hour is: {most_common_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Getting the most common start station:
    most_common_start_station = df["Start Station"].mode()[0]
    print(f"The Most Common Start Station Is: {most_common_start_station}")

    # Getting the most common end station:
    most_common_end_station = df["End Station"].mode()[0]
    print(f"The Most Common End Station Is: {most_common_end_station}")

    # Getting the most common combined start & end station => Trip:
    df["Start + End"] = df["Start Station"] + " to " + df["End Station"]
    most_common_trip = df["Start + End"].mode()[0]
    print(f"The Most Common Trip is: {most_common_trip}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Calculating total time traveled:
    total_travel_time = int(df["Trip Duration"].sum())
    total_travel_time_hours = round(total_travel_time / 120)
    total_travel_time_mints = round(total_travel_time % 60)
    print(f"The Total Travel Time is: {total_travel_time_hours} Hours, {total_travel_time_mints} Minutes")

    # Calculating total time traveled mean:
    mean_travel_time = round(int(df["Trip Duration"].mean()))
    mean_travel_time_hours = round(mean_travel_time / 120)
    print(f"The Mean Travel Time is: {mean_travel_time_hours} Hours")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Getting user types:
    count_type_user = df["User Type"].value_counts()
    print(f"Users Types are: {count_type_user} ")

    # Getting users gender:
    try:
        gender_count = df['Gender'].value_counts()
        print(f"The Type Of Users By Gender is: {gender_count}")
    except:
        print("The Data Filter That You Choose Doesn't Have a Gender Columns")

    # Getting users earliest year, most recent and most common year of birth:
    try:
        earliest_year_of_birth = int(df["Birth Year"]).min()
        most_recent_year_of_birth = int(df["Birth Year"]).max()
        most_common_year_of_birth = int(df["Birth Year"]).mode()[0]
        print(
            f"The Earliest Year Of Birth Is: {earliest_year_of_birth}"
            f"The Most Recent Year Of Birth Is: {most_recent_year_of_birth}"
            f"The Most Common Year Of Birth Is: {most_common_year_of_birth}"
        )
    except:
        print("The Data Filter That You Choose Doesn't Have a Birth Year Data")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_data(df):
    """Prints 5 rows of raw data from the selected city file."""
    raw_print_indexing = 5 
    loop_flag = True
    # Keep asking the user if he wants to print raw data, every time he says 'yes' we increase out indexing counter by + 5
    while loop_flag:
        response = input("Do you wish to view the raw data? type 'yes' or 'no' \n").lower()
        if response == 'yes':
            raw_data = df[raw_print_indexing:raw_print_indexing + 5]
            raw_print_indexing += 5
            print(raw_data)
        else:
            loop_flag = False


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
