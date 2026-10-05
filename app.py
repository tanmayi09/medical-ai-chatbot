from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


medical_responses = {
    "fever": "Common symptoms of fever may include increased body temperature, chills, sweating, headache, weakness, and tiredness. If the fever is severe or persistent, consult a healthcare professional.",

    "cold": "Common cold symptoms may include a runny or blocked nose, sneezing, sore throat, cough, and mild tiredness. Rest and staying hydrated can help. Consult a doctor if symptoms become severe.",

    "headache": "Headaches can have many causes, including stress, lack of sleep, dehydration, or illness. Rest, hydration, and adequate sleep may help. Seek medical attention if the headache is sudden, severe, or unusual.",

    "cough": "A cough can occur due to a cold, allergies, infection, or other conditions. Staying hydrated may help. If the cough is severe, persistent, or accompanied by difficulty breathing, seek medical care.",

    "stomach pain": "Stomach pain can have many causes, including indigestion, infection, or food-related problems. If the pain is severe, persistent, or accompanied by vomiting or bleeding, seek medical attention.",

    "diabetes": "Diabetes is a condition that affects how the body manages blood sugar. Common symptoms can include increased thirst, frequent urination, tiredness, and unexplained weight changes. A healthcare professional can provide proper testing and diagnosis.",

    "blood pressure": "High blood pressure often does not cause noticeable symptoms. Regular blood pressure checks are important. A healthcare professional can help interpret your blood pressure readings and recommend appropriate care.",

    "flu": "Flu symptoms can include fever, chills, cough, sore throat, body aches, headache, and tiredness. Rest and fluids can help, but seek medical care if symptoms are severe.",

    "allergy": "Allergy symptoms may include sneezing, itching, runny nose, skin rashes, or watery eyes. Severe allergic reactions involving breathing difficulties require immediate emergency medical attention.",

    "covid": "Common COVID-19 symptoms can include fever, cough, sore throat, tiredness, and changes in taste or smell. Testing and medical advice may be appropriate depending on the symptoms and situation."
}


def generate_response(message):
    message = message.lower()

    for keyword, response in medical_responses.items():
        if keyword in message:
            return response

    if "hello" in message or "hi" in message or "hey" in message:
        return "Hello! I am your medical information assistant. You can ask me about common health topics such as fever, cold, cough, headache, diabetes, allergies, and more."

    if "thank" in message:
        return "You're welcome! Take care and stay healthy."

    return (
        "I can provide general information about common health topics such as "
        "fever, cold, cough, headache, diabetes, blood pressure, flu, and allergies. "
        "Please ask me about one of these topics."
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"reply": "Please enter a question."}), 400

    response = generate_response(user_message)

    return jsonify({"reply": response})


if __name__ == "__main__":
    app.run(debug=True)