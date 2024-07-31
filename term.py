import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style

quiz_data = [
   {
        "question": "what is a decrease in the purchasing power of money, reflected in a general increase in the prices of goods and services in an economy.",
        "choices": ['loan', 'inflation', 'deflation', 'demand'],
        "answer": 'inflation', 
        "ans_des": "Inflation refers to the rate at which the general level of prices for goods and services is rising, resulting in a decrease in the purchasing power of a currency."
    },
    {
        "question": "_____is type of investment in which an individual invests a lump sum amount for a specific period of time with a bank.?",
        "choices": ['fixed deposits', 'Recurrent deposits', 'Equated Monthly Instalment.', 'Mutal funds'],
        "answer": 'fixed deposits', 
        "ans_des": "Fixed deposits are financial instruments where an individual invests a sum of money with a bank or financial institution for a predetermined period at a fixed interest rate, providing a guaranteed return upon maturity."
    },
    {
        "question": "_____ market consists of exchanges in which stock shares and other financial securities of publicly held companies are bought and sold.?",
        "choices": ['Stock market', 'Bond Shop', 'Real estate', 'gold shop'],
        "answer": 'Stock market',  
        "ans_des" :"The stock market is a platform where shares of publicly traded companies are bought and sold, facilitating investment and capital raising. It serves as a crucial component of the economy, influencing corporate growth, investor wealth, and overall financial stability."
    },
    {
    
        "question": "what is a term that explains purchase of one security and simultaneous sale of another to give a risk-free profit",
        "choices": ['arbitrage', 'asset beta', 'basis risk', 'carve-out'],
        "answer": 'arbitrage', 
        "ans_des": "arbitage is the act of purchase of one security and simultaneous sale of another to give a risk-free profit. often used loosely to describe the taking of offsetting positions in related securities, e.g., at the time of a takeover bid.."
    },
    {
        "question": "what is the full form of dcf",
        "choices": ['discounted cash flow', 'coupon', 'economic income', 'exchange traded fund'],
        "answer": 'discounted cash flow', 
        "ans_des": "Discounted cash flow (DCF) refers to a valuation method that estimates the value of an investment using its expected future cash flows."
    },
    {
        "question": "what is  a network of japanese companies organized around a major bank.?",
        "choices": ['ICIC', 'RBI', 'JBA', 'keiretsu'],
        "answer": 'keiretsu',  
        "ans_des" :"A keiretsu is an interdependent group of companies, each with its own banking partner, manufacturers, distributors, and supply chain partners"
    },
    {
        "question": "what are the Taxes on imported goods called as.?",
        "choices": ['tariffs', 'Customs Duty', 'Travel tax', 'toll'],
        "answer": 'Stock market',  
        "ans_des" :"A tariff is a tax imposed by the government of a country or by a supranational union on imports or exports of goods."
    },
    {
        "question": "What is considered as a security with a specified maturity date.",
        "choices": ['term security', 'cyber security', 'equity', 'novality'],
        "answer": 'term security',  
        "ans_des" :"A security is a fungible, negotiable financial instrument that represents some type of financial value, usually in the form of a stock, bond, or option.."
    }
    

]

def show_question():
    question = quiz_data[current_question]
    qs_label.config(text=question['question']) 
    choices = question['choices']
    for i in range(4):
        choice_btns[i].config(text=choices[i], state='normal')
    
    feedback_label.config(text="")
    next_btn.config(state='disabled')

def check_answer(choice):
    question = quiz_data[current_question] 
    selected_choice = choice_btns[choice].cget("text") 
    if selected_choice == question['answer']:
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        ans_des_text2 = quiz_data[current_question]['ans_des']
        feedback_label.config(text=f'Correct!\n { ans_des_text2 }', foreground='green')
    else:
        feedback_label.config(text='Incorrect!', foreground='red') 
        ans_des_text = quiz_data[current_question]['ans_des']
        # Display incorrect message and answer description in separate lines
        feedback_label.config(text=f"Incorrect!\n{ans_des_text}", foreground='red', wraplength=1000) 
    
    # Disable all choice buttons and enable next button
    for button in choice_btns:
        button.config(state='disabled')
    next_btn.config(state="normal")

def next_question():
    global current_question
    current_question += 1 

    if current_question < len(quiz_data):
        # If there any questions, display them
        show_question()
    else:
        # If all the questions are shown, end quiz
        messagebox.showinfo("Quiz completed",
                            'Quiz Completed! Final score: {}/{}'.format(score, len(quiz_data))) 
        root.destroy()

root = tk.Tk()
root.title("Quiz App")
root.geometry("600x500")
style = Style(theme='flatly')

style.configure("TLabel", font=("Times Roman", 20))
style.configure("TButton", font=("Times Roman", 18))

qs_label = ttk.Label(
    root,
    anchor='center',
    wraplength=500,
    padding=10
) 
qs_label.pack(pady=10)

choice_btns = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: check_answer(i)
    ) 
    button.pack(pady=5)
    choice_btns.append(button)

feedback_label = ttk.Label(
    root,
    anchor='center',
    padding=10
)
feedback_label.pack(pady=10) 

score = 0

score_label = ttk.Label(
    root,
    text='Score: 0/{}'.format(len(quiz_data)),
    anchor='center',
    padding=10
)  
score_label.pack(pady=10)

next_btn = ttk.Button(
    root,
    text='Next',
    command=next_question,
    state='disabled'
)
next_btn.pack(pady=10) 

current_question = 0

show_question()

root.mainloop()
