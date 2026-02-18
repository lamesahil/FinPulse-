import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="FINPULSE | QuadCore", layout="wide", page_icon="💸")

# --- 2. 💎 PREMIUM FINTECH UI CSS ---
st.markdown("""
    <style>
    /* 🌌 Enterprise Fintech Gradient Background */
    .stApp { 
        background: linear-gradient(135deg, #050b14 0%, #0a1929 50%, #021114 100%) !important;
        background-attachment: fixed !important;
        color: #e2e8f0; 
    }
    
    /* 🟢 Subtle Aurora Glow Effect behind everything */
    .stApp::before {
        content: '';
        position: fixed;
        top: -20%;
        left: 15%;
        width: 70vw;
        height: 70vh;
        background: radial-gradient(circle, rgba(0, 255, 136, 0.05) 0%, transparent 60%);
        z-index: -1;
        pointer-events: none;
    }

    /* Centered Header Text */
    .header-box { text-align: center; padding: 25px 0 15px 0; position: relative; z-index: 10; }
    .header-title { font-size: 3.2rem; font-weight: 800; color: #ffffff; letter-spacing: -1px; }
    .header-sub { color: #94a3b8; font-size: 1.1rem; letter-spacing: 1.5px; text-transform: uppercase; font-weight: 500; }

    /* 🚀 PREMIUM GLASSMORPHISM NAVIGATION BAR */
    [data-baseweb="tab-list"] {
        background: rgba(15, 23, 42, 0.6) !important; /* Semi-transparent Slate */
        backdrop-filter: blur(16px) !important;
        -webkit-backdrop-filter: blur(16px) !important;
        border-radius: 50px;
        padding: 6px 10px;
        display: flex;
        justify-content: center;
        gap: 5px;
        margin: 0 auto 35px auto;
        width: fit-content;
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    }
    
    /* Inactive Tabs */
    button[data-baseweb="tab"] {
        color: #94a3b8 !important;
        background-color: transparent !important;
        border-radius: 50px !important;
        padding: 10px 28px !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        border: none !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }

    /* Active Tab (Neon Accent) */
    button[data-baseweb="tab"][aria-selected="true"] {
        background-color: rgba(0, 255, 136, 0.15) !important;
        color: #00ff88 !important;
        box-shadow: inset 0 0 12px rgba(0, 255, 136, 0.1) !important;
        border: 1px solid rgba(0, 255, 136, 0.3) !important;
    }
    
    div[data-baseweb="tab-highlight"] { display: none !important; }

    /* Modern Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #00ff88 0%, #00cc6e 100%);
        color: #020617; border: none; border-radius: 12px; 
        padding: 14px 24px; font-weight: 800; width: 100%; transition: 0.3s;
        box-shadow: 0 4px 15px rgba(0, 255, 136, 0.2);
    }
    .stButton>button:hover { 
        transform: translateY(-2px); 
        box-shadow: 0 8px 25px rgba(0, 255, 136, 0.4); 
    }
    
    /* Glassmorphism Metric Cards & UI Elements */
    .metric-card { 
        background: rgba(15, 23, 42, 0.5); 
        backdrop-filter: blur(12px);
        padding: 24px; 
        border-radius: 16px; 
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-left: 4px solid #00ff88; 
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
    }
    
    [data-testid="stFileUploadDropzone"] {
        background: rgba(15, 23, 42, 0.4) !important;
        border: 2px dashed rgba(0, 255, 136, 0.4) !important;
        border-radius: 16px !important;
        backdrop-filter: blur(10px);
    }
    
    /* Fixed Glass Footer */
    .custom-footer {
        position: fixed; bottom: 0; left: 0; width: 100%;
        background: rgba(2, 6, 23, 0.85); backdrop-filter: blur(12px);
        padding: 12px 0; text-align: center; font-size: 13px; color: #64748b; 
        border-top: 1px solid rgba(255,255,255,0.05); z-index: 1000;
    }
    .custom-footer span { color: #00ff88; font-weight: bold; }
    .block-container { padding-bottom: 90px !important; }
    </style>
""", unsafe_allow_html=True)

# --- 3. CUSTOM HEADER ---
st.markdown("""
    <div class="header-box">
        <div class="header-title">💸 FINPULSE</div>
        <div class="header-sub">Autonomous Banking Intelligence</div>
    </div>
""", unsafe_allow_html=True)

# --- 4. NAVIGATION TABS ---
tab1, tab2, tab3 = st.tabs(["🎯 Live Operations", "🏗️ Architecture", "🎥 Live Demo"])

