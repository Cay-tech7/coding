# Olympic Medal Analysis
# This program analyzes Olympic medal data for various countries.

#Olymipic medal data: (Country, (Gold, Silver, Bronze))
#data pulled from the most recent olympics(changed order to ensure code works correctly)
olympic_data = [
    ("USA", (40, 44, 42)),
    ("China", (40, 27, 24)),
    ("Spain", (5, 4, 9)),
    ("Sweden", (4, 4, 3)),
    ("Kenya", (4, 2, 5)),
    ("Norway", (4, 1, 3)),
    ("Ireland", (4, 0, 3)),
    ("Brazil", (3, 7, 10)),
    ("Iran", (3, 6, 3)),
    ("Ukraine", (3, 5, 4)),
    ("Belgium", (3, 1, 6)),
    ("Romania", (3, 4, 2)),
    ("Japan", (20, 12, 13)),
    ("Australia", (18, 19, 16)),
    ("France", (16, 26, 22)),
    ("Netherlands", (15, 7, 12)),
    ("Great Britain", (14, 22, 29)),
    ("South Korea", (13, 9, 10)),
    ("Italy", (12, 13, 15)),
    ("Germany", (12, 13, 8)),
    ("New Zealand", (10, 7, 3)),
    ("Canada", (9, 7, 11)),
    ("Uzbekistan", (8, 2, 3)),
    ("Hungary", (6, 7, 6)),
    ("Georgia", (3, 3, 1))
]

# Function to analyze medal data by calculating total medals and sorting countries by total medals earned
def analyze_medals(data):
    medal_totals = [] #create an empty list to store medal totals
    for country, medals in data: #iterate through the data
        total = sum(medals) #calculate total medals for each country
        medal_totals.append((country, total)) #append the country and total medals as a tuple to the list

    #sort the medals to the countries by total medals in descending order
    #current_contry is the index of the current element
    #next_country is the index of the next element
    #AI taught me this sorting method, it puts a loop within a loop to compare each element with the next element and swap them if they are out of order
    for current_country in range(len(medal_totals)): #loops through each country starting from the first country (current index)
        for next_country in range(current_country + 1, len(medal_totals)): #compares the total medals of the current country with the next countries (next index)
            if medal_totals[next_country][1] > medal_totals[current_country][1]: #if the next country's total medals is greater than the current country, then they are swapped
                medal_totals[current_country], medal_totals[next_country] = medal_totals[next_country], medal_totals[current_country] #swap the countries

    return medal_totals

if __name__ == "__main__":
    sorted_medals = analyze_medals(olympic_data)

    # Print the sorted medal totals
    print("Olympic Medal Totals:")
    for i, (country, total) in enumerate(sorted_medals, start=1): #enumerate to get the index and the country and total medals
        print(f"{i}. {country}: {total} medals")

    #find the country with the highest gold medals
    highest_gold = olympic_data[0][0] #initialize with the first country
    max_gold = olympic_data[0][1][0]# initialize with the first country's gold medals

    for country, medals in olympic_data: #iterate through the data
        if medals[0] > max_gold: #compare gold medals
            max_gold = medals[0] #update max_gold to current country's gold medals
            highest_gold = country #update highest_gold to current country

    print(f"\nCountry with the highest gold medals: {highest_gold} with {max_gold} gold medals.")
    print()
    print("----------------------------------------------------------------------------------------")