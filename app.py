import streamlit as st
import time

st.set_page_config(page_title="BIS Engine", layout="wide")

st.title("🏗️ BIS Standards Recommendation Engine")
st.markdown("AI-powered system to identify relevant BIS standards")

# sidebar
st.sidebar.header("ℹ️ About")
st.sidebar.write("Enter product description to get BIS standards instantly")

try:
    from src.rag import generate_results

    st.success("✅ Backend ready")

    query = st.text_area("🔍 Enter Product Description")

    def detect_category(text):
        text = text.lower()
        if "cement" in text:
            return "Cement"
        elif "steel" in text:
            return "Steel"
        elif "concrete" in text:
            return "Concrete"
        return "General"

    if st.button("🚀 Get Recommendations"):
        if not query.strip():
            st.warning("Please enter a product description")
        else:
            start = time.time()

            results = generate_results(query)

            latency = time.time() - start

            category = detect_category(query)

            st.success(f"Detected Category: **{category}**")

            st.divider()

            col1, col2 = st.columns([3, 1])

            with col1:
                st.subheader("📊 Recommended Standards")

                for i, r in enumerate(results, 1):
                    st.markdown(f"### 🧾 {i}. {r['standard']}")
                    st.write(r["reason"])
                    st.markdown("---")

            with col2:
                st.subheader("⚡ Performance")
                st.metric("Response Time", f"{round(latency,2)} sec")

                st.subheader("🎯 Confidence")
                st.progress(min(1.0, 0.6 + 0.1 * len(results)))

except Exception as e:
    st.error(f"Error loading backend: {e}")