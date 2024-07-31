import tkinter as tk
import webbrowser
import subprocess

# Game window
window = tk.Tk()
window.title("Wallet Quest")

# Initialize game variables (initial values are in rupees)
initial_budget = 10000
initial_savings = 10000
initial_financial_score = 0

budget = initial_budget
savings = initial_savings
financial_score = initial_financial_score

global level 
level = 1 

# Define the scenarios with choices
scenarios = [
    {
        "name": "You’ve got one final summer of freedom. And your neighbor wants you to spend a week of it house-sitting.",
        "choices": ["Yess", "Nahh"],
        "consequences": [(-2000, -1000, -10),  # Budget, Savings, Score for Choice A
                     (0, 0, 5)] 
    },
    {
        "name": "You receive a bonus at work for your extraordinary work😊.",
        "choices": ["Save the bonus (₹3000)", "Spend the bonus"],
        "consequences": [(3000, 2000, 20),     # Budget, Savings, Score for Choice A
                         (0, 0, -10)]            # Budget, Savings, Score for Choice B
    },
    {
        "name": "You or a family member require medical treatment that is not covered by insurance,You need to pay a medical bill.",
        "choices": ["Pay the bill (₹1000)", "Ignore the bill"],
        "consequences": [(-1000, -500, -5),    # Budget, Savings, Score for Choice A
                         (0, 0, -10)]            # Budget, Savings, Score for Choice B
    },
    {
        "name": "You're considering buying a house",
        "choices": ["pay the Advance amt (₹5000)", "Delay decision"],
        "consequences": [(-5000, -3000, -20),  # Budget, Savings,  Score for Choice A
                         (0, 0, -15)]            # Budget, Savings,  Score for Choice B
    },
    {
        "name": "You come across a promising investment opportunity and you make a profitable investment.",
        "choices": ["Reinvest", "Withdraw the profit"],
        "consequences": [(5000, 3000, 30),     # Budget, Savings,Score for Choice A
                         (0, 0, 15)]            # Budget, Savings, Score for Choice B
    },
    {
        "name": "Check your savings and make a wise choice to invest on the following choices",
        "choices": ["buying any form of asset", "Spend extravagantly"],
        "consequences": [(-3000, 2000, 20),     # Budget, Savings,Score for Choice A
                         (-3000, 0, -5)]            # Budget, Savings, Score for Choice B
    },
    {
        "name": "Its lucky period...The lottery you had signed up brought you a total amount of (₹5000) ",
        "choices": ["Put into savings for your future", "Use it for daily expenses"],
        "consequences": [(0, 5000, 30),     # Budget, Savings,Score for Choice A
                         (-5000, 5000, 10)]            # Budget, Savings, Score for Choice B
    },
    {
        "name": "You came across a pamplet for health insurance,would you go for it",
        "choices": ["Yes,go for it without any background research", "Give it some thought"],
        "consequences": [(0,0, 30),     # Budget, Savings,Score for Choice A
                         (0, 0, 15)]            # Budget, Savings, Score for Choice B
    },
    {
        "name": "Someone told you about investing in stocks of a company 'ABC'",
        "choices": ["Check annual report of the comapny ", "Just invest basic amount"],
        "consequences": [(0, 0, 30),     # Budget, Savings,Score for Choice A
                         (-1000, 50, 10)]            # Budget, Savings, Score for Choice B
    }

]

