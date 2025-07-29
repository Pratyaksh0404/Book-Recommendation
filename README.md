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
```bash
book-recommendation-system/
│
├── .devcontainer/                  # (Optional) VS Code Dev Container config
├── Books.zip                       # Zipped folder containing book metadata
├── Ratings.csv                     # Dataset: User ratings for books
├── Users.csv                       # Dataset: User metadata
├── app.py                          # Flask or Streamlit app for web interface
├── book-recommendation-system.ipynb # Jupyter notebook with code and EDA
├── filtered_books.pkl              # Pickle file of filtered book metadata
├── pt.pkl                          # Pickle file of pivot table or model
├── similarities.zip                # Zipped similarity matrix/model
├── requirements.txt                # List of Python dependencies
└── README.md                       # Project documentation
```

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


