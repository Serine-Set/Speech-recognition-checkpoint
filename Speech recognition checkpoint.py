# What You're Aiming For
# Improve the Speech Recognition App

# In this exercise, you will improve the Speech Recognition App by adding some features to enhance its functionality.

# Instructions
# Include a new option for users to select the speech recognition API they want to use. In addition to Google Speech Recognition, consider other APIs available in the provided libraries.
# Improve the error handling in the transcribe_speech() function to provide more meaningful error messages to the user.
# Add a feature to allow the user to save the transcribed text to a file.
# Add a feature to allow the user to choose the language they are speaking in, and configure the speech recognition API to use that language.
# Add a feature to allow the user to pause and resume the speech recognition process.
# Note:

# When adding new features, be sure to test the app thoroughly to ensure that it is working correctly. 
# Also, consider the user experience and design the app to be intuitive and easy to use. 
# Finally, if you encounter any issues or challenges, don't hesitate to consult the documentation or seek help from the community.

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

    if st.button("Resume"):
        st.write("Speech recognition resumed.")

if __name__ == "__main__":
    main()
