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
    },
    {
        question: "In collateral-free education loans, the repayment period typically ranges from how many years?",
        options: ["1 year to 5 years", "5 years to 10 years", "10 years to 15 years", "15 years to 20 years"],
        answer: "10 years to 15 years",
        description: "In collateral-free education loans, the repayment period is usually longer compared to other types of loans. This is because education loans are designed to provide students with a flexible repayment option, considering that they may not have a stable income immediately after completing their education. The repayment period of 10 to 15 years allows borrowers to have a reasonable timeframe to repay the loan without putting excessive financial burden on them."
    },
    {
        question: "Education loans are primarily offered for which educational purposes?",
        options: ["Tuition fees and living expenses", "Research and development projects", "Purchase of educational equipment", "Educational tours and extracurricular activities"],
        answer: "Tuition fees and living expenses",
        description: "Collateral-free education loans are primarily offered for covering the tuition fees and living expenses of students. These loans provide financial assistance to students who may not have any collateral or security to offer. By covering these expenses, the loans help students pursue their education without the burden of immediate financial obligations. This allows students to focus on their studies and alleviate the financial stress that often comes with pursuing higher education"
    },
    {
        question: "What is the interest rate typically associated with collateral-free education loans?",
        options: ["0% interest", "Prime lending rate (PLR)", "5% above the base rate", "Varies from bank to bank"],
        answer: "Varies from bank to bank",
        description: "The interest rate typically associated with collateral-free education loans varies from bank to bank. This means that different banks may offer different interest rates for these types of loans. The specific interest rate offered by a bank may depend on various factors such as the borrower's credit history, income level, and the bank's own policies. Therefore, it is important for individuals seeking education loans to research and compare the interest rates offered by different banks to find the most favorable option for their needs"
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
        document.getElementById("question").textContent = "Quiz Completed! Your Score: " + score + "/80";
        document.getElementById("options").innerHTML = "";
        document.getElementById("nextBtn").style.display = "none";
        // Display reference materials
        const referenceSection = document.createElement("div");
        referenceSection.innerHTML = "<h2>Refer the following content to know more on student loans</h2>";
        
        // You can add links or descriptions to relevant resources here
        referenceSection.innerHTML += "<p>Learn more about education loans <a href='https://www.youtube.com/watch?v=FyLRxU5mJPM'>here</a>.</p>";
        document.body.appendChild(referenceSection);
    }
}

// Display the first question when the page loads
displayQuestion();
