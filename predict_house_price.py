import joblib
import numpy as np

# Load trained model
model = joblib.load("house_price_model.pkl")

print("=== House Price Prediction ===")

# Take user inputs
MedInc = float(input("Enter Median Income: "))
HouseAge = float(input("Enter House Age: "))
AveRooms = float(input("Enter Average Rooms: "))
AveBedrms = float(input("Enter Average Bedrooms: "))
Population = float(input("Enter Population: "))
AveOccup = float(input("Enter Average Occupancy: "))
Latitude = float(input("Enter Latitude: "))
Longitude = float(input("Enter Longitude: "))

# Create input array
input_data = np.array([[
    MedInc,
    HouseAge,
    AveRooms,
    AveBedrms,
    Population,
    AveOccup,
    Latitude,
    Longitude
]])

# Predict
prediction = model.predict(input_data)

print("\nPredicted House Price:")
print(prediction[0], "(in hundred-thousands of dollars)")

