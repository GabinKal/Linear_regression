import streamlit as st
import pickle
import pandas as pd


with open("model/model.pkl", "rb")as f:
    model=pickle.load(f)

st.title("🛒 E-Commerce Spending Prediction")

st.write("Cette application prédit le montant d'achat annuel en fonction des caractéristiques utilisateur.")

# Champs de saisie utilisateur
time_on_site = st.number_input("Temps passé sur le site (min)", min_value=0.0, max_value=100.0, value=10.0)
time_on_app = st.number_input("Temps passé sur l'application mobile (min)", min_value=0.0, max_value=100.0, value=10.0)
length_session = st.number_input("Longueur de session (min)", min_value=0.0, max_value=100.0, value=10.0)
membership = st.number_input("Nombre d'années d'abonnement", min_value=0.0, max_value=20.0, value=5.0)

# Créer un DataFrame pour la prédiction
X_new = pd.DataFrame({
    "Avg. Session Length": [length_session],
    "Time on App": [time_on_app],
    "Time on Website": [time_on_site],
    "Length of Membership": [membership]
})



# Bouton de prédiction
if st.button("Prédire le montant d'achat annuel 💰"):
    prediction = model.predict(X_new)[0]
    if prediction <0:
        prediction=0
    st.success(f"Montant d'achat prédit : **{prediction:.2f} €**")