import nltk
nltk.download('punkt')
nltk.download('wordnet')
import random
import string
from nltk.chat.util import Chat, reflections
from fpdf import FPDF
from datetime import datetime

pairs = [
    [
        r"(hi|hello|hey|hii|hiii)",
        ["Hello! How can I assist you today?", "Hi there! What can I do for you?"]
    ],
    [
        r"(.*)(your name|who are you)",
        ["I am CodTech's AI Chatbot created for internship queries."]
    ],
    [
        r"(.*)(help|support)",
        ["Sure, I'm here to help! Please tell me your issue."]
    ],
    [
        r"(.*)(internship|certificate|completion)",
        ["You will receive your internship certificate upon completion."]
    ],
    [
        r"(.*)(thank you|thanks|thx)",
        ["You're welcome!", "No problem!"]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a great day!", "See you soon!"]
    ]
]

def start_chatbot():
    print("🤖 CodTech Chatbot: Hello! I am your AI assistant. (type 'exit' to quit)\n")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

def generate_certificate(name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "COMPLETION CERTIFICATE", ln=True, align="C")

    pdf.ln(20)
    pdf.set_font("Arial", "", 12)
    text = (
        f"This is to certify that {name} has successfully completed the internship at CodTech.\n\n"
        f"The internship concluded on {datetime.today().strftime('%d-%m-%Y')}.\n\n"
        f"We appreciate your hard work and dedication.\n\n"
        f"Best wishes,\nCodTech Team"
    )
    pdf.multi_cell(0, 10, text, align="C")
    pdf.output("CodTech_Certificate.pdf")
    print("\n🎉 Certificate generated: CodTech_Certificate.pdf")

if __name__ == "__main__":
    user_name = input("Enter your name to begin your internship chatbot session: ")
    start_chatbot()
    generate_certificate(user_name)
