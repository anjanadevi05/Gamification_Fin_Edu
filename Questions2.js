const questions = [
    {
        question: "How is the savings rate calculated based on the information provided?",
        options: ["By dividing total expenses by disposable income", "By dividing savings by total income", " By subtracting expenses from savings","By dividing savings by disposable income and multiplying by 100"],
        answer: "By dividing savings by disposable income and multiplying by 100",
        description: "The savings rate is calculated by dividing the savings by disposable income and then multiplying the result by 100,This formula helps to determine the percentage of disposable personal income that is saved rather than spent on consumption or obligations."
    },
    {
        question: "What is the average personal savings rate in India?",
        options: ["20.5%", "30.2%", "18.4%", "45%"],
        answer: "30.2%",
        description: "India Gross Savings Rate was measured at 30.2% in Mar 2023, compared with 30.2% in the previous year.The personal saving rate is the percentage of disposable income that people save. It is calculated by dividing the monthly savings amount by the monthly gross income, and then multiplying that decimal by 100."
    },
    {
        question: "What is the recommended rule of thumb for emergency savings?",
        options: ["Save enough to cover one month's worth of expenses", "Save enough to cover three to six months' worth of expenses", "Save enough to cover one year's worth of expenses", "Save enough to cover all expenses indefinitely"],
        answer: "Save enough to cover three to six months' worth of expenses",
        description: "This recommendation is based on the idea that having an emergency fund equivalent to three to six months' worth of expenses provides a financial cushion to cover unexpected expenses or financial emergencies without having to rely on credit cards or loans."
    },
    {
        question: "What is the main purpose of a savings account?",
        options: ["To earn interest on your balance", "To make everyday purchases and withdrawals", "To separate money from everyday spending to avoid impulse purchases.", "To store funds securely for future use or emergencies."],
        answer: "To earn interest on your balance",
        description: " A savings account is designed to hold money you don’t plan to spend immediately and allows you to earn interest on your balance"
    },
    {
        question: "What is the limit on the number of withdrawal transactions you can make from a savings account per month",
        options: ["Upto 5 withdrawals", "Upto 10 withdrawals", "Upto 15 withdrawal", "There is no fixed maximum limit."],
        answer: "Upto 10 withdrawals",
        description: "Many banks allow up to 10 free withdrawals per month to provide flexibility for routine transactions."
    }    ];

let currentQuestion = 0;
let score = 0;

function displayQuestion() {
    const questionElement = document.getElementById("question");
    const optionsElement = document.getElementById("options");
    const progressElement = document.getElementById("progress");
    const questionNumberElement = document.getElementById("questionNumber");

    questionElement.textContent = questions[currentQuestion].question;
    progressElement.style.width = ((currentQuestion + 1) / questions.length) * 100 + '%';
    questionNumberElement.textContent = `Question ${currentQuestion + 1} / ${questions.length}`;
    optionsElement.innerHTML = "";

    questions[currentQuestion].options.forEach(option => {
        const button = document.createElement("button");
        button.textContent = option;
        button.onclick = function() { checkAnswer(option); };
        optionsElement.appendChild(button);
    });
}

function checkAnswer(selectedOption) {
    const resultElement = document.getElementById("result");
    const correctAnswer = questions[currentQuestion].answer;

    if (selectedOption === correctAnswer) {
        score += 10;
        resultElement.textContent = "Correct! " + questions[currentQuestion].description;
    } else {
        const incorrectMessage = "Incorrect. The correct answer is: " + correctAnswer + ". " + questions[currentQuestion].description;
        resultElement.textContent = incorrectMessage;
    }
}

function nextQuestion() {
    const resultElement = document.getElementById("result");
    resultElement.textContent = "";

    currentQuestion++;

    if (currentQuestion < questions.length) {
        displayQuestion();
    } else {
        // Display final score
        document.getElementById("question").textContent = "Quiz Completed! Your Score: " + score + "/50";
        document.getElementById("options").innerHTML = "";
        document.getElementById("nextBtn").style.display = "none";
    }
}

// Display the first question when the page loads
displayQuestion();
