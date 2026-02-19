# 💸 FINPULSE: Autonomous Banking Intelligence

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-LightGBM%20%7C%20Scikit--Learn-brightgreen)
![Status](https://img.shields.io/badge/Status-Prototype%20Ready-success)

FINPULSE is an AI-powered Autonomous Banking Intelligence System that converts raw transaction data into actionable cross-sell recommendations using privacy-first local machine learning inference.

The platform ingests transaction CSV batches, runs a trained ML pipeline, and generates hyper-personalized Top-3 financial product recommendations (Credit Cards, Loans, Insurance) for every customer.

Designed & Engineered by Anuvesh Tiwari.

--------------------------------------------------

## ✨ Key Features

- Local ML inference (LightGBM + Scikit-Learn)
- Probabilistic customer behaviour aggregation
- Enterprise Streamlit dashboard UI
- Batch CSV processing
- Privacy-first architecture (no external APIs)

--------------------------------------------------

## 🛠️ Tech Stack

* **Frontend:** Streamlit, Custom CSS3, HTML5 (Glassmorphism & Neon UI)
* **Data Processing:** Pandas 2.3.3, NumPy 2.3.5
* **Machine Learning Engine:** Scikit-Learn 1.7.2, LightGBM 4.6.0
* **Model Serialization:** Joblib 1.5.2
* **Deployment:** Streamlit Community Cloud

--------------------------------------------------

## 🏗️ System Architecture

FINPULSE operates through a structured end-to-end machine learning inference workflow:

**1. Data Ingestion**  
Transaction batch uploaded via CSV for processing.

**2. Schema Validation**  
Validates required columns, formats, and data consistency before inference.

**3. ML Inference Pipeline**
- Imputation   
- Scaling 
- Encoding 
- Prediction

**4. Probability Intelligence**  
Aggregates transaction-level predictions into customer-level behavioral insights using averaged probability vectors.

**5. Product Mapping**
- Travel Spending → Travel Credit Card  
- High EMI Pattern → Personal Loan  
- Healthcare Spending → Insurance Plan

**6. Export**  
Produces a downloadable customer targeting matrix for cross-sell campaigns.


--------------------------------------------------

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

--------------------------------------------------

## 👨‍💻 Project Team

| Role | Name | Contribution |
| :--- | :--- | :--- |
| **Lead Machine Learning Engineer** | **Anuvesh Tiwari** | **Led and implemented the complete machine learning pipeline, including feature engineering, model training, probabilistic recommendation logic, and production inference integration.** |
| **Lead Developer** | **Sahil Tiwari** | **Designed and developed the interactive fintech dashboard UI, implementing modern UX principles and custom Streamlit interface architecture.** |
| Data Analyst | Kshitij Singh | Data for CSV |
| Strategy | Omkar Dubey | Product Strategy |

--------------------------------------------------

## Vision

- Real-time behavioural prediction
- Intelligent cross-selling
- Customer lifetime value optimization
- AI-driven banking personalization

--------------------------------------------------

### 📬 Contact
Anuvesh Tiwari
Machine Learning Engineer

Built with Python & Machine Learning.
