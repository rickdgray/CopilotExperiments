def countDaysBetweenDates(begin, end):
    """
    Counts the number of days between two dates.
    """
    # Get the number of days between the two dates.
    days = (end - begin).days
    # Return the number of days.
    return days

def addAllNumbersFrom1ToN(n):
    """
    Adds all the numbers from 1 to n.
    """
    # Initialize the sum.
    sum = 0
    # Loop through all the numbers from 1 to n.
    for i in range(1, n + 1):
        # Add the current number to the sum.
        sum += i
    # Return the sum.
    return sum

#from adventofcode
def countNumberOfIncreasesFromPreviousNumber(list):
    """
    Counts the number of increases from the previous number in a list.
    """
    # Initialize the number of increases.
    increases = 0
    # Loop through all the numbers in the list.
    for i in range(1, len(list)):
        # Check if the current number is greater than the previous number.
        if list[i] > list[i - 1]:
            # Increment the number of increases.
            increases += 1
    # Return the number of increases.
    return increases

def getNumbersFromFile():
    """
    Gets the numbers from a file.
    """
    # Initialize the list.
    list = []
    # Open the file.
    file = open("numbers.txt", "r")
    # Loop through all the lines in the file.
    for line in file:
        # Add the current line to the list.
        list.append(int(line))
    # Close the file.
    file.close()
    # Return the list.
    return list

print(countNumberOfIncreasesFromPreviousNumber(getNumbersFromFile()))