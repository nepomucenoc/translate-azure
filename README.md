# 🌍 Translate Azure

A simple project that translates text using the Microsoft Translator Text API (Azure Cognitive Services).

## ✨ Features

This script translates phrases from English to other languages using the Azure API. You can configure the target languages in the code.

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
## 📦Dependencies:
- requests
- python-dotenv

## 🛡️ Security
Sensitive variables, such as the API key, are not versioned (they are ignored via .gitignore) and should be manually added to the .env file.