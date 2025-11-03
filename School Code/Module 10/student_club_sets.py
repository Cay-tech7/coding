top_gun_club = {"Maverick","Goose","Iceman","Viper"}
awaks_support_club = {"Viper","Iceman","Bob","DaggerII"}

#finds the prints a list of studetns who are in both clubs
def both_clubs():
    names = [] #list to hold names of students in both clubs
    for student in top_gun_club: #iterate through Top Gun club members
        if student in awaks_support_club: #check if student is also in AWAKS Support club
            names.append(student) #add student to names list
    return names 

#finds and prints students who are in only one of the clubs
def only_one_club():
    names = [] #list to hold names of students in only one club
    for student in top_gun_club: #iterate through Top Gun club members
        if student not in awaks_support_club: #check if student is not in AWAKS Support club
            names.append(student) #add student to names list
    for student in awaks_support_club: #iterate through AWAKS Support club members
        if student not in top_gun_club: #check if student is not in Top Gun club
            names.append(student) #add student to names list
    return names    

#finds students who are only in the Top Gun club
def only_top_gun_club():
    names = [] #list to hold names of students only in Top Gun club
    for student in top_gun_club: #iterate through Top Gun club members
        if student not in awaks_support_club: #check if student is not in AWAKS Support club
            names.append(student) #add student to names list
    return names

#finds and prints all unique students across both clubs
def all_unique_students():
    all_students = top_gun_club.union(awaks_support_club) #create a set with all unique students from both clubs
    return all_students

if __name__ == "__main__":
    print(f"These members are in both clubs: {sorted(both_clubs())}\n") #prints members in both clubs
    print(f"These members are only in one club: {sorted(only_one_club())}\n") #prints members only in one club
    print(f"These members are only in the Top Gun club: {sorted(only_top_gun_club())}\n") #prints members only in Top Gun club
    print(f"These are all unique members across both clubs: {sorted(all_unique_students())}\n") #prints all unique members across both clubs
 
    top_gun_club.add("Grace") #adds "Grace" to the Top Gun club

    awaks_support_club.discard("Bob") #removes "Bob" from the AWAKS Support club if present

    #test if grace and bob are in their respective clubs after modifications
    print(f"Is Grace in the Top Gun club? {'Grace' in top_gun_club}")
    print(f"Is Bob in the AWAKS Support club? {'Bob' in awaks_support_club}")