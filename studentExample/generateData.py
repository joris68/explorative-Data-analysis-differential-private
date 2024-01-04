import csv
import random
import numpy as np

# Set the mean and standard deviation for the normal distribution
mean_grade = 55
std_deviation = 15


surnames = [
    "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor",
    "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson",
    "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King",
    "Wright", "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter",
    "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins",
    "Stewart", "Sanchez", "Morris", "Rogers", "Reed", "Cook", "Morgan", "Bell", "Murphy", "Bailey",
    "Rivera", "Cooper", "Richardson", "Cox", "Howard", "Ward", "Torres", "Peterson", "Gray", "Ramirez",
    "James", "Watson", "Brooks", "Kelly", "Sanders", "Price", "Bennett", "Wood", "Barnes", "Ross",
    "Henderson", "Coleman", "Jenkins", "Perry", "Powell", "Long", "Patterson", "Hughes", "Flores", "Washington",
    "Butler", "Simmons", "Foster", "Gonzales", "Bryant", "Alexander", "Russell", "Griffin", "Diaz", "Hayes",
    "Myers", "Ford", "Hamilton", "Graham", "Sullivan", "Wallace", "Woods", "Cole", "West", "Jordan",
    "Owens", "Reynolds", "Fisher", "Ellis", "Harrison", "Gibson", "McDonald", "Cruz", "Marshall", "Ortiz",
    "Gomez", "Murray", "Freeman", "Wells", "Webb", "Simpson", "Stevens", "Tucker", "Porter", "Hunter",
    "Hicks", "Crawford", "Henry", "Boyd", "Mason", "Morales", "Kennedy", "Warren", "Dixon", "Ramos",
    "Reyes", "Burns", "Gordon", "Shaw", "Holmes", "Rice", "Robertson", "Hunt", "Black", "Daniels",
    "Palmer", "Mills", "Nichols", "Grant", "Knight", "Ferguson", "Rose", "Stone", "Hawkins", "Dunn",
    "Perkins", "Hudson", "Spencer", "Gardner", "Stephens", "Payne", "Pierce", "Berry", "Matthews", "Arnold",
    "Wagner", "Willis", "Ray", "Watkins", "Olson", "Carroll", "Duncan", "Snyder", "Hart", "Cunningham",
    "Bradley", "Lane", "Andrews", "Ruiz", "Harper", "Fox", "Riley", "Armstrong", "Carpenter", "Weaver",
    "Greene", "Lawrence", "Elliott", "Chavez", "Sims", "Austin", "Peters", "Kelley", "Franklin", "Lawson"
]



names = [
    "Liam", "Olivia", "Noah", "Emma", "Oliver", "Ava", "Elijah", "Charlotte", "William", "Sophia",
    "James", "Amelia", "Benjamin", "Isabella", "Lucas", "Mia", "Henry", "Evelyn", "Alexander", "Harper",
    "Mason", "Abigail", "Michael", "Emily", "Ethan", "Elizabeth", "Daniel", "Avery", "Jacob", "Sofia",
    "Logan", "Ella", "Jackson", "Madison", "Sebastian", "Scarlett", "Jack", "Victoria", "Aiden", "Grace",
    "Owen", "Chloe", "Samuel", "Penelope", "Matthew", "Luna", "Joseph", "Layla", "Levi", "Riley",
    "Mateo", "Zoey", "David", "Nora", "John", "Eleanor", "Wyatt", "Hannah", "Carter", "Addison",
    "Julian", "Lily", "Luke", "Camila", "Grayson", "Aubrey", "Isaac", "Zoe", "Jayden", "Stella",
    "Theodore", "Bella", "Gabriel", "Violet", "Anthony", "Aurora", "Dylan", "Savannah", "Leo", "Claire",
    "Lincoln", "Lucy", "Jaxon", "Audrey", "Asher", "Sadie", "Christopher", "Anna", "Joshua", "Kinsley",
    "Andrew", "Allison", "Thomas", "Sarah", "Ezra", "Aaliyah", "Hudson", "Samantha", "Charles", "Natalie",
    "Caleb", "Alice", "Isaiah", "Lillian", "Ryan", "Leah", "Nathan", "Adeline", "Adrian", "Elizabeth",
    "Christian", "Lyla", "Maverick", "Mila", "Colton", "Eliana", "Elias", "Aria", "Aaron", "Elena",
    "Eli", "Gabriella", "Landon", "Taylor", "Jonathan", "Hailey", "Nolan", "Gianna", "Hunter", "Willow",
    "Cameron", "Katherine", "Connor", "Nevaeh", "Santiago", "Ruby", "Jeremiah", "Quinn", "Ezekiel", "Piper",
    "Angel", "Isla", "Roman", "Sydney", "Easton", "Emilia", "Miles", "Caroline", "Robert", "Nova",
    "Jameson", "Genesis", "Nicholas", "Emery", "Greyson", "Kennedy", "Cooper", "Serenity", "Ian", "Valentina",
    "Carson", "Willow", "Axel", "Valeria", "Jaxson", "Adalynn", "Dominic", "Athena", "Leonardo", "Delilah",
    "Luca", "Melanie", "Brooks", "Margaret", "Micah", "Jade", "Austin", "Ivy", "Ayden", "Luna",
    "Adam", "Hazel", "Xavier", "Summer", "Josiah", "Emerson", "Diego", "Leilani", "Vincent", "Eliza",
    "Carter", "Laila", "Parker", "Liliana", "Wesley", "Holly", "Maddox", "Maci", "Kai", "Gracie",
    "Harrison", "Isabelle", "Zachary", "Mya", "Jason", "Vivian", "Chase", "Haley", "Ian", "Morgan"
]

matrikel_nummern = [random.randint(100000, 999999) for _ in range(200)]
num_students = 200

# Create a CSV file and write headers
with open('student_grades.csv', mode='w', newline='') as file:
    fieldnames = ['Name', 'Surname', 'StudentID', 'Course', 'Grade']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for i in range(num_students):
        # Generate random student data
        name = names[i]
        surname = surnames[i]
        student_id = matrikel_nummern[i]
        course = "Information Governance"  

        # right skewed distribution 
        grade = int(np.random.normal(mean_grade, std_deviation) - np.random.exponential(5))

        # Ensure the grade is within a valid range (0-100)
        grade = max(min(grade, 100), 0)

        writer.writerow({'Name': name, 'Surname': surname, 'StudentID': student_id,
                         'Course': course, 'Grade': grade})

print("CSV file generated successfully.")
