import time
import pandas as pd
import numpy as np
import datetime

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
    city=''
    month=0
    day=0
    option=0
    while city.upper() not in ['C','N','W']:
        city= input('\nPlease enter a city to filer Chicago (C), New York (N), Washington(W): ')
    while option not in [1,2,3]:
        option= int(input('\nWhich subset of data are you looking for:\n1) By Month\n2) by month and day\n3) No Filter\nSelect (1-3)> '))
    if option != 3:
        while month not in range(1,13):
            month= int(input('\nPlease enter a month in range of 1-12: '))
        if option==2:
            while day not in range(1,32):
                day= int(input('\nPlease enter day in the range of 1-31: '))

    print('-'*40)
    return city.lower(), month, day,option


def load_data(city, month, day,option):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        (int) option - Selected filter option
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    city, month, day,option = 'c',0,0,3
    print('params',city, month, day,option)
    df=None
    if city== 'c':
        print('loading Chicago')
        df= pd.read_csv('/home/workspace/chicago.csv')
    if city=='n':
        df= pd.read_csv('/home/workspace/new_york_city.csv')
    if city=='w':
        df= pd.read_csv('/home/workspace/washington.csv')
    df.head()
    df['Start Time']= pd.to_datetime(df['Start Time'], errors='coerce') 
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.day
    if option==1:
        df=df[(df['month']== month)]
    if option ==2:
        df=df[(df['month']== month) & (df['day']==day)]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month


    # TO DO: display the most common day of week


    # TO DO: display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day, option = get_filters()
        df = load_data(city, month, day, option)
        #df.head()
        #time_stats(df)
        #station_stats(df)
        #trip_duration_stats(df)
        #user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
