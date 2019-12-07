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
     united_city = input('\nWhich city would you like to filter by? New York City, Chicago or Washington???\n').lower()   
    while true:            
            if united_city in ('New York City', 'Chicago', 'Washington'):
                break                
            else:
                united_city=input.("Enter correct city: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('\\nWhich month you want ? January, February, March, April, May, or June?\\n').lower()
    while(true): 
        if month  in ('January', 'February', 'March', 'April', 'May', 'June', 'all')):
            break
        else:
            month = input('Enter correct month:\\n').lower()
       

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("\\nWhich day you want ? monday, tuesday, wednesday, thursday, friday, saturday , sunday or all to display data of all     days?\\n")
    while(true):
        if day in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
            break
        else:
            day = input('Enter Correct day: ').lower()
  

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
    df = df[df['Start Time'].dt.month == month]    
    if day != 'all': 
        df = df[df['Start Time'].dt.weekday_name == day.title()]
        print(df.head())

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if(month == 'all'):
        most_common_month = df['Start Time'].dt.month.value_counts().idxmax()
        print('Most common month is ' + str(most_common_month))

    # TO DO: display the most common day of week
    if(day == 'all'):
        most_common_day = df['Start Time'].dt.weekday_name.value_counts().idxmax()
        print('Most common day is ' + str(most_common_day))


    # TO DO: display the most common start hour
    most_common_hour = df['Start Time'].dt.hour.value_counts().idxmax()
    print('Most popular hour is ' + str(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = st.mode(df['Start Station'])
    print('\\nMost common start station is {}\\n'.format(most_start_station))
    

    # TO DO: display most commonly used end station
    most_end_station = st.mode(df['End Station'])
    print('\\nMost common end station is {}\\n'.format(most_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    combination_trip = df['Start Station'].astype(str) + " to " + df['End Station'].astype(str)
    most_frequent_trip = combination_trip.value_counts().idxmax()
    print('\\nMost popular trip is from {}\\n'.format(most_frequent_trip))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
        time1 = total_travel_time
        day = time1 // (24 * 3600)
        time1 = time1 % (24 * 3600)
        hour = time1 // 3600
        time1 %= 3600
        minutes = time1 // 60
        time1 %= 60
        seconds = time1
        print('\\nTotal travel time is {} days {} hours {} minutes {} seconds'.format(day, hour, minutes, seconds))


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
        time2 = mean_travel_time
        day2 = time2 // (24 * 3600)
        time2 = time2 % (24 * 3600)
        hour2 = time2 // 3600
        time2 %= 3600
        minutes2 = time2 // 60
        time2 %= 60
        seconds2 = time2
        print('\\nMean travel time is {} hours {} minutes {} seconds'.format(hour2, minutes2, seconds2))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    num_of_subscribers = df['User Type'].str.count('Subscriber').sum()
    num_of_customers = df['User Type'].str.count('Customer').sum()
    print('Number of subscribers are {}'.format(int(num_of_subscribers)))
    print('Number of customers are {}'.format(int(num_of_customers)))    

    # TO DO: Display counts of gender
    if('Gender' in df):
        male_count = df['Gender'].str.count('Male').sum()
        female_count = df['Gender'].str.count('Female').sum()
        print('Number of male users are {}'.format(int(male_count)))
        print('Number of female users are {}'.format(int(female_count)))


    # TO DO: Display earliest, most recent, and most common year of birth
    if('Birth Year' in df):
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()
        try:
              print(' Oldest Birth Year is {}\\n Youngest Birth Year is {} Most popular Birth Year is {}\\n'.format(int(earliest_year), int(recent_year), int(most_common_birth_year)))
        except:
             print('Oldest Birth Year is {}\\n Youngest Birth Year is {} Most popular Birth Year is {}\\n'.format(int(earliest_year), int(recent_year), most_common_birth_year))


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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
