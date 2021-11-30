import time
import pandas as pd
import numpy as np

#Defining the data 
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_dict = {'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6, 'all':7}
day_dict = {'sunday':1, 'monday':2, 'tuesday':3, 'wednesday':4, 'thursday':5, 'friday':6, 'saturday':7, 'all':8}
    
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    #CITY FILTER
    city = ''
    #This while loop will take the empty list above and input user data to filter by
    while city not in CITY_DATA.keys():
        print('\nPlease choose a city to explore its bikeshare data: ')
        print('\nI can show you Chicago, New York City, or Washington!')
        city = input().lower()
        #By the end of this loop, users will input which city they want to filter by
        #By putting the lower function, I am making sure that all the inputs become standardized
        
        if city not in CITY_DATA.keys():
            print('\nPlease input a valid response. Remember you can choose from Chicago, New York City, or Washington!')
       
    print(('\nOkay! Let\'s look at {}!').format(city.title()))
    #This will confirm the user's city and present it to the user in title format
    
    #MONTH FILTER
    #Now we will create another input but hold each month in a dictionary as to standardize the data
    #I am going to put 'all' as the 7th key so the months match their chronological order best
    month_dict = {'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6, 'all':7}
    month = ''
    while month not in month_dict.keys():
        print('\nPlease choose a month to filter your city\'s data: ')
        print('\nPlease input the name of a month from January through June, or you can select all available months by inputting "All"')
        month = input().lower()
        #This loop will prompt the user to input the month they want to filter by, and create a standard input using the lower function
    
        if month not in month_dict.keys():
            print('\nPlease input a valid response. Remember you can choose a month from January through June, or all months.')
    
    print(('\nOkay! Let\'s look at {}!').format(month.title()))
    
    #DAY FILTER
    #For this task, I am going to use the same while loop methodology
    day_dict = {'sunday':1, 'monday':2, 'tuesday':3, 'wednesday':4, 'thursday':5, 'friday':6, 'saturday':7, 'all':8}
    day = ''
    while day not in day_dict.keys():
        print('\nPlease choose a day to filter your city\'s data: ')
        print('\nPlease input a day of the week from Sunday though Saturday, or you can select all available days by inputting "All"')
        day = input().lower()
   
        if day not in day_dict.keys():
            print('\nPlease input a valid response. Remember you can choose any day of the week, or all days.')
        
    print(('\nOkay! Let\'s look at {}!').format(day.title()))
    
    #This next line will confirm their inputs
    print(('\nI will show you data for {}, using the month filter: {}, and the day filter: {}.').format(city.title(), month.title(), day.title()))
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
    #Loading the data
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
   
    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month
    # extract day of the week from the Start Time column to create a day of the week column
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    
    #Now we are going to filter for month and day of the week if necessary
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    #Using mode to extract the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month (January as 1 and June as 6):', popular_month)


    #Using mode to extract the most common day of the week
    popular_day = df['day_of_week'].mode()[0]
    print('\nMost Popular Day:', popular_day)

                
    #Using mode to extract the most common hour
    popular_hour = df['hour'].mode()[0]
    print('\nMost Popular Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #Using mode to extract the most popular start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station: ', common_start_station)

    #Using mode to extract the most popular end station
    common_end_station = df['End Station'].mode()[0]
    print('\nMost Popular End Station: ', common_end_station)

    #Using operations to create a new column then using mode to extract the most popular start to end stations
    df['Start To End'] = df['Start Station'] + ' to ' + df['End Station']
    start_to_end = df['Start To End'].mode()[0]
    print('\nMost Popular Start to End Stations: ', start_to_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #Using sum to extract the total travel time
    total_travtime = df['Trip Duration'].sum()
    print('Total Travel Time: ', total_travtime)

    #Using mean to extract the mean travel time
    mean_travtime = df['Trip Duration'].mean()
    print('\nMean Travel Time: ', mean_travtime)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Using count to extract the counts of user types
    user_type = df['User Type'].value_counts()
    print(('Number of Users by User Type:\n \n{}').format(user_type))

    #Using count to extract the counts of gender
    #After troubleshooting, I realize that there is no gender column in the df for Washington. To remedy this I have included a try
    #statement as to make sure the code does not break if there is no gender column
    try:
        gender = df['Gender'].value_counts()
        print(('\nNumber of Users by Gender: \n \n{}').format(gender))
    except:
        print('\nThere is no Gender column.')
    #Using min, max, and mode to extract the earliest, most recent, and most common birth years
    #Similar to gender, I have included a try statement so the code will not break
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common = int(df['Birth Year'].mode()[0])
        print(('\nThe earliest User Birth Year is {}, \nthe most recent User Birth Year is {}, \nand the most common User Birth Year is {}').format(earliest, recent, common))
    except:
        print('\nThere is no Birth Year column.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data from the selected city's csv file if prompted.
        
        Args:
            (df): the dataframe you want to work with.
        
        Returns:
            Nothing.
            """
    #To display the raw data I am using a similar methodology to the city, month, day filters
    #I created a list and a string variable then ran a while loop to keep prompting the user if 
    #they would like to see more raw data. When the answer is no, the loop breaks
    responses = ['yes', 'no']
    raw_data = ''
    count = 0
    #Prompts users for input and appends this to the raw_data variable
    while raw_data not in responses:
        print('\nWould you like to view the raw data?')
        raw_data = input().lower()
        if raw_data == 'yes':
            print(df.head(5))
        elif raw_data not in responses:
            print('\nPlease type yes or no.')
          
   #Keeps asking users for input until the answer is not yes     
    while raw_data == 'yes':
        print('\nWould you like to view more raw data?')
        count += 5
        raw_data = input().lower()
        if raw_data == 'yes':
            print(df[count:count+5])
        elif raw_data != 'yes':
            break
    
    print('-'*40)
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()

#Awknowledgments:
#I used the pandas documentation page for general formatting/syntax and various github forum pages for general bug/error troubleshooting