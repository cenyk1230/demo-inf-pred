import streamlit as st
import json
import requests


def predict(text):
    res = requests.post("http://103.242.175.212:5000/", {"text": text})
    st.write(res.text)
    pred = json.loads(res.text)["pred"]
    return pred


title = st.text_input("Paper title", "evasion attacks against machine learning at test time")
abstract = st.text_area("Paper abstract", "In security-sensitive applications, the success of machine learning depends on a thorough vetting of their resistance to adversarial data. In one pertinent, well-motivated attack scenario, an adversary may attempt to evade a deployed system at test time by carefully manipulating attack samples. In this work, we present a simple but effective gradient-based approach that can be exploited to systematically assess the security of several, widely-used classification algorithms against evasion attacks. Following a recently proposed framework for security evaluation, we simulate attack scenarios that exhibit different risk levels for the classifier by increasing the attacker's knowledge of the system and her ability to manipulate attack samples. This gives the classifier designer a better picture of the classifier performance under evasion attacks, and allows him to perform a more informed model selection (or parameter setting). We evaluate our approach on the relevant security task of malware detection in PDF files, and show that such systems can be easily evaded. We also sketch some countermeasures suggested by our analysis.", height=20)

if st.button('Predict'):
    st.write("Prediction:", predict(title + " " + abstract))
