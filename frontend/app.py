import streamlit as st
from backend.predict import predict_risk

st.set_page_config(
    page_title="Jung Proof AI",
    page_icon="🌧️",
    layout="centered"
)

# Language selector
lang = st.selectbox("🌐 Language / भाषा", ["English", "नेपाली"])
def t(en, np): 
    return en if lang == "English" else np

# Title
st.title(t(
    "🌍 Jung Proof AI – Disaster Early Warning System",
    "🌍 जंग प्रूफ AI – विपद् पूर्व चेतावनी प्रणाली"
))

st.write(t(
    "AI-powered flood and landslide risk prediction using satellite-style data and community inputs.",
    "AI, उपग्रह-जस्तै डेटा र समुदायको सूचनाबाट जोखिम अनुमान।"
))

# Inputs
rainfall = st.slider(t("Rainfall (mm/day)", "वर्षा (मिमी/दिन)"), 0, 300, 120)

river_level = st.selectbox(
    t("River Level", "नदीको सतह"),
    [0,1,2,3],
    format_func=lambda x: ["Low","Medium","High","Very High"][x]
)

soil = st.slider(t("Soil Moisture", "माटोको चिस्यान"), 0.0, 1.0, 0.7)
slope = st.slider(t("Slope (degrees)", "ढलान (डिग्री)"), 0, 60, 35)

st.subheader(t("Community Warning Signs", "समुदायका चेतावनी संकेत"))
crack = st.checkbox(t("Ground cracks", "माटोमा चिरा"))
muddy = st.checkbox(t("Muddy water from springs", "धमिलो पानी"))
river_change = st.checkbox(t("River behavior change", "नदीको असामान्य व्यवहार"))
past = st.checkbox(t("Past disaster history", "पहिले विपद्"))

input_data = [[
    rainfall,
    river_level,
    soil,
    slope,
    int(crack),
    int(muddy),
    int(river_change),
    int(past)
]]

if st.button(t("🚨 Predict Risk", "🚨 जोखिम अनुमान")):
    result = predict_risk(input_data)

    st.metric(
        t("Flood Risk", "बाढी जोखिम"),
        result["flood"][0],
        f"{result['flood'][1]:.1f}%"
    )

    st.metric(
        t("Landslide Risk", "पहिरो जोखिम"),
        result["landslide"][0],
        f"{result['landslide'][1]:.1f}%"
    )

    if result["flood"][0] == "High" or result["landslide"][0] == "High":
        st.error(t(
            "⚠️ High risk detected. Move to a safer location immediately.",
            "⚠️ उच्च जोखिम। तुरुन्त सुरक्षित स्थानमा जानुहोस्।"
        ))