scenarios2 = [
    {
        "name": "Your car breaks down unexpectedly, and you need to repair your car.",
        "choices": ["Repair the car (₹2000)", "Delay the repair"],
        "consequences": [(-2000, -1000, -10),  # Budget, Savings,  Score for Choice A
                         (0, 0, -5)]            # Budget, Savings,  Score for Choice B
    },
   
    {
        "name": "You or a family member require medical treatment that is not covered by insurance,You need to pay a medical bill.",
        "choices": ["Pay the bill (₹1000)", "Ignore the bill"],
        "consequences": [(-1000, -500, -5),    # Budget, Savings, Score for Choice A
                         (0, 0, -10)]            # Budget, Savings, Score for Choice B
    },
    {
        "name": "You're considering buying a house",
        "choices": ["pay the Advance amt (₹5000)", "Delay decision"],
        "consequences": [(-5000, -3000, -20),  # Budget, Savings,  Score for Choice A
                         (0, 0, -15)]            # Budget, Savings,  Score for Choice B
    },
    {
        "name": "You come across a promising investment opportunity and you make a profitable investment.",
        "choices": ["Reinvest", "Withdraw the profit"],
        "consequences": [(5000, 3000, 30),     # Budget, Savings,Score for Choice A
                         (0, 0, 15)]            # Budget, Savings, Score for Choice B
    },
    {
        "name": "Check your savings and make a wise choice to invest on the following choices",
        "choices": ["buying any form of asset", "Spend extravagantly"],
        "consequences": [(-3000, 2000, 20),     # Budget, Savings,Score for Choice A
                         (-3000, 0, -5)]            # Budget, Savings, Score for Choice B
    },
    {
        "name": "Its lucky period...The lottery you had signed up brought you a total amount of (₹5000) ",
        "choices": ["Put into savings for your future", "Use it for daily expenses"],
        "consequences": [(0, 5000, 30),     # Budget, Savings,Score for Choice A
                         (-5000, 5000, 10)]            # Budget, Savings, Score for Choice B
    },
    {
        "name": "You came across a pamplet for health insurance,would you go for it",
        "choices": ["Yes,go for it without any background research", "Give it some thought"],
        "consequences": [(0,0, 30),     # Budget, Savings,Score for Choice A
                         (0, 0, 15)]            # Budget, Savings, Score for Choice B
    },
    {
        "name": "Someone told you about investing in stocks of a company 'ABC'",
        "choices": ["Check annual report of the comapny ", "Just invest basic amount"],
        "consequences": [(0, 0, 30),     # Budget, Savings,Score for Choice A
                         (-1000, 50, 10)]            # Budget, Savings, Score for Choice B
    }

]

scenarios3 = [
   
    {
        "name": "You're considering buying a house",
        "choices": ["pay the Advance amt (₹5000)", "Delay decision"],
        "consequences": [(-5000, -3000, -20),  # Budget, Savings,  Score for Choice A
                         (0, 0, -15)]            # Budget, Savings,  Score for Choice B
    },
    {
        "name": "You come across a promising investment opportunity and you make a profitable investment.",
        "choices": ["Reinvest", "Withdraw the profit"],
        "consequences": [(5000, 3000, 30),     # Budget, Savings,Score for Choice A
                         (0, 0, 15)]            # Budget, Savings, Score for Choice B
    },
    {
        "name": "Check your savings and make a wise choice to invest on the following choices",
        "choices": ["buying any form of asset", "Spend extravagantly"],
        "consequences": [(-3000, 2000, 20),     # Budget, Savings,Score for Choice A
                         (-3000, 0, -5)]            # Budget, Savings, Score for Choice B
    },
    {
        "name": "Its lucky period...The lottery you had signed up brought you a total amount of (₹5000) ",
        "choices": ["Put into savings for your future", "Use it for daily expenses"],
        "consequences": [(0, 5000, 30),     # Budget, Savings,Score for Choice A
                         (-5000, 5000, 10)]            # Budget, Savings, Score for Choice B
    },
    {
        "name": "You came across a pamplet for health insurance,would you go for it",
        "choices": ["Yes,go for it without any background research", "Give it some thought"],
        "consequences": [(0,0, 30),     # Budget, Savings,Score for Choice A
                         (0, 0, 15)]            # Budget, Savings, Score for Choice B
    },
    {
        "name": "Someone told you about investing in stocks of a company 'ABC'",
        "choices": ["Check annual report of the comapny ", "Just invest basic amount"],
        "consequences": [(0, 0, 30),     # Budget, Savings,Score for Choice A
                         (-1000, 50, 10)]            # Budget, Savings, Score for Choice B
    }

]

