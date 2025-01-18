import speech_recognition as sr
import streamlit as st

# Initialize recognizer
recognizer = sr.Recognizer()

# Available APIs
api_choices = ["Google Speech Recognition", "Sphinx", "IBM Watson"]

# Function to handle speech recognition
def transcribe_speech(recognizer, audio, api, language):
    try:
        if api == "Google Speech Recognition":
            return recognizer.recognize_google(audio, language=language)
        elif api == "Sphinx":
            return recognizer.recognize_sphinx(audio)
        elif api == "IBM Watson":
            # IBM Watson API requires a key, so you'll need to implement this based on your credentials
            # For this example, we'll assume the IBM Watson API is available
            return recognizer.recognize_ibm(audio, language=language)
        else:
            raise ValueError("Unsupported API selection")
    except sr.UnknownValueError:
        return "Could not understand the audio"
    except sr.RequestError as e:
        return f"Error with the API request; {e}"
    except Exception as e:
        return f"An error occurred: {e}"

# Function to save transcribed text to a file
def save_transcribed_text(text):
    with open("transcribed_text.txt", "w") as file:
        file.write(text)
    return "Text saved to transcribed_text.txt"

# Streamlit UI
def main():
    st.title("Speech Recognition App")
    
    st.write("""
        This app transcribes speech into text. You can choose the speech recognition API,
        select your preferred language, and even save the transcribed text to a file.
        """)

    # Choose the API
    api = st.selectbox("Choose the Speech Recognition API", api_choices)
    
    # Choose the language for recognition
    language = st.selectbox("Select Language", ["en-US", "es-ES", "fr-FR", "de-DE", "it-IT"])
    
    # Record and transcribe speech
    if st.button("Start Recording"):
        with sr.Microphone() as source:
            st.write("Listening... Please speak into the microphone.")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            st.write("Recognizing...")
            
            # Get transcription based on selected API
            text = transcribe_speech(recognizer, audio, api, language)
            st.write(f"Transcribed Text: {text}")
            
            # Option to save the transcribed text
            if st.button("Save Transcription"):
                result = save_transcribed_text(text)
                st.write(result)

    # Pause and resume feature (Simple simulation with buttons)
    if st.button("Pause"):
        st.write("Speech recognition paused.")
        # A real pause and resume implementation would be complex and depend on the API's capability.
        # This could involve stopping and resuming the microphone input stream.

    if st.button("Resume"):
        st.write("Speech recognition resumed.")
        # In reality, you'd continue the recording process here or start a new one.

if __name__ == "__main__":
    main()
