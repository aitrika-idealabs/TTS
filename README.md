# **Text-to-Speech Conversion with OpenAI - README**

---

## **What the Code Does**
This project is a **Streamlit web application** that takes user-provided text as input and converts it into lifelike spoken audio using **OpenAI’s Text-to-Speech API**. Users can select different AI-generated voices and audio formats, generate the speech, and play the output directly within the app.

---

## **How to Use It (Step by Step)**

1. **Install the Required Dependencies:**
   - Install **Streamlit** and **Requests** using pip:
     ```bash
     pip install streamlit requests
     ```

2. **Set Up API Credentials:**
   - Create a `.streamlit/secrets.toml` file in the root of your project.
   - Add your **OpenAI API key** as shown below:
     ```toml
     OPENAI_API_KEY = "your_openai_api_key"
     ```

3. **Run the Streamlit App:**
   - Navigate to the project directory and run:
     ```bash
     streamlit run app.py
     ```

4. **Interact with the App:**
   - Open the app in your web browser.
   - Enter the text you want to convert to speech.
   - Select a voice and audio format.
   - Click the **"Convert to Speech"** button to generate and play the audio output.

---

## **What Happens in Each Step**

1. **User Interface Setup:**
   - The Streamlit app initializes with a title and description using `st.title()` and `st.write()`.

2. **API Key Setup:**
   - The API key is securely fetched from the `secrets.toml` file using `st.secrets["OPENAI_API_KEY"]`.

3. **User Input Collection:**
   - The app prompts the user to enter the text using a text area (`st.text_area()`).
   - It also provides dropdowns and radio buttons to select the desired voice and audio format.

4. **Sending Request to OpenAI API:**
   - When the **"Convert to Speech"** button is clicked, the app prepares a JSON payload with the input text, selected voice, and format.
   - It sends a POST request to the OpenAI API to generate the audio.

5. **Receiving and Saving the Audio:**
   - If the request is successful, the app saves the audio content to a local file in the selected format.

6. **Playing the Audio:**
   - The generated audio is played back directly within the app using `st.audio()`.

---

## **Role of Each File in the Project Structure**

```
project-directory/
│
├── app.py                  # Main Python script to run the Streamlit app
│
├── .streamlit/
│   └── secrets.toml        # Contains the API key for secure access to OpenAI’s API
│
└── requirements.txt        # Optional: List of dependencies for the project
```

### **File Details:**

1. **`app.py`:**  
   The main application script where the UI is defined, user inputs are handled, and the API request is made. This is the file you run using `streamlit run app.py`.

2. **`.streamlit/secrets.toml`:**  
   A configuration file used by Streamlit to store sensitive information, such as API keys, in a secure manner. This file should **never** be shared publicly.

   Example:
   ```toml
   OPENAI_API_KEY = "your_openai_api_key"
   ```

3. **`requirements.txt` :**  
   If you want to deploy the app or ensure consistent environments, you can create this file by running:
   ```bash
   pip freeze > requirements.txt
   ```
   The file typically includes:
   ```
   streamlit
   requests
   ```

---

## **Screenshots**
![image](https://github.com/user-attachments/assets/7ce11808-4d79-42b7-9320-e93044e9b066)



## **Conclusion**
This project demonstrates how to easily integrate OpenAI’s Text-to-Speech API within a Streamlit application to create an interactive audio generation tool. With customizable voices and formats, this app can be used for many applications like narration, language learning, or accessibility tools. 
