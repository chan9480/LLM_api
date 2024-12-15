import google.generativeai as genai

GOOGLE_API_KEY="AIzaSyDNrDtHF2TjvJI6LdVHfjEq6O7HjQGKyqM"

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

while True:
    message = input("메시지를 입력하세요: ")
    if (message == "exit"):
        break
    response = chat.send_message(message)
    print("-----gemini-pro-----")
    print(response.text)