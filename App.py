import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Config
st.set_page_config(page_title="Safebloq MVP", layout="wide")

# Header
st.title("🛡️ Safebloq Zero Trust Security Dashboard")
st.markdown("Welcome to your centralized cybersecurity hub for small and medium businesses.")

# Section 1: Live Threats Table
st.subheader("🔍 Detected Threats (Live)")
security_events = pd.DataFrame([
    {"Time": "10:21", "Device": "Laptop - HR", "Threat": "Phishing Link Detected", "Severity": "High"},
    {"Time": "11:05", "Device": "Mobile - Sales", "Threat": "Unsecured Wi-Fi Access", "Severity": "Medium"},
    {"Time": "11:40", "Device": "Tablet - Finance", "Threat": "Unauthorized Login", "Severity": "Critical"},
    {"Time": "12:10", "Device": "Desktop - Admin", "Threat": "Malware Signature Match", "Severity": "High"}
])
st.dataframe(security_events)

# Section 2: Threat Severity Breakdown Chart
st.subheader("📊 Threat Severity Distribution")
labels = ['Low', 'Medium', 'High', 'Critical']
sizes = [10, 30, 45, 15]
colors = ['#7dd3fc', '#facc15', '#fb923c', '#ef4444']
explode = (0, 0, 0.1, 0.1)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', colors=colors, shadow=True, startangle=140)
ax1.axis('equal')
st.pyplot(fig1)

# Section 3: Connected Devices Overview
st.subheader("🖥️ Connected Devices")
devices = {
    "Laptops": 14,
    "Mobiles": 9,
    "Desktops": 6,
    "Tablets": 4
}
st.bar_chart(devices)

# Section 4: User Access Status Cards
st.subheader("✅ User Access Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Active Users", "52")
col2.metric("Blocked Users", "3")
col3.metric("New Devices Today", "7")

# Section 5: Compliance & Coverage
st.subheader("📋 Compliance Checks")
st.success("✅ Endpoint encryption policies are enforced.")
st.warning("⚠️ 4 devices pending MFA enrollment.")
st.info("ℹ️ 76% of users have completed security training.")

# Footer
st.markdown("---")
st.caption("Safebloq MVP | Built for SMBs | Zero Trust Security Simplified")
