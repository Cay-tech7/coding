# This program analyzes product ratings using functional programming concepts.
# It maps numeric ratings to descriptive labels, filters positive ratings,
# calculates the average rating, generates recommendation flags, and summarizes the ratings.

from functools import reduce #import statistics module for average calculation

# Function to map numeric ratings to descriptive labels
def map_product_ratings(ratings): 
    rating_map = list(map(lambda x: "Excellent" if x == 5 else "Good" if x == 4 else "Average" if x == 3 else "Poor" if x == 2 else "Terrible", ratings))  #uses map to convert numeric ratings to descriptive labels
    print(f"Mapped product ratings: {rating_map}\n")  
    return rating_map

# Function to filter positive ratings (4 and 5)
def filter_positive_ratings(ratings):
    positive_ratings = list(filter(lambda x: x >= 4, ratings)) #uses filter to get ratings 4 and 5
    print(f"Positive ratings (4 and 5): {positive_ratings}\n") 
    return positive_ratings

# Function to calculate average rating
def average_rating(ratings):
    total =reduce(lambda x, y: x + y, ratings) #uses reduce to sum up ratings
    average_rating = total / len(ratings) #calculate average
    print(f"Average rating: {average_rating:.2f}\n")
    return average_rating

# Function to generate recommendation flags (True for ratings 4 and 5)
def generate_recommendations_flags(ratings):
    recommendations = [rating >= 4 for rating in ratings] #list comprehension to generate boolean flags and stores in a list
    print(f"Recommendations flags: {recommendations}\n")
    return recommendations

# Function to summarize ratings count
def rating_summary(ratings):
    summary = {i: ratings.count(i) for i in range(1, 6)} #dictionary comprehension to count occurrences of each rating from 1 to 5 by using count method
    print("Rating Summary:")
    for key, value in summary.items(): #iterate through summary dictionary
        print(f"\t{key}: {value}") #print each rating and its count with a tab
    return summary

if __name__ == "__main__":
    ratings = [4, 5, 2, 3, 5, 1, 4, 3, 5, 2, 4]
    print("Original Ratings:", ratings, "\n")
    map_product_ratings(ratings)
    filter_positive_ratings(ratings)
    average_rating(ratings)
    generate_recommendations_flags(ratings)
    rating_summary(ratings)