category_to_product = {
    "Travel": "Travel Credit Card", "Shopping": "Cashback Credit Card",
    "Food": "Dining Rewards Card", "Groceries": "Supermarket Cashback Card",
    "Housing": "Home Loan", "Medical": "Health Insurance",
    "Fitness": "Wellness Insurance", "Subscriptions": "Premium Savings Account",
    "Transportation": "Auto Loan", "Hobbies": "Lifestyle Credit Card",
    "Gifts": "Rewards Credit Card", "Friend": "Peer Transfer Wallet",
    "Personal Hygiene": "Essential Spending Card"
}

# ==========================================
# 🟢 TAB 1: LIVE OPERATIONS (ML Logic)
# ==========================================
with tab1:
    try:
        pipeline = joblib.load("model/model.pkl")
        le = joblib.load("model/label_encoder.pkl")
    except Exception as e:
        st.error("System Core Offline. Missing ML files in /model directory.")
        st.stop()

    uploaded_file = st.file_uploader("📂 Drop Banking Batch CSV Here", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        required_columns = ["Customer ID", "Category", "Total Spent", "Quantity", "Transaction Date"]
        if not all(col in df.columns for col in required_columns):
            st.error(f"⚠️ Invalid Data Schema. Required: {', '.join(required_columns)}")
        else:
            c1, c2 = st.columns(2)
            c1.markdown(f'<div class="metric-card"><span style="color:#94a3b8; font-size:14px; font-weight:600; text-transform:uppercase;">Batch Size</span><br><h2 style="color:#ffffff; margin:5px 0 0 0;">{len(df)} <span style="font-size:16px; color:#00ff88;">Records</span></h2></div>', unsafe_allow_html=True)
            c2.markdown(f'<div class="metric-card"><span style="color:#94a3b8; font-size:14px; font-weight:600; text-transform:uppercase;">Target Entities</span><br><h2 style="color:#ffffff; margin:5px 0 0 0;">{df["Customer ID"].nunique()} <span style="font-size:16px; color:#00ff88;">Unique IDs</span></h2></div>', unsafe_allow_html=True)
            st.write("")

            if st.button("🚀 INITIATE ML PIPELINE"):
                with st.spinner("Analyzing neural vectors..."):
                    try:
                        X = df.drop(columns=["Category"], errors='ignore')
                        probs = pipeline.predict_proba(X)
                        prob_df = pd.DataFrame(probs, columns=le.classes_)
                        
                        prob_df.columns = [category_to_product.get(col, col) for col in prob_df.columns]
                        prob_df["Customer ID"] = df["Customer ID"].values
                        customer_scores = prob_df.groupby("Customer ID").mean()

                        final_recs = []
                        for cust_id, row in customer_scores.iterrows():
                            top3 = row.sort_values(ascending=False).head(3).index.tolist()
                            final_recs.append([cust_id, " | ".join(top3)])

                        output_df = pd.DataFrame(final_recs, columns=["Customer ID", "Recommended Strategy"])
                        
                        st.success("✅ Neural Mapping Complete.")
                        st.dataframe(output_df, use_container_width=True)

                        csv = output_df.to_csv(index=False).encode("utf-8")
                        st.download_button("📥 DOWNLOAD STRATEGY MATRIX", csv, "finpulse_strategy.csv", "text/csv")
                    except Exception as e:
                        st.error(f"Inference Error: {e}")

# ==========================================
# 🏗️ TAB 2: SYSTEM ARCHITECTURE
# ==========================================
with tab2:
    st.subheader("🏗️ Pipeline Architecture")
    if os.path.exists("images/p1.jpg"):
        st.image("images/p1.jpg", use_container_width=True)
    else:
        st.warning("Diagram 'p1.jpg' not found.")

# ==========================================
# 🎥 TAB 3: LIVE DEMO (YOUTUBE LINK)
# ==========================================
with tab3:
    st.subheader("🎥 FINPULSE: Official Product Demo")
    st.write("Watch the complete system workflow and AI inference in action.")
    
    # 🚨 APNA YOUTUBE LINK YAHAN DAALNA 🚨
    youtube_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 
    
    st.video(youtube_url)

# --- FOOTER ---
st.markdown("""
    <div class="custom-footer">
        Engineered for Scale by <span>QUADCORE</span> | FinPulse Protocol v2.0
    </div>
""", unsafe_allow_html=True)