scenarios4 = [
    {
        "name": "You come across a promising investment opportunity and you make a profitable investment.",
        "choices": ["Reinvest", "Withdraw the profit"],
        "consequences": [(5000, 3000, 30),     # Budget, Savings,Score for Choice A
                         (0, 0, 15)]            # Budget, Savings, Score for Choice B
    },
    {
        "name": "Check your savings and make a wise choice to invest on the following choices",
        "choices": ["buying any form of asset", "Spend extravagantly"],
        "consequences": [(-3000, 2000, 20),     # Budget, Savings,Score for Choice A
                         (-3000, 0, -5)]            # Budget, Savings, Score for Choice B
    },
    {
        "name": "Its lucky period...The lottery you had signed up brought you a total amount of (₹5000) ",
        "choices": ["Put into savings for your future", "Use it for daily expenses"],
        "consequences": [(0, 5000, 30),     # Budget, Savings,Score for Choice A
                         (-5000, 5000, 10)]            # Budget, Savings, Score for Choice B
    },
    {
        "name": "You came across a pamplet for health insurance,would you go for it",
        "choices": ["Yes,go for it without any background research", "Give it some thought"],
        "consequences": [(0,0, 30),     # Budget, Savings,Score for Choice A
                         (0, 0, 15)]            # Budget, Savings, Score for Choice B
    },
    {
        "name": "Someone told you about investing in stocks of a company 'ABC'",
        "choices": ["Check annual report of the comapny ", "Just invest basic amount"],
        "consequences": [(0, 0, 30),     # Budget, Savings,Score for Choice A
                         (-1000, 50, 10)]            # Budget, Savings, Score for Choice B
    }

]

scenarios5 = [
    {
        "name": "Check your savings and make a wise choice to invest on the following choices",
        "choices": ["buying any form of asset", "Spend extravagantly"],
        "consequences": [(-3000, 2000, 20),     # Budget, Savings,Score for Choice A
                         (-3000, 0, -5)]            # Budget, Savings, Score for Choice B
    },
    {
        "name": "Its lucky period...The lottery you had signed up brought you a total amount of (₹5000) ",
        "choices": ["Put into savings for your future", "Use it for daily expenses"],
        "consequences": [(0, 5000, 30),     # Budget, Savings,Score for Choice A
                         (-5000, 5000, 10)]            # Budget, Savings, Score for Choice B
    },
    {
        "name": "You came across a pamplet for health insurance,would you go for it",
        "choices": ["Yes,go for it without any background research", "Give it some thought"],
        "consequences": [(0,0, 30),     # Budget, Savings,Score for Choice A
                         (0, 0, 15)]            # Budget, Savings, Score for Choice B
    },
    {
        "name": "Someone told you about investing in stocks of a company 'ABC'",
        "choices": ["Check annual report of the comapny ", "Just invest basic amount"],
        "consequences": [(0, 0, 30),     # Budget, Savings,Score for Choice A
                         (-1000, 50, 10)]            # Budget, Savings, Score for Choice B
    }

]

current_scenario_index = 0

# Function to handle user choices
def make_choice(choice_index):
    global budget, savings, financial_score, current_scenario_index

    # Update game variables based on user's choice
    choice_consequences = scenarios[current_scenario_index]["consequences"][choice_index]
    budget_change, savings_change, financial_score_change = choice_consequences
    budget += budget_change
    savings += savings_change
    financial_score += financial_score_change

    # Update labels on the interface
    update_labels()

    # Move to the next scenario
    current_scenario_index += 1

    # Check if there are more scenarios left
    if current_scenario_index < len(scenarios) and level==1:
        present_scenario()
    elif current_scenario_index < len(scenarios2) and level==2:
        present_scenario2()
    elif current_scenario_index < len(scenarios2) and level==3:
        present_scenario3()
    elif current_scenario_index < len(scenarios2) and level==4:
        present_scenario4()
    elif current_scenario_index < len(scenarios2) and level==5:
        present_scenario5()
    else:
        # End of game
        label_scenario.config(text="Level Over")
        # Remove choice buttons
        for button in choice_buttons:
            button.grid_forget()
        # Show the financial score and its description
        label_financial_score.config(text=f"Financial Score: {financial_score}")
        display_score_description(financial_score)
        # Show restart button
        restart_button.grid(row=12, column=0, columnspan=2, padx=10, pady=5)
        # Show back to menu button
        button_back_to_menu.grid(row=14, column=0, columnspan=2, padx=10, pady=5)

# Function to update labels on the interface
def update_labels():
    label_budget.config(text=f"Budget: ₹{budget:,}")
    label_savings.config(text=f"Savings: ₹{savings:,}")
    label_financial_score.config(text=f"Financial Score: {financial_score}")


