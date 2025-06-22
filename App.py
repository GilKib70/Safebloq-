import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Safebloq Zero Trust MVP", layout="wide")

st.image("safebloq_logo.png", width=150)
st.title("Safebloq Zero Trust Dashboard (MVP)")
st.subheader("Protecting SMEs with a Click-and-Play Cybersecurity Platform")

st.markdown("### 📊 Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Total Devices", "45", "+3")
col2.metric("Active Alerts", "7", "⚠️")
col3.metric("Incidents Resolved", "38", "+5")

st.markdown("---")

st.markdown("### 🧠 Threat Summary")
data = {
    "Date": [datetime.date.today() - datetime.timedelta(days=i) for i in range(5)],
    "Malware Detected": [3, 1, 2, 4, 1],
    "Phishing Attempts": [1, 0, 2, 1, 3],
    "Policy Violations": [2, 3, 0, 1, 2]
}
df = pd.DataFrame(data)
st.line_chart(df.set_index("Date"))

st.markdown("---")
st.markdown("### 🛡️ Recommendations")
st.info("• Enable auto-remediation on all endpoints\n• Train staff on latest phishing simulations\n• Review access control rules in Keycloak\n• Monitor network anomalies via OpenZiti overlays")
