###PyBoss###
#-------------------------------------------------------------------------------------------------------#
#Dependencies - Import the os module so you can create file paths across operating systems/
############# - Import the csv module so the code can read the csv file
############# - Import DateTime package for re-formatting
#-------------------------------------------------------------------------------------------------------#
import os
import csv
import datetime

#Outline the path to the csv file you're going to use in the code
#-------------------------------------------------------------------------------------------------------#
csvpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Resources', 'employee_data.csv')


#Output File
file_to_output = "analysis/employee_data_reformatted.csv"

# Dictionary of states with abbreviations
us_state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

#Establish Lists for Re-formatted Column Names
emp_ids = []
emp_first_names = []
emp_last_names = []
emp_dobs = []
emp_ssns = []
emp_states = []

#Read the csv data into the dictionary to re-format
with open(csvpath) as emp_data:
    reader = csv.DictReader(emp_data)

    #Loop through all the rows and grab the fields to put into a new list
    for row in reader:

        #Store emp_ids into a list
        emp_ids = emp_ids + [row["Emp ID"]]

        #Split and Store names in a temporary variable
        split_name = row["Name"].split(" ")

        #Save First/Last in their own lists
        emp_first_names = emp_first_names + [split_name[0]]
        emp_last_names = emp_last_names + [split_name[1]]

        #Re-format Date of Birth
        reformatted_dob = datetime.datetime.strptime(row["DOB"], "%Y-%m-%d")
        reformatted_dob = reformatted_dob.strftime("%m/%d/%Y")

        #Store Date of Birth into a list
        emp_dobs = emp_dobs + [reformatted_dob]

        #Re-format SSN
        split_ssn = list(row["SSN"])
        split_ssn[0:3] = ("*", "*", "*")
        split_ssn[4:6] = ("*", "*")
        joined_ssn = "".join(split_ssn)

        #Store SSN into a list
        emp_ssns = emp_ssns + [joined_ssn]

        #Use dictionary to replace states with abbreviations
        state_abbrev = us_state_abbrev[row["State"]]

        #Store abbreviations into a list
        emp_states = emp_states + [state_abbrev]

#Zip the lists together
empdb = zip(emp_ids, emp_first_names, emp_last_names,
            emp_dobs, emp_ssns, emp_states)

#Write the data to csv
with open(file_to_output, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Emp ID", "First Name", "Last Name",
                     "DOB", "SSN", "State"])
    writer.writerows(empdb)