# Function to start the game
def start_game():
    label_welcome.grid_forget()  # Remove the welcome message
    button_start.grid_forget()    # Remove the start button
    button_terms.grid(row=10, column=1, padx=5, pady=5)
    button_level1.grid(row=12, column=0, padx=5, pady=5)   
    button_quiz.grid(row=14, column=1, padx=5, pady=5)
    button_level2.grid(row=16, column=0, padx=5, pady=5)   
    button_quiz2.grid(row=18, column=1, padx=5, pady=5)
    button_level3.grid(row=20, column=0, padx=5, pady=5)  
    button_quiz3.grid(row=22, column=1, padx=5, pady=5) 
    button_level4.grid(row=24, column=0, padx=5, pady=5)  
    button_quiz4.grid(row=26, column=1, padx=5, pady=5) 
    button_level5.grid(row=30, column=0, padx=5, pady=5)  
    button_quiz5.grid(row=32, column=1, padx=5, pady=5) 

def level_1_button_click():
    # Hide the Level-1 and Quiz buttons
    global level
    level=1;
    button_terms.grid_forget()
    button_level1.grid_forget()
    button_quiz.grid_forget()
    button_level2.grid_forget()
    button_quiz2.grid_forget()
    button_level3.grid_forget()
    button_quiz3.grid_forget()
    button_level4.grid_forget()
    button_quiz4.grid_forget()
    button_level5.grid_forget()
    button_quiz5.grid_forget()
    global budget, savings, financial_score, current_scenario_index
    budget = initial_budget
    savings = initial_savings
    financial_score = initial_financial_score  # Reset financial score
    label_budget.config(text=f"Budget: ₹{budget:,}")
    label_savings.config(text=f"Savings: ₹{savings:,}")
    label_financial_score.config(text=f"Financial Score: {financial_score}")  # Update financial score label
    label_scenario.config(text="")
    # Show the scenario labels and choice buttons
    label_scenario.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
    label_budget.grid(row=7, column=0, columnspan=2, padx=10, pady=5)
    label_savings.grid(row=8, column=0, columnspan=2, padx=10, pady=5)
    label_financial_score.grid(row=9, column=0, columnspan=2, padx=10, pady=5)
    present_scenario()

# Function to handle the "Level-2" button click
def level_2_button_click():
    # Hide the Level and Quiz buttons
    global level
    level=2
    button_terms.grid_forget()
    button_level1.grid_forget()
    button_quiz.grid_forget()
    button_level2.grid_forget()
    button_quiz2.grid_forget()
    button_level3.grid_forget()
    button_quiz3.grid_forget()
    button_level4.grid_forget()
    button_quiz4.grid_forget()
    button_level5.grid_forget()
    button_quiz5.grid_forget()
    global budget, savings, financial_score, current_scenario_index
    budget = initial_budget
    savings = initial_savings
    financial_score = initial_financial_score  # Reset financial score
    label_budget.config(text=f"Budget: ₹{budget:,}")
    label_savings.config(text=f"Savings: ₹{savings:,}")
    label_financial_score.config(text=f"Financial Score: {financial_score}")  # Update financial score label
    label_scenario.config(text="")
    # Show the scenario labels and choice buttons
    label_scenario.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
    label_budget.grid(row=7, column=0, columnspan=2, padx=10, pady=5)
    label_savings.grid(row=8, column=0, columnspan=2, padx=10, pady=5)
    label_financial_score.grid(row=9, column=0, columnspan=2, padx=10, pady=5)
    present_scenario2()

# Function to handle the "Level-3" button click
def level_3_button_click():
    # Hide the Level and Quiz buttons
    global level
    level=3
    button_terms.grid_forget()
    button_level1.grid_forget()
    button_quiz.grid_forget()
    button_level2.grid_forget()
    button_quiz2.grid_forget()
    button_level3.grid_forget()
    button_quiz3.grid_forget()
    button_level4.grid_forget()
    button_quiz4.grid_forget()
    button_level5.grid_forget()
    button_quiz5.grid_forget()
    global budget, savings, financial_score, current_scenario_index
    budget = initial_budget
    savings = initial_savings
    financial_score = initial_financial_score  # Reset financial score
    label_budget.config(text=f"Budget: ₹{budget:,}")
    label_savings.config(text=f"Savings: ₹{savings:,}")
    label_financial_score.config(text=f"Financial Score: {financial_score}")  # Update financial score label
    label_scenario.config(text="")
    # Show the scenario labels and choice buttons
    label_scenario.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
    label_budget.grid(row=7, column=0, columnspan=2, padx=10, pady=5)
    label_savings.grid(row=8, column=0, columnspan=2, padx=10, pady=5)
    label_financial_score.grid(row=9, column=0, columnspan=2, padx=10, pady=5)
    present_scenario3()

