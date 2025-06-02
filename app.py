from flask import Flask, request, render_template
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

# Use raw string or double backslashes to fix path issue
model_path = r'C:\Users\Pranita\OneDrive\Desktop\House price predication\home_prices_model.pkl'

# Load model
#with open(model_path, 'rb') as file:
#    model = pickle.load(file)
# Load model
with open(model_path, 'rb') as file:
    model_dict = pickle.load(file)
    model = model_dict['model']  # ✅ Correct: extract the model object

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])  # FIXED 'method' → 'methods'
def predict():
    try:
        # Assuming order: location, bhk, bath, total_sqft
        total_sqft = float(request.form['total_sqft'])
        bath = float(request.form['bath'])
        bhk = float(request.form['bhk'])
        location = request.form['location_encoded']

        location_encoded = le.fit_transform([location])[0]

        # Example if model expects [location_encoded, total_sqft, bath, bhk]
        final_features = np.array([[location_encoded, total_sqft, bath, bhk]])

        prediction = model.predict(final_features)
        output = round(prediction[0], 2)

        return render_template('index.html', prediction_text=f'Predicted House Price: ₹{output:,}')

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')


if __name__ == "__main__":
    app.run(debug=True)
