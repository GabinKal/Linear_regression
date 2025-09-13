# 🛒 E-Commerce Linear Regression Project

## 📌 Description
Cette application utilise la **régression linéaire** pour prédire le montant d'achat annuel d’un client à partir de ses comportements d’utilisation (site web, application mobile, durée de session, ancienneté).  
L’interface est développée avec **Streamlit**, permettant une interaction simple et intuitive.

---

## 📂 Structure du projet

```Linear_regression/
│── data/
│ └── ecommerce.csv # Jeu de données utilisé pour l'entraînement
│
│── model/
│ ├── model.pkl # Modèle de régression sauvegardé
│ └── scaler.pkl # Scaler sauvegardé (normalisation des features)
│
│── app/
│ └── main.py # Application Streamlit
│
│── Linear.ipynb # Notebook Jupyter d'entraînement et analyse
│── requirements.txt # Dépendances Python
│── README.md # Documentation du projet
````

---

## ⚙️ Fonctionnalités principales
- 📊 Exploration et visualisation du dataset e-commerce  
- 🤖 Entraînement d’un modèle de **régression linéaire** avec scikit-learn  
- 📈 Évaluation des performances du modèle (R², MSE)  
- 🖥️ Interface web interactive avec **Streamlit** pour prédire le montant d’achat annuel  
- ✅ Gestion des valeurs incohérentes (prédictions négatives corrigées en 0 €)  

---

## 🛠️ Technologies utilisées
- **Python 3.11**  
- **Jupyter Notebook**  
- **Pandas, Numpy** (manipulation des données)  
- **Matplotlib, Seaborn** (visualisation)  
- **Scikit-learn** (modélisation et évaluation)  
- **Streamlit** (interface web)  

---

## 🚀 Installation et utilisation

1. **Cloner le dépôt**
```bash
git clone https://github.com/ton-username/Ecommerce-Spending-Prediction.git
cd Ecommerce-Spending-Prediction