# Function to handle the "Level-4" button click
def level_4_button_click():
    # Hide the Level and Quiz buttons
    global level
    level=4
    button_terms.grid_forget()
    button_level1.grid_forget()
    button_quiz.grid_forget()
    button_level2.grid_forget()
    button_quiz2.grid_forget()
    button_level3.grid_forget()
    button_quiz3.grid_forget()
    button_level4.grid_forget()
    button_quiz4.grid_forget()
    button_level5.grid_forget()
    button_quiz5.grid_forget()
    global budget, savings, financial_score, current_scenario_index
    budget = initial_budget
    savings = initial_savings
    financial_score = initial_financial_score  # Reset financial score
    label_budget.config(text=f"Budget: ₹{budget:,}")
    label_savings.config(text=f"Savings: ₹{savings:,}")
    label_financial_score.config(text=f"Financial Score: {financial_score}")  # Update financial score label
    label_scenario.config(text="")
    # Show the scenario labels and choice buttons
    label_scenario.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
    label_budget.grid(row=7, column=0, columnspan=2, padx=10, pady=5)
    label_savings.grid(row=8, column=0, columnspan=2, padx=10, pady=5)
    label_financial_score.grid(row=9, column=0, columnspan=2, padx=10, pady=5)
    present_scenario4()

# Function to handle the "Level-5" button click
def level_5_button_click():
    # Hide the Level and Quiz buttons
    global level
    level=5
    button_terms.grid_forget()
    button_level1.grid_forget()
    button_quiz.grid_forget()
    button_level2.grid_forget()
    button_quiz2.grid_forget()
    button_level3.grid_forget()
    button_quiz3.grid_forget()
    button_level4.grid_forget()
    button_quiz4.grid_forget()
    button_level5.grid_forget()
    button_quiz5.grid_forget()
    global budget, savings, financial_score, current_scenario_index
    budget = initial_budget
    savings = initial_savings
    financial_score = initial_financial_score  # Reset financial score
    label_budget.config(text=f"Budget: ₹{budget:,}")
    label_savings.config(text=f"Savings: ₹{savings:,}")
    label_financial_score.config(text=f"Financial Score: {financial_score}")  # Update financial score label
    label_scenario.config(text="")
    # Show the scenario labels and choice buttons
    label_scenario.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
    label_budget.grid(row=7, column=0, columnspan=2, padx=10, pady=5)
    label_savings.grid(row=8, column=0, columnspan=2, padx=10, pady=5)
    label_financial_score.grid(row=9, column=0, columnspan=2, padx=10, pady=5)
    present_scenario5()

def Term_quiz_click():
    subprocess.Popen(["python", "term.py"]) 

def quiz_button_click():
    webbrowser.open("Quiz1.html")  

def quiz2_button_click():
    webbrowser.open("Quiz2.html")

def quiz3_button_click():
    webbrowser.open("Quiz3.html")  

def quiz4_button_click():
    webbrowser.open("Quiz4.html") 

def quiz5_button_click():
    webbrowser.open("Quiz5.html")   
# Function to present the current scenario
def present_scenario():
    scenario = scenarios[current_scenario_index]
    scenario_name = scenario["name"]
    scenario_choices = scenario["choices"]

    # Update scenario label
    label_scenario.config(text=f"Situation {current_scenario_index + 1}: {scenario_name}")

    # Update choice buttons
    for i, choice in enumerate(scenario_choices):
        choice_buttons[i].config(text=choice)
        choice_buttons[i].grid(row=i + 3, column=0, columnspan=2, padx=5, pady=5)  # Show choice buttons

def present_scenario2():
    scenario = scenarios2[current_scenario_index]
    scenario_name = scenario["name"]
    scenario_choices = scenario["choices"]

    # Update scenario label
    label_scenario.config(text=f"Situation {current_scenario_index + 1}: {scenario_name}")

    # Update choice buttons
    for i, choice in enumerate(scenario_choices):
        choice_buttons[i].config(text=choice)
        choice_buttons[i].grid(row=i + 3, column=0, columnspan=2, padx=5, pady=5)  # Show choice buttons

