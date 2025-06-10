
# 🤖 AI-Powered Google Form Auto-Filler

This project uses **Python**, **spaCy**, **Tkinter**, and **Selenium** to automatically extract personal details from a user (via GUI or PDF Resume) and auto-fill them into a **Google Form** using a given link.

---

## 🚀 Features

- 📥 Extract personal data from a resume (PDF)
- 🧑‍💻 Enter details manually via GUI
- 🌐 Auto-fill Google Forms using Selenium WebDriver
- ✅ Supports fields like Name, Email, Phone, DOB, Address
- 💡 Easy-to-use interface with minimal setup

---

## 🧠 Technologies Used

- Python 3.8+
- spaCy NLP (`en_core_web_sm`)
- PyMuPDF (`fitz`)
- Tkinter (GUI)
- Selenium (Browser automation)
- Chrome WebDriver

## 📁 Project Structure

AI-GoogleFormFiller/
├── main.py                # GUI + Controller

├── form_filler.py         # Selenium-based form filler

├── extract_data.py        # Resume parser using spaCy + PyMuPDF

├── requirements.txt       # All required libraries

├── README.md              # This file

## 💻 Create Virtual Environment (Recommended)

python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

## 📥 Install Dependencies

pip install -r requirements.txt
python -m spacy download en_core_web_sm

## 🙋‍♀️ Author
Trishna Kumari Paswan
