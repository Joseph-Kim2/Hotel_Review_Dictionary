"""
This program analyzes review scores from a CSV file and determines the weekday with the best average review score.

1. The main() function:
    - Opens a CSV file containing review data.
    - Calls the build_weekday_dict function to create a dictionary of weekdays and their corresponding review scores.
    - Closes the file.
    - Calls the best_score function to find the weekday with the best average review score.
    - Prints the result.

2. build_weekday_dict(file_handle) function:
    - Initializes an empty dictionary to store weekdays and their review scores.
    - Iterates through each line in the file:
        - Skips the header line.
        - Populates the dictionary with weekdays as keys and review scores as values.
    - Returns the populated dictionary.

3. best_score(dict1) function:
    - Initializes variables to keep track of the best day and its average score.
    - Iterates through the keys (weekdays) in the input dictionary:
        - Calculates the average review score for each weekday.
        - Updates the best day and average score if the current average is higher.
    - Returns the best day and its average score.

4. __main__ block:
    - Calls the main function if the script is executed as the main program.
"""

def main():
    # Open the CSV file containing review scores
    fh = open("LV_Ratings.csv")

    # Call build_weekday_dict to create a dictionary of weekdays and review scores
    dictionary1 = build_weekday_dict(fh)

    # Close the file
    fh.close()

    # Call best_score to find the weekday with the best average review score
    day, score = best_score(dictionary1)

    # Print the result
    print("The weekday with the best review scores was %s with an average score of %.2f" % (day, score))

def build_weekday_dict(file_handle):
    # Initialize an empty dictionary to store weekdays and their review scores
    dictionary2 = {}

    # Iterate through each line in the file
    for line in file_handle:
        data = line.split(",")

        # Skip the header line
        if data[1] == "Review Score":
            continue

        # Populate the dictionary with weekdays and review scores
        if data[6] in dictionary2:
            dictionary2[data[6]].append(int(data[1]))
        else:
            dictionary2[data[6]] = [int(data[1])]

    # Return the populated dictionary
    return dictionary2

def best_score(dict1):
    # Initialize variables to keep track of the best day and its average score
    best_day = ""
    best_avg = 0

    # Iterate through the keys (weekdays) in the input dictionary
    for key in dict1.keys():
        # Calculate the average review score for each weekday
        average = sum(dict1[key]) / len(dict1[key])

        # Update the best day and average score if the current average is higher
        if average > best_avg:
            best_day = key
            best_avg = average

    # Return the best day and its average score
    return best_day, best_avg

# Check if the script is executed as the main program
if __name__ == "__main__":
    # Call the main function
    main()

