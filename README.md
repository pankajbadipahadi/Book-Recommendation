# 📚✨ Book Recommendation System

### 🤖 Hybrid ML Recommendation Engine | Streamlit App

## 🌟 Project Overview

📖 This **Book Recommendation System** provides **personalized book suggestions** using a **Hybrid Collaborative Filtering approach**.
It combines **SVD (Matrix Factorization)** and **KNN (Similarity-based filtering)** and is deployed using an **interactive Streamlit UI**.

---

## 🎯 What This Project Does

🔹 Recommends books based on **User ID**
🔹 Allows **Book Search & Similar Book Discovery**
🔹 Displays **Book Cover, Author, Year & Score**
🔹 Optimized for **low memory systems (8GB RAM)**

---

## 🧠 Recommendation Strategy

🟢 **SVD (Collaborative Filtering)**
→ Learns hidden user preferences

🟢 **KNN (Item Similarity)**
→ Finds similar books

✨ **Hybrid Score Formula**

```
Final Score = 0.6 × SVD + 0.4 × KNN
```

---

## 🛠️ Tech Stack

🧩 **Backend**

* 🐍 Python
* 📊 Pandas, NumPy
* 🤖 scikit-surprise

🎨 **Frontend**

* Streamlit

💾 **Model Handling**

* Joblib

---

## 📂 Project Structure

```
📦 Book-Recommendation-System
 ┣ 📁 models
 ┃ ┣ 📄 svd_model.pkl
 ┃ ┣ 📄 knn_model.pkl
 ┃ ┗ 📄 df_small.pkl
 ┣ 📄 Recommendation_Project.py
 ┗ 📄 README.md
```

---

## ▶️ How to Run the App

```bash
git clone https://github.com/your-username/book-recommendation-system.git
cd book-recommendation-system
pip install -r requirements.txt
streamlit run Recommendation_Project.py
```

---

## 🖥️ Application Features

👤 **User Recommendation**

* Select User ID
* Get top book recommendations

🔍 **Book Search**

* Search by book title
* View similar books

🖼️ **UI Highlights**

* Book posters
* Grid layout (5 books per row)
* Clean & modern design

---

## 📈 Results & Impact

⭐ Improved personalization
⚡ Fast response time
📉 Reduced data sparsity impact
🎯 Better user experience

---

## 🚀 Future Enhancements

✨ Content-based filtering
✨ User login system
✨ Online rating input
✨ Cloud deployment

---

## 👨‍💻 Author

* Pankaj Badipahadi - 📊 Data Science | 🤖 Machine Learning
* Parth Neware
* Sanchit Satpaise
* Usha Gudla
* Vasanth

---

⭐ **If you like this project, give it a star and share your feedback!** ⭐
