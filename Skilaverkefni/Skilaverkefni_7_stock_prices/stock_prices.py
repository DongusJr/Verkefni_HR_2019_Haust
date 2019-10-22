DATE = 0
ADJ_CLOSE = 5
VOLUME = 6

def open_file(file_name):
    ''' A function that takes a filename from the user and returns the file object '''
    try:
        return open(file_name, "r")
    except FileNotFoundError:
        print("Filename {} not found!".format(file_name))
        return None

def get_data_list(file_obj):
    ''' A function that takes in a file object and returns a list with adj close and volume for each date '''
    is_first_line = True  # Boolean that holds on wheter it is the first line of the file
    data_list = []
    for line in file_obj:
        if is_first_line:  # Skip the first line
            is_first_line = False
            continue
        line = line.strip().split(",")
        data_list.append(line)  # Add the inner list to data_list

    return data_list  # Two dimentional list

def get_monthly_averages(data_list):
    ''' A function that takes in a list of data and returns average price for each month '''
    monthly_averages_list = []
    year_and_month = data_list[0][DATE][:7]  # Save the first month, the string will look like "xxxx-xx", used for comparison
    price_sum = 0  # sum of Volume*(Adj Close)
    volume_sum = 0  # sum of Volume
    for data in data_list:
        if data[DATE][:7] == year_and_month:  # If it is the same month
            price_sum, volume_sum = get_price_and_volume_sum(data, price_sum, volume_sum)
        else:
            # If it is a new month
            add_average_price(price_sum, volume_sum, monthly_averages_list, year_and_month)
            year_and_month = data[DATE][:7] # Save the new month
            price_sum, volume_sum = get_price_and_volume_sum(data) # Only data in parameter to reset price and volume sum
    # Add the last month to the average list
    add_average_price(price_sum, volume_sum, monthly_averages_list, year_and_month)

    return monthly_averages_list

def add_average_price(price_sum, volume_sum, monthly_averages_list, year_and_month):
    ''' Function that calculates the average price for a month and adds it to a list along with the month '''
    average_price = (price_sum)/(volume_sum) # V*C
    monthly_averages_list.append((year_and_month, average_price)) # Tuple of month and average price

def get_price_and_volume_sum(data, price_sum=0, volume_sum=0): # Price sum and volume sum take 0 by default to reset sum when it is a new month
    ''' Function that takes in line from data list and adds price and volume '''
    price_sum += float(data[ADJ_CLOSE])*float(data[VOLUME])  # add Volume*(Adj Close) to sum
    volume_sum += float(data[VOLUME])                        # add Volume to sum
    return price_sum, volume_sum

def get_max_price(data_list):
    ''' Function that finds maximum price from the data_list and also returns the date '''
    max_price = 0        # To save the max price
    max_price_date = ""  # To save the date
    for data in data_list:
        if float(data[ADJ_CLOSE]) > max_price: # If it is the highest price seen yet, save the price and the date
            max_price = float(data[ADJ_CLOSE])
            max_price_date = data[DATE]
    return (max_price_date, max_price)  # Return as a tuple

def print_info(monthly_averages_list, max_price_tuple):
    ''' Function that prints out average price for each month and the maximum price '''
    max_day, max_price = max_price_tuple
    print("{:<2}{:>7}".format("Month", "Price"))
    for month, price in monthly_averages_list:
        print("{:<10}{:>7.2f}".format(month, price))
    print("Highest price {:.2f} on day {}".format(max_price, max_day))

def main():
    ''' The main function of this program '''
    file_input = input("Enter filename: ")
    file_obj = open_file(file_input)
    if file_obj:
        data_list = get_data_list(file_obj)
        monthly_averages_list = get_monthly_averages(data_list) 
        max_price_tuple = get_max_price(data_list)
        print_info(monthly_averages_list, max_price_tuple)
        file_obj.close()

main()