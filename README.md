# ML-IDS-Project README

# 🚨 ML-Based Intrusion Detection System (IDS)

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.2.2-orange)
![Flask](https://img.shields.io/badge/Flask-2.3-green)
![License](https://img.shields.io/badge/License-MIT-red)

---

## 🔹 Overview

This project implements a **Machine Learning-based Intrusion Detection System (IDS)** using the **UNSW-NB15 dataset**.

It includes:

* Data preprocessing & cleaning
* Handling imbalanced classes with **SMOTE**
* Training a **Random Forest classifier**
* Visualizing **feature importance**, **confusion matrix**, **ROC curves**
* Deployment via a **Flask web app** for real-time network traffic predictions

---

## 🔹 Folder Structure

```
ML-IDS-Project/
│
├─ notebooks/                  
│   ├─ 01_Data_Loading_Preprocessing.ipynb
│   └─ 02_Model_Training_Evaluation.ipynb
├─ models/                     
│   └─ rf_ids_model.pkl
├─ src/                        
│   └─ utils.py                 
├─ templates/                  
│   └─ index.html
├─ app.py                      
├─ requirements.txt            
└─ README.md
```

---

## 🔹 Quick Start

### 1️⃣ Clone the repository

```bash
git clone https://github.com/soukainahn/ML-IDS.git
cd ML-IDS
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask Web App

```bash
python app.py
```

* Open your browser at `http://127.0.0.1:5000/`
* Enter network traffic features to get predictions:

  * `Normal Traffic ✅`
  * `Attack Detected 🚨`

---

## 🔹 Dataset

* **UNSW-NB15 dataset** is **not included** due to size.
* Download from [Kaggle](https://www.kaggle.com/datasets/mrwellsdavid/unsw-nb15)
* Optionally include a **small sample CSV** in `data/` for testing.

---

## 🔹 Features Used

Some example features:

| Feature             | Description                            |
| ------------------- | -------------------------------------- |
| `dur`               | Session duration (seconds)             |
| `proto`             | Protocol type (TCP, UDP, etc.)         |
| `service`           | Network service (HTTP, FTP, DNS, etc.) |
| `state`             | Connection state (FIN, CON, etc.)      |
| `spkts` / `dpkts`   | Source / Destination packets           |
| `sbytes` / `dbytes` | Source / Destination bytes             |

> Full feature list is in the notebooks.

---

## 🔹 Model

* **Random Forest Classifier**
* Balanced training set using **SMOTE**
* Metrics include:

  * Accuracy
  * F1-Score
  * Confusion Matrix
  * ROC-AUC

---

## 🔹 Visualizations

All graphs are included in the notebooks. Examples:

**Confusion Matrix**
![Confusion Matrix](images/confusion_matrix.png)

**ROC Curve**
![ROC Curve](images/roc_curve.png)

**Feature Importance**
![Feature Importance](images/feature_importance.png)

> 💡 Save plots from notebooks using `plt.savefig('images/<name>.png')` and link them here.

---

## 🔹 License

MIT License – see [LICENSE](LICENSE) for details.

---

## 🔹 Author

**Soukaina Hanane**

* GitHub: [https://github.com/soukainahn](https://github.com/soukainahn)
* LinkedIn / Portfolio: *(optional)*

---

## 🔹 Notes / Tips

* Keep `models/` folder with the trained `.pkl` file (use **Git LFS** for large files).
* Include screenshots or diagrams to make it visually appealing.
* Update badges (Python, Flask, scikit-learn) if versions change.
