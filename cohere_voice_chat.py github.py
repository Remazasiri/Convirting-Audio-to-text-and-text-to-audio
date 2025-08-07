import cohere
import pyttsx3

co = cohere.Client("b2fqjNACS5GoJxwsqJz8mxfh9xFTp0x7plpH5AS5") 

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def main():
    print("🚀 البرنامج بدأ!")
    while True:
        try:
            text = input("أنت: ")
            if text.lower() in ["خروج", "exit", "quit"]:
                print("مع السلامة!")
                break

            print("🔎 جاري المعالجة...")
            response = co.chat(
                message=text,
                model="command-r7b-arabic-02-2025",
                preamble="You are a helpful AI assistant. Always answer with less than 15 words."
            )

            answer = response.text.strip()
            print("المساعد:", answer)
            speak(answer)

        except KeyboardInterrupt:
            print("
تم الإنهاء يدويًا.")
            break

if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()
    main()
