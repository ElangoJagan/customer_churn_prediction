# Customer Churn Prediction

A machine learning web application that predicts whether a customer is likely to churn, built with a modular, production-style pipeline.

## 🎯 Problem Statement

Customer churn prediction helps businesses identify customers at risk of leaving, enabling proactive retention strategies. This project demonstrates handling **imbalanced classification** using **SMOTE** and **ensemble methods**.

## 🏗️ Project Architecture
3 Data Sources → Merge → Train/Test Split → Preprocessing → SMOTE → Model Training → Flask Web App
## 📊 Key Features

- **Multiple Data Sources**: Merges customer demographics, usage, and support data
- **Imbalanced Data Handling**: SMOTE (Synthetic Minority Oversampling Technique)
- **Ensemble Models**: Logistic Regression, Random Forest, XGBoost — best model auto-selected
- **Modular OOP Design**: Class-based components with industry-standard patterns
- **Custom Logging & Exception Handling**: Full traceability across the pipeline
- **Flask Web Interface**: User-friendly prediction form

## 🧠 OOP Concepts Used

| Concept | File |
|---|---|
| `__str__` / `__repr__` | `exception.py` |
| Singleton Pattern | `logger.py` |
| `@dataclass` | `config_entity.py` |
| `@staticmethod` | `data_ingestion.py` |
| `@property` | `data_transformation.py` |
| `@classmethod` | `model_trainer.py` |
| Composition | `train_pipeline.py` |
| Abstract Base Class (ABC) | `predict_pipeline.py` |

## 🛠️ Tech Stack

- **Language**: Python
- **ML Libraries**: scikit-learn, XGBoost, imbalanced-learn
- **Web Framework**: Flask
- **Data Handling**: Pandas, NumPy

## 📁 Project Structure
Customer_Churn_Prediction/

├── data/                  # Raw and processed data

├── artifacts/             # Saved model and preprocessor

├── src/

│   ├── components/        # Data ingestion, transformation, model training

│   ├── pipeline/           # Train and predict pipelines

│   ├── entity/             # Config dataclasses

│   ├── logger.py

│   ├── exception.py

│   └── utils.py

├── templates/              # HTML pages

├── static/                 # CSS styling

├── app.py                  # Flask application

└── main.py                 # Training entry point

## 🚀 How to Run

```bash
# Activate virtual environment
.\ml_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Train the model
python main.py

# Run the web app
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

## 📈 Model Evaluation

Models are evaluated using **Precision, Recall, F1-Score, and ROC-AUC** rather than accuracy alone, since accuracy is misleading on imbalanced datasets.

## 👨‍💻 Author

Elango K J 