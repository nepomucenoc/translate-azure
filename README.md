# 🌍 Translate Azure

A simple, yet powerful script that leverages the Microsoft Translator Text API (Azure Cognitive Services) to translate text from English to multiple languages. This tool is designed to be flexible and easy to use, with the goal of automating translation tasks seamlessly.


## ✨ Features

This script can translate phrases from English to any language supported by the Azure API. You can easily modify the target languages in the script to suit your needs.

## ⚙️ How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/nepomucenoc/translate-azure.git
   cd translate-azure
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   ```
3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up the sensitive variables: Create a .env file and add:**
   ```env
   KEY=your-key-here
   ENDPOINT=https://api.cognitive.microsofttranslator.com
   LOCATION=eastus
   ```
5. **Run the script:**
   ```bash
   python translate-azure.py 
   ```
6. **Answers:**
   ```bash
      [
      {
         "translations": [
               {
                  "text": "La traduction n’est pas seulement une question de mots, il s’agit de transmettre le vrai sens à travers les langues !",
                  "to": "fr"
               },
               {
                  "text": "Beim Übersetzen geht es nicht nur um Worte, sondern darum, die wahre Bedeutung sprachübergreifend zu vermitteln!",
                  "to": "de"
               },
               {
                  "text": "A tradução não é apenas sobre palavras, é sobre transmitir o verdadeiro significado através das línguas!",
                  "to": "pt"
               }
         ]
      }
   ]
   ```
## 📦Dependencies:
- requests
- python-dotenv

## 🛡️ Security
Sensitive variables, such as the API key, are not versioned (they are ignored via .gitignore) and should be manually added to the .env file.