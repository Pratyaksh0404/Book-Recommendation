import streamlit as st
import pandas as pd
import numpy as np
import pickle
from difflib import get_close_matches
import zipfile
import os

# --- Safe unzip and load ---
if not os.path.exists("similarities.pkl"):
    if os.path.exists("similarities.zip"):
        with zipfile.ZipFile("similarities.zip", 'r') as zip_ref:
            zip_ref.extractall(".")
    else:
        st.error("❌ Missing both similarities.pkl and similarities.zip!")
        st.stop()

with open("similarities.pkl", "rb") as f:
    similarity_scores = pickle.load(f)

# --- Load Pickle Files ---
pt = pickle.load(open('pt.pkl', 'rb'))
# similarity_scores = pickle.load(open('similarities.pkl', 'rb'))
filtered_books = pickle.load(open('filtered_books.pkl', 'rb'))

# --- Genre Options ---
genre_options = ['All'] + sorted(filtered_books['Genre'].dropna().unique().tolist())

# --- Streamlit Page Config ---
st.set_page_config(page_title="📚 Book Recommender", layout="wide")
st.markdown("<h1 style='text-align: center; color: white;'>📖 Book Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>🔍 Enter a book you like, filter by genre, or browse popular picks!</p>", unsafe_allow_html=True)


# --- Genre Filter and Input ---
selected_genre = st.selectbox("🎭 Filter by Genre (Optional):", genre_options)
user_input = st.text_input("Type a Book Name")

# --- Show Book Cards ---
def show_books(book_titles):
    cols = st.columns(5)
    for i, title in enumerate(book_titles):
        book_info = filtered_books[filtered_books['Book-Title'] == title].drop_duplicates('Book-Title')

        if not book_info.empty:
            # Try to get a valid thumbnail
            valid_thumbnails = book_info[book_info['Image-URL-M'].notnull() & (book_info['Image-URL-M'] != '')]
            thumbnail = valid_thumbnails['Image-URL-M'].values[0].strip() if not valid_thumbnails.empty else None

            author = book_info['Book-Author'].values[0]

            with cols[i % 5]:
                if thumbnail:
                    st.image(thumbnail, width=120)
                else:
                    st.write("📕")  # fallback icon
                st.markdown(f"**{title}**")
                st.caption(f"by {author}")
        else:
            with cols[i % 5]:
                st.markdown(f"**{title}**")


# --- Show Popular Books by Genre ---
def show_popular_books(genre):
    st.subheader("📈 Popular Books")
    if genre != 'All':
        top_books = filtered_books[filtered_books['Genre'] == genre]
    else:
        top_books = filtered_books
    top_books = top_books.drop_duplicates('Book-Title').sort_values('Book-Rating', ascending=False).head(10)
    show_books(top_books['Book-Title'].tolist())


def recommend(book_name):
    lowercase_titles = [title.lower() for title in pt.index]
    matched_titles = get_close_matches(book_name.lower(), lowercase_titles, n=5, cutoff=0.6)

    blacklist_keywords = ['box set', 'summary', 'movie', 'cover', 'collection', 'guide', 'paperback']

    for matched in matched_titles:
        matched_title = pt.index[lowercase_titles.index(matched)]

        if any(bad_word in matched_title.lower() for bad_word in blacklist_keywords):
            continue

        if matched_title not in pt.index:
            continue

        try:
            book_index = pt.index.get_loc(matched_title)
            distances = similarity_scores[book_index]
        except:
            continue

        book_info = filtered_books[filtered_books['Book-Title'] == matched_title]
        book_genre = book_info['Genre'].values[0] if not book_info.empty else "Unknown"

        if selected_genre != 'All':
            if book_genre == "Unknown":
                st.warning("⚠️ *Note:* The genre of this book is unknown. Showing its recommendations anyway.")
            elif book_genre != selected_genre:
                st.warning(f"⚠️ *Note:* The book you entered belongs to the **{book_genre}** genre, not **{selected_genre}**. Showing its recommendations anyway.")

        st.subheader(f"📚 Recommendations for: *{book_name}*")
        book_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:]

        # --- Genre Filtering ---
        recommended_titles = []
        for idx, _ in book_list:
            title = pt.index[idx]
            info = filtered_books[filtered_books['Book-Title'] == title]
            if book_genre == "Unknown":
                recommended_titles.append(title)  # allow all
            elif not info.empty and info['Genre'].values[0] == book_genre:
                recommended_titles.append(title)
            if len(recommended_titles) >= 10:
                break

        show_books(recommended_titles)
        return True

    return False


if st.button("Recommend"):
    if user_input.strip():
        manual_map = {
            'harry potter': "Harry Potter and the Sorcerer's Stone",
            'lord of the rings': "Lord of the Rings, Part 1",
            'atomic habits': "Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones",
            'dune': "Dune (Dune Chronicles, Book 1)",
            'game of thrones': "A Game of Thrones (A Song of Ice and Fire, Book 1)"
        }

        input_clean = user_input.strip().lower()
        mapped_input = manual_map.get(input_clean, user_input.strip())

        success = recommend(mapped_input)

        if not success:
            st.warning("⚠️ Sorry, we can't process your request right now. You may like these books instead:")
            show_popular_books(selected_genre)
    else:
        st.info("✏️ Please enter a book name to get recommendations.")


# --- Footer ---
st.markdown("---")
st.markdown("<p style='text-align:center'>Made by Pratyaksh Agrawal</p>", unsafe_allow_html=True)

# --- Styling ---
st.markdown("""
    <style>
        body {
            background-color: #F5F5F5;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 10px 24px;
            border-radius: 8px;
        }
        .stTextInput>div>input {
            background-color: #ffffff;
            color: black;
        }
        .css-1v0mbdj.ef3psqc4 {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)
