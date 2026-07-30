import random

print("नमस्ते/Namaste! I am your Hindi Buddy.☺️ 🙏")
print("I will help you learn your mother tongue Hindi.")

# Ask for name
while True:
    name = input("What is your name? ").strip()
    if name:
        break
    print("Please enter your name to start learning Hindi.")

print(f"Hi, {name}! Let's start learning Hindi.")

# Clean vocabulary
words = {
    "नमस्ते": "Hello",
    "धन्यवाद": "Thank you",
    "कृपया": "Please",
    "मुझे माफ़ करें": "Excuse me",
    "आप कैसे हैं?": "How are you?",
    "मेरा नाम ... है।": "My name is ...",
    "मैं ठीक हूँ।": "I am fine.",
    "आपका स्वागत है।": "You're welcome.",
    "शुभकामनाएँ।": "Best wishes.",
    "अलविदा।": "Goodbye.",
    "शुभ प्रभात": "Good morning",
    "शुभ रात्रि": "Good night",
    "हाँ": "Yes",
    "नहीं": "No",
    "फिर मिलेंगे": "See you again",
    "क्या हाल है?": "What's up?",
    "सब ठीक है": "Everything is fine",
    "कोई बात नहीं": "No problem / It's okay",
    "बधाई हो": "Congratulations",
    "मुझे खेद है": "I am sorry",
    "चिंता मत करो": "Don't worry",
    "ध्यान रखना": "Take care",
    "बिल्कुल": "Absolutely",
    "शायद": "Maybe",
    "यह क्या है?": "What is this?",
    "आप कहाँ हैं?": "Where are you?",
    "मुझे मदद चाहिए": "I need help",
    "शौचालय कहाँ है?": "Where is the restroom?",
    "इसका दाम क्या है?": "How much does this cost?",
    "मुझे समझ नहीं आया": "I didn't understand",
    "क्या आप अंग्रेजी बोलते हैं?": "Do you speak English?",
    "पानी": "Water",
    "खाना": "Food",
    "घर": "Home / House",
    "दुकान": "Shop / Store",
    "गाड़ी": "Car / Vehicle",
    "किताब": "Book",
    "दोस्त": "Friend",
    "समय": "Time",
    "आज": "Today",
    "कल": "Tomorrow / Yesterday",
}

print("\nLet's start the quiz! I will ask you 5 questions. Try to answer them correctly. Good luck!🍀🍀🍀")

score = 0
questions = random.sample(list(words.items()), 5)

for i, (hindi, eng) in enumerate(questions, start=1):
    print("\n" + "="*45)
    print(f"Question {i}")
    print("="*45)
    print(f"\n   Hindi word  →   {hindi}")
    print("\nWhat is the English translation?")
    
    answer = input("Your answer: ").strip()

   
    def clean(text):
        text = text.lower()
        for ch in ".,!?;:'’\"()-":
            text = text.replace(ch, "")
        text = " ".join(text.split())
        return text

    user_clean = clean(answer)
    correct_clean = clean(eng)

    is_correct = False

    if user_clean == correct_clean:
        is_correct = True
    elif " / " in eng:
        options = [clean(opt) for opt in eng.split(" / ")]
        if user_clean in options:
            is_correct = True
    if not is_correct:
        if "no problem" in correct_clean or "its okay" in correct_clean:
            accepted = ["its ok", "its okay", "okay", "ok", "no problem"]
            if user_clean in accepted:
                is_correct = True
    

    if is_correct:
        print("Correct!👍")
        score += 1
    else:
        print(f"Wrong!👎 The correct answer is: {eng}")

print(f"\nYour final score is: {score}/5🏆")
print("Thank you for practicing Hindi with me! Keep learning and improving your skills.😊")
print("Goodbye!👋 Have a great day!")
print("Run the program again to practice more words, phrases, sentences in Hindi.📚")