import streamlit as st
import joblib
import pandas as pd

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="📚 Book Recommendation System",
    layout="wide"
)

# =========================
# LOAD MODELS & DATA
# =========================
@st.cache_resource
def load_assets():
    svd = joblib.load("models/svd_model.pkl")
    knn = joblib.load("models/knn_model.pkl")
    df = joblib.load("models/df_small.pkl")

    user_ids = sorted(df["User-ID"].unique())
    isbn_list = df["ISBN"].unique()

    return svd, knn, df, user_ids, isbn_list


svd, knn, df, user_ids, isbn_list = load_assets()

# =========================
# HELPER
# =========================
def get_book_row(isbn):
    row = df[df["ISBN"] == isbn]
    return row.iloc[0] if not row.empty else None

# =========================
# HEADER
# =========================
st.title("📚 Book Recommendation System")
st.caption("Hybrid Recommendation Engine (SVD + KNN)")

# =========================
# TABS
# =========================
tab1, tab2 = st.tabs(["👤 User Recommendation", "🔍 Book Search"])

# =====================================================
# 👤 USER BASED RECOMMENDATION
# =====================================================
with tab1:
    user_id = st.selectbox("Select User ID", user_ids)
    top_n = st.slider("Number of Recommendations", 5, 20, 10)

    if st.button("🎯 Recommend Books"):
        with st.spinner("Finding best books for you..."):
            user_read = df[df["User-ID"] == user_id]["ISBN"].tolist()
            user_read_set = set(user_read)

            scores = []

            for isbn in isbn_list:
                if isbn in user_read_set:
                    continue

                try:
                    svd_score = svd.predict(user_id, isbn).est
                except:
                    svd_score = 0

                try:
                    knn_score = knn.predict(user_id, isbn).est
                except:
                    knn_score = 0

                final_score = 0.6 * svd_score + 0.4 * knn_score
                scores.append((isbn, final_score))

            scores = sorted(scores, key=lambda x: x[1], reverse=True)[:top_n]

        st.subheader("📖 Recommended Books")

        for i in range(0, len(scores), 5):
            cols = st.columns(5)

            for col, (isbn, score) in zip(cols, scores[i:i+5]):
                row = get_book_row(isbn)
                if row is None:
                    continue

                with col:
                    st.image(
                        row["Image-URL-M"]
                        if pd.notna(row["Image-URL-M"])
                        else "https://via.placeholder.com/120x180",
                        width=120
                    )
                    st.markdown(f"""
                    **{row['Book-Title']}**  
                    ✍️ {row['Book-Author']}  
                    🗓️ {row['Year-Of-Publication']}  
                    ⭐ {score:.2f}
                    """)

# =====================================================
# 🔍 BOOK SEARCH & SIMILAR BOOKS
# =====================================================
with tab2:
    book_name = st.text_input("Enter Book Title")

    if st.button("🔎 Find Similar Books") and book_name:
        matches = df[
            df["Book-Title"].str.contains(book_name, case=False, na=False)
        ]

        if matches.empty:
            st.error("❌ Book not found")
        else:
            selected_book = matches.iloc[0]
            target_isbn = selected_book["ISBN"]

            st.success(f"Showing results for: **{selected_book['Book-Title']}**")

            similar = []

            for isbn in isbn_list:
                if isbn == target_isbn:
                    continue

                try:
                    score = knn.predict(
                        selected_book["User-ID"], isbn
                    ).est
                except:
                    score = 0

                similar.append((isbn, score))

            similar = sorted(similar, key=lambda x: x[1], reverse=True)[:10]

            st.subheader("📚 Similar Books")

            for i in range(0, len(similar), 5):
                cols = st.columns(5)

                for col, (isbn, score) in zip(cols, similar[i:i+5]):
                    row = get_book_row(isbn)
                    if row is None:
                        continue

                    with col:
                        st.image(
                            row["Image-URL-M"]
                            if pd.notna(row["Image-URL-M"])
                            else "https://via.placeholder.com/120x180",
                            width=120
                        )
                        st.markdown(f"""
                        **{row['Book-Title']}**  
                        ✍️ {row['Book-Author']}  
                        🗓️ {row['Year-Of-Publication']}  
                        ⭐ {score:.2f}
                        """)

# =========================