def present_scenario3():
    scenario = scenarios3[current_scenario_index]
    scenario_name = scenario["name"]
    scenario_choices = scenario["choices"]

    # Update scenario label
    label_scenario.config(text=f"Situation {current_scenario_index + 1}: {scenario_name}")

    # Update choice buttons
    for i, choice in enumerate(scenario_choices):
        choice_buttons[i].config(text=choice)
        choice_buttons[i].grid(row=i + 3, column=0, columnspan=2, padx=5, pady=5)  # Show choice buttons

def present_scenario4():
    scenario = scenarios4[current_scenario_index]
    scenario_name = scenario["name"]
    scenario_choices = scenario["choices"]

    # Update scenario label
    label_scenario.config(text=f"Situation {current_scenario_index + 1}: {scenario_name}")

    # Update choice buttons
    for i, choice in enumerate(scenario_choices):
        choice_buttons[i].config(text=choice)
        choice_buttons[i].grid(row=i + 3, column=0, columnspan=2, padx=5, pady=5)  # Show choice buttons

def present_scenario5():
    scenario = scenarios2[current_scenario_index]
    scenario_name = scenario["name"]
    scenario_choices = scenario["choices"]

    # Update scenario label
    label_scenario.config(text=f"Situation {current_scenario_index + 1}: {scenario_name}")

    # Update choice buttons
    for i, choice in enumerate(scenario_choices):
        choice_buttons[i].config(text=choice)
        choice_buttons[i].grid(row=i + 3, column=0, columnspan=2, padx=5, pady=5)  # Show choice buttons

# Function to reset the game
def restart_game():
    global budget, savings, financial_score, current_scenario_index
    budget = initial_budget
    savings = initial_savings
    financial_score = initial_financial_score  # Reset financial score
    current_scenario_index = 0
    label_budget.config(text=f"Budget: ₹{budget:,}")
    label_savings.config(text=f"Savings: ₹{savings:,}")
    label_financial_score.config(text=f"Financial Score: {financial_score}")  # Update financial score label
    label_scenario.config(text="")
    present_scenario()  # Display the first scenario
    # Remove the score description label
    score_description_label.grid_forget()

# Function to go back to the menu page
def back_to_menu():
    global current_scenario_index  
    global budget, savings, financial_score, current_scenario_index
    budget = initial_budget
    savings = initial_savings
    financial_score = initial_financial_score 
    current_scenario_index = 0     # Reset the current scenario index
    # Remove scenario labels, choice buttons, and restart button
    label_scenario.grid_forget()
    label_budget.grid_forget()
    label_savings.grid_forget()
    label_financial_score.grid_forget()
    score_description_label.grid_forget()
    restart_button.grid_forget()
    # Hide the back to menu button
    button_back_to_menu.grid_forget()
    button_terms.grid(row=10, column=1, padx=5, pady=5)
    button_level1.grid(row=12, column=0, padx=5, pady=5)   
    button_quiz.grid(row=14, column=1, padx=5, pady=5)
    button_level2.grid(row=16, column=0, padx=5, pady=5)   
    button_quiz2.grid(row=18, column=1, padx=5, pady=5)
    button_level3.grid(row=20, column=0, padx=5, pady=5)  
    button_quiz3.grid(row=22, column=1, padx=5, pady=5) 
    button_level4.grid(row=24, column=0, padx=5, pady=5)  
    button_quiz4.grid(row=26, column=1, padx=5, pady=5) 
    button_level5.grid(row=30, column=0, padx=5, pady=5)  
    button_quiz5.grid(row=32, column=1, padx=5, pady=5) 



# Create interface
frame = tk.Frame(window)
frame.pack(padx=10, pady=10)

# Welcome message
label_welcome = tk.Label(frame, text="Let's make wise decisions!")
label_welcome.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

# Start button
button_start = tk.Button(frame, text="Enter the Game", command=start_game)
button_start.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")  # Center the button

# Labels for scenario, budget, savings, and financial score (initially hidden)
label_scenario = tk.Label(frame, text="")
label_budget = tk.Label(frame, text=f"Budget: ₹{budget:,}")
label_savings = tk.Label(frame, text=f"Savings: ₹{savings:,}")
label_financial_score = tk.Label(frame, text=f"Financial Score: {financial_score}")

