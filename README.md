# 💸 FINPULSE: Autonomous Banking Intelligence

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-LightGBM%20%7C%20Scikit--Learn-brightgreen)
![Status](https://img.shields.io/badge/Status-Prototype%20Ready-success)

**FINPULSE** is a Next-Gen Machine Learning dashboard built for modern Neo-Banks and financial institutions. It ingests massive batches of encrypted customer transaction data, runs complex probability models, and generates hyper-personalized top-3 product recommendations (Credit Cards, Loans, Insurance) for every unique customer.

Engineered with ❤️ by **Team QUADCORE**.

---

## ✨ Key Features

* 🧠 **Zero-API Local Inference Engine:** Uses pre-trained gradient boosting models (LightGBM/Scikit-Learn) for high-speed, local data processing without relying on expensive external APIs.
* 📊 **Probabilistic Aggregation:** Groups multiple transactions per customer and mathematically averages probability vectors to find their *long-term dominant financial need*.
* 🎨 **Enterprise Fintech UI:** Built with custom CSS featuring a Deep Slate gradient, Neo-Green accents, and modern Glassmorphism architecture.
* 📥 **Batch CSV Processing:** Allows bank operators to upload daily transaction dumps and instantly download targeted cross-sell matrices.
* 🔒 **Compliant Architecture:** Processes all data locally within the server environment, ensuring no PII data leakage.

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit, Custom CSS3, HTML5 (Glassmorphism & Neon UI)
* **Data Processing:** Pandas 2.3.3, NumPy 2.3.5
* **Machine Learning Engine:** Scikit-Learn 1.7.2, LightGBM 4.6.0
* **Model Serialization:** Joblib 1.5.2
* **Deployment:** Streamlit Community Cloud

---

## 🏗️ System Architecture

1.  **Data Ingestion:** User uploads a raw transaction `.csv` batch.
2.  **Schema Validation:** System strictly verifies required banking features.
3.  **Inference Pipeline:** Data is passed through a pre-trained scikit-learn pipeline (Imputation, Scaling, Label Encoding) and a classification model.
4.  **Probability Mapping:** The raw category output is mapped to specific, marketable banking products (e.g., *Travel* -> *Travel Credit Card*).
5.  **Export:** Generates a downloadable strategic targeting matrix.

---

## 🚀 Local Installation & Setup

To run FINPULSE on your local machine, ensure you have Python installed, then follow these exact steps to avoid environment mismatch errors.

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/finpulse.git](https://github.com/your-username/finpulse.git)
cd finpulse
```
2. Install Exact Dependencies
Note: We strictly pin our environment versions to ensure serialization compatibility with the pre-trained .pkl models.

```bash
pip install -r requirements.txt
```
3. Required File Structure
Ensure the following directories and files exist before running the application:
```bash
Plaintext
📦 finpulse
 ┣ 📂 model
 ┃ ┣ 📜 model.pkl             # Pre-trained ML pipeline
 ┃ ┗ 📜 label_encoder.pkl     # Target variable encoder
 ┣ 📂 images
 ┃ ┗ 📜 p1.jpg                # Architecture Diagram
 ┣ 📜 app.py                  # Main Streamlit Application
 ┗ 📜 requirements.txt        # Environment Dependencies
```

4. Run the Application
```bash
streamlit run app.py
The application will launch on http://localhost:8501
 ```

## 👨‍💻 Project Team

| Role | Name | Contribution |
| :--- | :--- | :--- |
| **Project Lead & Architect** | **Sahil Tiwari** | **Lead Developer, UI/UX Design** |
| ML Engineer | Anuvesh Tiwari | ML Engineer |
| Data Analyst | Kshitij Singh | Data Analyst |
| Strategy | Omkar Dubey | Product Strategy |

---

### 📬 Contact
**Maintained by Sahil Tiwari** *Open for collaboration and feedback.*

<div align="center">
  <sub>Built with ❤️ using Python</sub>
</div>
