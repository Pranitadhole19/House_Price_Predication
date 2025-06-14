from flask import Flask, request, render_template
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

model_path = r'C:\Users\Pranita\OneDrive\Desktop\House price predication\house_price_model.pkl'

with open(model_path, 'rb') as file:
    model_dict = pickle.load(file)
    model = model_dict['model']  

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST']) 
def predict():
    try:
        
        total_sqft = float(request.form['total_sqft'])
        bath = float(request.form['bath'])
        bhk = float(request.form['bhk'])
        location = request.form['location_encoded']

        location_encoded = le.fit_transform([location])[0]

        final_features = np.array([[location_encoded, total_sqft, bath, bhk]])

        prediction = model.predict(final_features)
        output = round(prediction[0], 2)

        return render_template('index.html', prediction_text=f'Predicted House Price: ₹{output:,}')

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')


if __name__ == "__main__":
    app.run(debug=True)