# Initialize choice buttons
choice_buttons = [tk.Button(frame, text="", command=lambda i=i: make_choice(i)) for i in range(4)]

# Hide choice buttons initially
for button in choice_buttons:
    button.grid_forget()

# Button for terminology quiz
button_terms = tk.Button(frame, text="Discover Your Financial IQ!", command=Term_quiz_click)
button_terms.grid(row=10, column=1, padx=5, pady=5)
button_terms.grid_remove()  # Initially hidden

# Button for Level 1
button_level1 = tk.Button(frame, text="Student Loans", command=level_1_button_click)
button_level1.grid(row=11, column=0, padx=5, pady=5)
button_level1.grid_remove()  # Initially hidden

# Button for Quiz
button_quiz = tk.Button(frame, text="Quiz on Student loans", command=quiz_button_click)
button_quiz.grid(row=12, column=1, padx=5, pady=5)
button_quiz.grid_remove()  # Initially hidden

# Button for Level 2
button_level2 = tk.Button(frame, text="Savings", command=level_2_button_click)
button_level2.grid(row=14, column=0, padx=5, pady=5)
button_level2.grid_remove()  # Initially hidden

# Button for Quiz2
button_quiz2 = tk.Button(frame, text="Quiz on Savings", command=quiz2_button_click)
button_quiz2.grid(row=16, column=1, padx=5, pady=5)
button_quiz2.grid_remove()  # Initially hidden

# Button for Level 3
button_level3 = tk.Button(frame, text="Interest", command=level_3_button_click)
button_level3.grid(row=18, column=0, padx=5, pady=5)
button_level3.grid_remove()  # Initially hidden

# Button for Quiz3
button_quiz3 = tk.Button(frame, text="Quiz on Interest", command=quiz3_button_click)
button_quiz3.grid(row=20, column=1, padx=5, pady=5)
button_quiz3.grid_remove()  # Initially hidden

# Button for Level 4
button_level4 = tk.Button(frame, text="Credit & Debit", command=level_4_button_click)
button_level4.grid(row=22, column=0, padx=5, pady=5)
button_level4.grid_remove()  # Initially hidden

# Button for Quiz4
button_quiz4 = tk.Button(frame, text="Quiz on Credit & Debit", command=quiz4_button_click)
button_quiz4.grid(row=24, column=1, padx=5, pady=5)
button_quiz4.grid_remove()  # Initially hidden

# Button for Level 5
button_level5 = tk.Button(frame, text="Budgeting", command=level_5_button_click)
button_level5.grid(row=26, column=0, padx=5, pady=5)
button_level5.grid_remove()  # Initially hidden

# Button for Quiz5
button_quiz5 = tk.Button(frame, text="Quiz on Budgeting", command=quiz5_button_click)
button_quiz5.grid(row=28, column=1, padx=5, pady=5)
button_quiz5.grid_remove()  # Initially hidden

# Define financial score descriptions
score_descriptions = {
    "Excellent": "Congratulations! You have excellent financial management skills.",
    "Good": "Well done! You have good financial management skills.",
    "Fair": "You have fair financial management skills. There is room for improvement.",
    "Poor": "Your financial management skills need improvement. Consider learning more about financial planning.",
    "Very Poor": "Your financial management skills need significant improvement. Seek guidance to improve your financial literacy."
}

# Function to get financial score description based on the score
def get_score_description(score):
    if score >= 100:
        return score_descriptions["Excellent"]
    elif score >= 80:
        return score_descriptions["Good"]
    elif score >= 50:
        return score_descriptions["Fair"]
    elif score >= 0:
        return score_descriptions["Poor"]
    else:
        return score_descriptions["Very Poor"]

# Function to display financial score description
def display_score_description(score):
    description = get_score_description(score)
    score_description_label.config(text=description)
    score_description_label.grid(row=11, column=0, columnspan=2, padx=10, pady=5)  

# Labels for financial score and description (initially hidden)
score_description_label = tk.Label(frame, text="")

# Button for back to menu
button_back_to_menu = tk.Button(frame, text="Back to Menu", command=back_to_menu)

# Restart button
restart_button = tk.Button(frame, text="Restart Decision", command=restart_game)

# Start the game
window.mainloop()



