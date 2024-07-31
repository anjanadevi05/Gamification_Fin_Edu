const questions = [
    {
        question: "What does collateral-free mean in the context of education loans?",
        options: ["No need to repay the loan", "No security or guarantee required", "Loan interest is waived off", "The loan is granted only to students with high grades"],
        answer: "No security or guarantee required",
        description: "Collateral-free refers to the absence of the requirement for providing any form of security or guarantee in order to obtain an education loan. This means that the borrower does not need to pledge any assets or provide a guarantor to secure the loan. The lender grants the loan solely based on the borrower's creditworthiness and ability to repay, without the need for any additional collateral."
    },
    {
        question: "Which financial institution provides collateral-free education loans in many countries?",
        options: ["World Bank", "International Monetary Fund (IMF)", "Reserve Bank of India (RBI)", "Non-Banking Financial Company (NBFC)"],
        answer: "Reserve Bank of India (RBI)",
        description: "The Reserve Bank of India (RBI) provides collateral-free education loans in many countries. This means that students can obtain loans for their education without having to provide any form of collateral or security. The RBI's initiative aims to make education more accessible and affordable for students, allowing them to pursue their academic goals without the burden of collateral requirements."
    },
    {
        question: "Which of the following is NOT a benefit of collateral-free education loans?",
        options: ["No need for a guarantor", "Low interest rates", "Flexible repayment options", "No need for a co-applicant"],
        answer: "No need for a co-applicant",
        description: "This is not a benefit of collateral-free education loans because even though these loans do not require collateral or a guarantor, they still typically require a co-applicant. A co-applicant is usually a parent or guardian who agrees to take joint responsibility for repaying the loan if the primary borrower is unable to do so."
    },
    {
        question: "Which document is typically required to apply for a collateral-free education loan?",
        options: ["Passport", "Property deed", "Income tax return", "Educational certificates"],
        answer: "Educational certificates",
        description: "Educational certificates are typically required to apply for a collateral-free education loan. This is because the lender needs to verify the educational qualifications of the borrower to assess their eligibility for the loan. The certificates provide evidence of the borrower's educational background and help the lender determine the likelihood of the borrower successfully completing their education and being able to repay the loan in the future. Additionally, educational certificates also serve as a proof of the borrower's commitment to their education, which can further strengthen their loan application"
    },
    {
        question: "What is the maximum loan amount offered for collateral-free education loans?",
        options: ["Rs:100000", "Rs:500000", "Rs.1000000", "There is no fixed maximum limit."],
        answer: "There is no fixed maximum limit.",
        description: "There is no fixed maximum limit. This means that there is no specific maximum loan amount offered for collateral-free education loans. The loan amount can vary depending on various factors such as the borrower's creditworthiness, the educational institution, and the loan provider's policies. This flexibility allows borrowers to potentially secure higher loan amounts based on their individual circumstances."
    }
    
];

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
