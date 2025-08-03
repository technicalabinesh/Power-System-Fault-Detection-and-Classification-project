# ⚡ Power System Fault Detection and Classification

This project focuses on building a machine learning model to detect and classify different types of faults in a **power distribution system**, using simulated electrical measurement data.

---

## 📌 Objective

To design a predictive model that:
- **Identifies faults** in power systems
- **Classifies** fault types (Line-to-Ground, Line-to-Line, etc.)
- Helps in **quick fault response and improved grid reliability**

---

## 🧠 Machine Learning Pipeline

### 🔹 1. Data Loading & Preprocessing
- CSV data containing electrical measurements (voltage, current, phase data)
- Cleaned missing/null values
- Encoded categorical labels

### 🔹 2. Feature Engineering
- Selected relevant electrical features
- Encoded target labels (fault types)

### 🔹 3. Feature Scaling
- StandardScaler applied to ensure uniform scaling

### 🔹 4. Model Training
- Model: **Random Forest Classifier**
- Splitting: Train/Test (80/20)

### 🔹 5. Evaluation Metrics
- **Accuracy Score**
- **Confusion Matrix**
- **Classification Report (Precision, Recall, F1-Score)**

---

## 🛠 Technologies Used

- **Python 3**
- **Pandas, NumPy** for data processing
- **Scikit-learn** for ML modeling
- **Matplotlib, Seaborn** for visualization

---

## 🧪 Results

The Random Forest model achieved:
- ✅ High accuracy on unseen test data
- 📊 Clear classification between fault types
- 🔧 Robust performance even with imbalanced data

---

## 📁 File Structure


power_fault_classification/
│
├── power_fault_classification_code.py # Full project code
├── fault_data.csv # Sample dataset (replace with actual)
├── README.md # Project documentation
└── output/
├── confusion_matrix.png
└── classification_report.txt


---

## 📥 How to Run

1. Clone the repo or download the `.py` file  
2. Install dependencies:
pip install pandas numpy scikit-learn matplotlib seaborn


Edit
3. Run the code:
python power_fault_classification_code.py

---

## 📈 Future Improvements

- Switch to **deep learning (LSTM/CNN)** for time-series data  
- Integrate **real-time sensor streaming**  
- Add **visual dashboards** for grid operators

---

## 👨‍💻 Author

**Abinesh M**  
*Aspiring Data Analyst | Machine Learning Enthusiast | Power Systems Learner*

---

## 🔗 License

This project is open-source and free to use under the [MIT License](https://opensource.org/licenses/MIT).


