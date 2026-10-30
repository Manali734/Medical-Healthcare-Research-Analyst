const question = document.querySelector("#question");
const askButton = document.querySelector("#askButton");
const counter = document.querySelector("#counter");
const resultPanel = document.querySelector("#resultPanel");
const answerBox = document.querySelector("#answer");
const sourcesBox = document.querySelector("#sources");
const disclaimerBox = document.querySelector("#disclaimer");
const resultStatus = document.querySelector("#resultStatus");

question.addEventListener("input", () => {
  counter.textContent = `${question.value.length} / 2000`;
});

document.querySelectorAll("[data-question]").forEach(button => {
  button.addEventListener("click", () => {
    question.value = button.dataset.question;
    counter.textContent = `${question.value.length} / 2000`;
    question.focus();
  });
});

askButton.addEventListener("click", async () => {
  const value = question.value.trim();
  if (value.length < 5) {
    alert("Please enter a question containing at least 5 characters.");
    return;
  }
  resultPanel.classList.remove("hidden");
  answerBox.textContent = "Analyzing the question, consulting the reference library, and reviewing the response…";
  sourcesBox.replaceChildren();
  disclaimerBox.textContent = "";
  resultStatus.textContent = "Working";
  askButton.disabled = true;
  try {
    const response = await fetch("/ask", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({question: value})
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.detail || "Request failed");
    // Use textContent rather than injecting model output as HTML.
    answerBox.textContent = data.answer;
    (data.sources || []).forEach(source => {
      const li = document.createElement("li");
      li.textContent = source;
      sourcesBox.appendChild(li);
    });
    disclaimerBox.textContent = data.disclaimer || "";
    resultStatus.textContent = "Complete";
  } catch (error) {
    answerBox.textContent = `Unable to complete the request: ${error.message}`;
    resultStatus.textContent = "Error";
  } finally {
    askButton.disabled = false;
  }
});
