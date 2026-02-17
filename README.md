# Flashy – French Flashcard App 🧠🇫🇷

Flashy is a simple Python flashcard application built with **Tkinter** and **Pandas** to help you learn French vocabulary.  
The app shows French words, flips the card after a few seconds, and tracks the words you already know.

---

## 🚀 Features

- Displays random French words with flashcards  
- Automatically flips the card to show the English translation  
- Lets you mark words as **known** or **unknown**  
- Saves progress so you don’t repeat learned words  
- Clean and minimal UI with card images  

---

## 📂 Project Structure

Flashy/
│
├── data/
│ ├── french_words.csv
│ └── words_to_learn.csv
│
├── images/
│ ├── card_front.png
│ ├── card_back.png
│ ├── right.png
│ └── wrong.png
│
├── main.py
└── README.md


---

## 🛠️ Requirements

Make sure you have Python installed (3.8+ recommended).

Install required packages:

```bash
pip install pandas
Tkinter comes pre-installed with most Python versions.

▶️ How to Run
Clone the repository:

git clone https://github.com/yourusername/flashy.git
Go to the project folder:

cd flashy
Run the app:

python main.py
🧩 How It Works
The app loads words from french_words.csv

If words_to_learn.csv exists, it loads only the remaining words

After 3 seconds, the card flips to show the English meaning

Clicking ✅ removes the word from the learning list

Your progress is saved automatically

📸 Screenshots
(Add screenshots here later)

📌 Future Improvements
Add sound pronunciation

Add more languages

Progress stats dashboard

Dark mode

🤝 Contributing
Feel free to fork this project and improve it. Pull requests are welcome.

📜 License
This project is open-source and free to use for learning purposes.

Author
Abu Hurayra Farhan


---

If you want, I can also:
- Make a **short version** of the README  
- Add **badges (Python, MIT license, GitHub stars)**  
- Write a **professional project description for your resume or portfolio**
