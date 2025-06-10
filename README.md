# 📚 Book Recommendation System

A smart and interactive Book Recommendation System built with **Streamlit** that suggests books based on your favorite reads using collaborative filtering and cosine similarity.

---

## 🚀 Live Demo

👉 [Click here to try the live app](https://book-recommendation-pratyaksh.streamlit.app/)

---

## 🧠 How It Works

- Takes a book name as input from the user.
- Matches it with the closest title using fuzzy matching.
- Uses a precomputed similarity matrix to recommend similar books.
- Optional: Filter results by genre.
- Handles vague names like _“harry potter”_ and shows thumbnails for better UX.

---

## 🎯 Features

🔍 Input-based recommendation

🎭 Optional genre filter

📈 Popular books section

🧠 Fuzzy matching for vague inputs

🖼️ Book thumbnails and author info

⚠️ Warning system for genre mismatches or unknown books

---

## 🛠️ Technologies Used

- Python 
- Pandas
- Scikit-learn
- Streamlit
- Pickle
- Difflib
- Cosine Similarity

---

## 📂 Project Structure

├── app.py # Streamlit app

├── filtered_books.pkl # Book metadata with images and genre

├── pt.pkl # Pivot table for book-user matrix

├── similarities.zip # Compressed similarity matrix

├── requirements.txt # Python dependencies

└── README.md 

---

## 🖥️ Running Locally

### 🔧 Prerequisites
Make sure you have Python 3.x and `pip` installed.

### ⬇️ Step-by-step Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/Book-Recommendation.git
cd book-recommendation-system
```
2. **Install Dependencies**

```bash
pip install -r requirements.txt
```
3. **Run the App**

```bash
streamlit run app.py
```

## 💡 Deployment Notes
Since similarities.pkl is larger than GitHub’s file limit (25 MB), it is compressed into a .zip file. Ensure it’s unzipped before running locally or deploying to Streamlit Cloud.

## 📊 Dataset Used
[Kaggle Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)

## 📌 Limitations
- Some thumbnails may not render due to external hosting issues.
- Book names must be reasonably accurate unless covered in manual mappings.
- Genre assignment is manually mapped and may miss some edge cases.

## ✨ Future Enhancements

✅ Add genre filters (Done)

✅ Add fallback recommendations (Done)

✅ Handle vague queries like "harry potter" (Done)

🔄 Use live APIs (e.g., Google Books) for dynamic metadata

🌐 Add multilingual support

⭐ Add user login + favorites tracking

## 🙌 Acknowledgements
Thanks to Kaggle for the dataset

Inspired by content-based & collaborative filtering concepts

Special thanks to Streamlit for rapid UI prototyping

## 👤 Author
Pratyaksh Agrawal

📬 [LinkedIn](https://www.linkedin.com/in/pratyaksh-agrawal-59b82928a/) 

Made with ❤️ using Python and Streamlit

## 📎 License
This project is open-source and available under the MIT License.


