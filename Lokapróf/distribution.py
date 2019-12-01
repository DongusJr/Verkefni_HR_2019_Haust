class Distribution:
    def __init__(self, file_steam = None):
        ''' Initialize this instance of distribution, entering a filesteam is optional ''' 
        self.__distribution = {}
        if file_steam: # If file_steam is not None 
            for line in file_steam:
                numbers = [int(number) for number in line.strip().split(" ")]  # Get all the numbers from that line of the file and convert them to int
                for number in numbers:
                    if number in self.__distribution:  # If they are in the dictionary add to count
                        self.__distribution[number] += 1
                    else:                              # If they are not in the dictionary add the number with count = 1
                        self.__distribution[number] = 1
            file_steam.close()

    def __str__(self):
        ''' Function that makes sure that the distribution prints out the right way '''
        output_str = ""
        if self.__distribution:  # If it is not empty
            for number, count in sorted(self.__distribution.items()):
                output_str += "{}: {}\n".format(number, count)  # "1: x\n2: y\n...""
        return output_str

    def set_distribution(self, distribution):
        ''' Function that allows to set a custom dictionary of distribution instead of using a filestream '''
        self.__distribution = distribution

    def average(self):
        ''' Function that returns an average of a distribution '''
        if self.__distribution:  # If it is not empty
            sum_dist, sum_count = 0, 0
            for number, count in self.__distribution.items():
                sum_dist += number*count  
                sum_count += count
            return (sum_dist/sum_count)
        else:  # If it is empty
            return 0

    def __ge__(self, other):
        ''' Function for the ">=" '''
        if self.average() >= other.average():
            return True
        return False

    def __gt__(self, other):
        ''' Function for the ">" '''
        if self.average() > other.average():
            return True
        return False

    def __add__(self, other):
        ''' Function for the '+', it takes two different distribution and combines their count for each number '''
        # new_dist = self_dist + other_dist
        new_dist = self.__distribution  # Add all the number and counts from the first distribution
        for number, count in other.__distribution.items():
            if number in new_dist: # If the number is in the new distribution, add the count from dist_other
                new_dist[number] += count
            else:                  # Initialize it if dist_2 has a unique number
                new_dist[number] = count
        sum_dist = Distribution()
        sum_dist.set_distribution(new_dist)  # Set the new distribution
        return sum_dist


