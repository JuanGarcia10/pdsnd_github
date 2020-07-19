import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please name the city you are interested in (Chicago, New York City, or Washington): ').lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input('Please check again the name of the city you want to explore. There are only three posibilities: Chicago, New York City, or Washington. Please try again: ').lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Great! now please give the month you are interested in (january, february, ..., june). Otherwise write "all": ').lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        month = input('Please try again, there is only information available for the first half of the year (from january to june): ').lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('One last question: Which day are you interestd in? monday, tuesday,...? Otherwise write just "all": ').lower()
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        day = input('Please try again, the program did not recognize your input: ').lower()


    print('-'*40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        df = df[df['month'] == month.title()]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('\nThe most popular month is {}'.format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('\nThe most popular day is {}'.format(most_common_day))

    # TO DO: display the most common start hour
    most_common_start_hour = df['Start Time'].dt.hour.mode()[0]
    print('\nThe most popular hour of the day is {}'.format(most_common_start_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_s_station = df['Start Station'].mode()[0]
    print('The most popular start station is "{}"'.format(most_common_s_station))

    # TO DO: display most commonly used end station
    most_common_e_station = df['End Station'].mode()[0]
    print('The most popular end station is "{}"'.format(most_common_e_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start to End'] = df['Start Station'] + ' to ' + df['End Station']
    most_common_route = df['Start to End'].mode()[0]
    print('The most popular route is from {}'.format(most_common_route))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time_min = total_travel_time/60
    print('For the chosen period, the bikes were used a total of {} seconds or {} minutes'.format(total_travel_time, total_travel_time_min))

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    avg_travel_time_min = avg_travel_time/60
    print('For the chosen period, the bikes were used on average {} seconds or {} minutes'.format(avg_travel_time, avg_travel_time_min))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print('this is the current distribution of user types:\n{}'.format(count_user_types))

    # TO DO: Display counts of gender
    if 'Gender' not in df.columns:
        print('No gender data available')
    else:
        count_genders = df['Gender'].value_counts()
        print('this is the current distribution of genders:\n{}'.format(count_genders))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df.columns:
        print('NO data regarding brith year of the users is available')
    else:
        oldest_user = df['Birth Year'].min()
        youngest_user = df['Birth Year'].max()
        most_common_birht = df['Birth Year'].mode()[0]
        print('Oldest users were born in {}\nThe youngest users were borned in {}\nThe most common user birth is in year {}'.format(oldest_user, youngest_user, most_common_birht))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        while True:
            raw_data = input('Would you like to see some raw data? Please answer with "yes" or "no": ').lower()
            while raw_data not in ['yes', 'no']:
                raw_data = input('please answer with "yes" or "no"')
            if raw_data == 'yes':
                print(df.sample(5))
            else:
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
