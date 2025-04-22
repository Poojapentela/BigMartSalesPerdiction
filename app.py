from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load models
linear_model = pickle.load(open('linear_model.pkl', 'rb'))
poly_model = pickle.load(open('poly_model.pkl', 'rb'))
rf_model = pickle.load(open('rf_model.pkl', 'rb'))
gb_model = pickle.load(open('gb_model.pkl', 'rb'))
cat_model = pickle.load(open('cat_model.pkl', 'rb'))

# Load transformers
poly_features = pickle.load(open('poly_features.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        # Extract features
        Item_Identifier = float(request.form["Item_Identifier"])
        Item_weight = float(request.form["Item_weight"])
        Item_Fat_Content = float(request.form["Item_Fat_Content"])
        Item_visibility = float(request.form["Item_visibility"])
        Item_Type = float(request.form["Item_Type"])
        Item_MPR = float(request.form["Item_MPR"])
        Outlet_identifier = float(request.form["Outlet_identifier"])
        Outlet_established_year = float(request.form["Outlet_established_year"])
        Outlet_size = float(request.form["Outlet_size"])
        Outlet_location_type = float(request.form["Outlet_location_type"])
        Outlet_type = float(request.form["Outlet_type"])
        
        selected_model = request.form.get("model_selection", "linear")

        features = np.array([[Item_Identifier, Item_weight, Item_Fat_Content, 
                              Item_visibility, Item_Type, Item_MPR, 
                              Outlet_identifier, Outlet_established_year, 
                              Outlet_size, Outlet_location_type, Outlet_type]])

        if selected_model == "linear":
            features_scaled = scaler.transform(features)
            prediction = linear_model.predict(features_scaled)[0]
        elif selected_model == "polynomial":
            features_scaled = scaler.transform(features)
            features_poly = poly_features.transform(features_scaled)
            prediction = poly_model.predict(features_poly)[0]
        elif selected_model == "random_forest":
            prediction = rf_model.predict(features)[0]
        elif selected_model == "gradient_boosting":
            prediction = gb_model.predict(features)[0]
        elif selected_model == "catboost":
            prediction = cat_model.predict(features)[0]
        else:
            prediction = rf_model.predict(features)[0]

        formatted_prediction = f"₹{prediction:.2f}"
        
        return render_template('index.html', 
                               prediction=formatted_prediction, 
                               selected_model=selected_model)

if __name__ == "__main__":
    app.run(debug=True)
