
BigMart Sales Forecasting Using Machine Learning:

A Machine Learning-powered web application that forecasts product sales across various BigMart outlets based on historical data and product/store attributes.


🔗 Live Demo

👉 [Click here to use the app](https://bigmartsalesperdiction-4.onrender.com/)


🧩 Project Development Process

1️⃣ Problem Understanding & Data Collection

  - Objective: Predict product sales based on item and outlet characteristics.
  - Dataset: Historical data containing attributes like item weight, visibility, fat content, type, MRP, and outlet details (size, location, establishment year).

2️⃣ Environment Setup

  - Python environment setup with ML and data analysis libraries.
  - Structured project folders for data processing, model training, and the web interface.
  - Version control enabled with Git.

3️⃣ Data Preprocessing

  - Missing Values: Mean imputation for item weight and mode for outlet size.
  - Cleaning: Standardized categorical variables.
  - Feature Preparation: Prepared dataset for ML training.

4️⃣ Feature Engineering & Data Splitting

  - Feature-target separation.
  - Split into 80% training and 20% test sets.
  - Feature scaling and polynomial feature generation.

5️⃣ Model Development & Training

  - Regression models used:
    - Linear Regression
    - Polynomial Regression
    - Ridge Regression
    - Random Forest
    - Gradient Boosting
    - CatBoost
  - Trained and saved using `pickle`.

6️⃣ Model Evaluation & Selection

  - Evaluated via R² Score and MSE.
  - Best-performing models identified and preserved for deployment.

🖥️ Web Application

🔧 Backend (Flask)

  - Handles user input and prediction logic.
  - Dynamically loads models.

🎨 Frontend

  - Dropdown for model selection.
  - Real-time input validation and prediction output.
  - Interactive UI with dynamic effects and mobile responsiveness.

🧪 Testing

  - Unit Testing: Component-level checks.
  - Integration Testing: End-to-end flow from input to prediction.


📄 Documentation

  Includes:
  - Installation steps
  - Usage instructions
  - Model details
  - Architecture overview
  - Enhancement roadmap


🧬 Publication Details

  - Title: "BigMart Sales Forecasting using Machine Learning"
  - Published at: International Conference on Advanced Computing Technologies
  - Pages: 98-103 | ISBN: 978-81-977391-1-8  
  - Authors:
    - Hari Prasad Chandika (Assistant Professor)
    - Mohammed Roumesha Firdous (Student)
    - Pentela Pooja (Student)
    - Mogilicharla Veerendra Sai (Student)
    - Nalanagula Venkata Harika (Student)  
  - Affiliation: Department of CSE, VVIT, Guntur, AP, India

🚀 Usage

🔧 Installation

  git clone https://github.com/your-repo-url
  cd BigMartSalesForecasting
  pip install -r requirements.txt
  python app.py

▶️ Running the App

  1. Select a prediction model
  2. Enter all required item and outlet attributes
  3. Click "Predict Sales" to view results

🔮 Future Enhancements

  - User authentication
  - Integration with E-commerce Platforms: Extend the solution to include a feature for price comparison across multiple e-commerce platforms for enhanced customer insights.
  - Dynamic Outlet Features: Incorporate dynamic features like monthly footfall, sales promotions, and marketing campaigns into the model to improve prediction.



