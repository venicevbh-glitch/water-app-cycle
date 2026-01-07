import streamlit as st
import time

# Page Configuration
st.set_page_config(page_title="AquaJourney", page_icon="💧")

st.title("💧 AquaJourney: Water Cycle Explorer")
st.markdown("---")

# Sidebar for Navigation
st.sidebar.header("Explore Stages")
stage = st.sidebar.selectbox("Choose a Stage", ["Home", "Evaporation", "Condensation", "Precipitation", "Collection"])

if stage == "Home":
    st.subheader("Welcome to the Water Cycle Project!")
    st.write("Is app ke zariye aap samajh sakte hain ki paani dharti se aasman aur wapas dharti tak kaise pahunchta hai.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Water_cycle.png/800px-Water_cycle.png", caption="The Water Cycle")

elif stage == "Evaporation":
    st.header("☀️ Stage 1: Evaporation")
    st.write("Jab suraj ki garmi se nadiyon aur samundar ka paani bhaap (vapor) bankar upar udta hai.")
    temp = st.slider("Temperature badhayein (°C)", 0, 100, 25)
    if temp > 50:
        st.success(f"High Temp ({temp}°C): Evaporation tez ho rahi hai! ☁️☁️")
    else:
        st.info("Normal Temp: Evaporation dheere ho rahi hai.")

elif stage == "Condensation":
    st.header("☁️ Stage 2: Condensation")
    st.write("Jab water vapor upar jakar thanda ho jata hai aur baadal (clouds) banata hai.")
    if st.button("Baadal Banayein"):
        with st.spinner('Thandak badh rahi hai...'):
            time.sleep(2)
        st.write("✅ Baadal taiyar hain! ☁️🌩️")

elif stage == "Precipitation":
    st.header("🌧️ Stage 3: Precipitation")
    st.write("Jab baadal bhari ho jate hain, toh barish, baraf ya olon ke roop mein paani neeche girta hai.")
    rain_type = st.radio("Mausam chunein:", ["Rain 🌧️", "Snow ❄️", "Hail 🧊"])
    st.write(f"Abhi dharti par **{rain_type}** ho rahi hai!")

elif stage == "Collection":
    st.header("🌊 Stage 4: Collection")
    st.write("Barish ka paani wapas samundar, jheelon aur zameen ke neeche jama ho jata hai.")
    st.progress(100)
    st.balloons()
