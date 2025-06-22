import streamlit as st

st.set_page_config(page_title="Safebloq MVP", layout="wide")

st.title("Safebloq Zero Trust Security Dashboard (MVP)")
st.markdown("Protecting SMBs with click-and-play Zero Trust security")

# Identity and Access Management Section
st.subheader("🔐 Identity & Access Management (Keycloak RBAC)")
st.success("2 users logged in. Role-based access control is active.")

# Endpoint Detection & Response Section
st.subheader("🛡️ Endpoint Monitoring (Wazuh)")
st.warning("3 endpoints flagged for suspicious login patterns.")
st.info("Auto-remediation enabled on affected devices.")

# Zero Trust Networking Section
st.subheader("🌐 Zero Trust Network (OpenZiti)")
st.success("VPN-less secure access active for 5 users.")

# Alerts and Visual Insight Section
st.subheader("📈 Alerts & Insights")
st.line_chart({
    "Anomalies Detected": [0, 1, 2, 3, 2, 4, 5]
})

st.caption("MVP Demo – Built with Streamlit. Full platform launching soon.")
