#Sample Data
soil_crop_mapping = {
    'clay': ['Rice', 'Wheat', 'Soybeans', 'Barley', 'Cotton'],
    'sandy': ['Carrots', 'Potatoes', 'Peanuts', 'Onions', 'Garlic'],
    'loamy': ['Tomatoes', 'Corn', 'Cucumbers', 'Peppers', 'Eggplant'],
    'silt': ['Beans', 'Lettuce', 'Chilies', 'Broccoli', 'Cauliflower'],
    'peat': ['Cranberries', 'Blueberries', 'Strawberries', 'Mint', 'Oregano'],
    'chalky': ['Spinach', 'Beetroot', 'Cabbage', 'Sweet Corn', 'Zucchini']
}

soil_health_tips = {
    'poor': 'Add organic compost, improve drainage, and perform crop rotation.',
    'average': 'Use balanced fertilizers, reduce tillage, and monitor soil pH.',
    'good': 'Maintain current practices, consider cover cropping, and regularly check pH levels.',
    'excellent': 'Continue with sustainable practices, and consider adding organic matter for long-term health.'
}

disease_symptoms_mapping = {
    'yellow leaves': 'Nitrogen deficiency. Suggest using a nitrogen-rich fertilizer.',
    'brown spots': 'Fungal infection. Suggest using a fungicide.',
    'wilting': 'Lack of water or root disease. Suggest improving irrigation or checking roots.',
    'white powdery coating': 'Powdery mildew. Suggest using a sulfur-based fungicide.',
    'black spots on leaves': 'Bacterial infection. Suggest using copper-based fungicides and improving air circulation.'
}

# Functions
def suggest_crops(soil_type):
    return soil_crop_mapping.get(soil_type.lower(), 'Unknown soil type')

def soil_management(soil_condition):
    return soil_health_tips.get(soil_condition.lower(), 'Unknown soil condition')

def identify_disease(symptom):
    return disease_symptoms_mapping.get(symptom.lower(), 'Unknown symptom. Consult an expert.')

#Input
print("Welcome to the Crop and Soil Management System!")
soil_type = input("Enter your soil type (clay, sandy, loamy, silt, peat, chalky): ")
soil_condition = input("Enter the current condition of your soil (poor, average, good, excellent): ")
symptom = input("Enter the symptom observed in crops (yellow leaves, brown spots, wilting, white powdery coating, black spots on leaves): ")

#output
print("\nRecommendations:")
print(f"Suitable crops for {soil_type} soil: {suggest_crops(soil_type)}")
print(f"Soil management tip: {soil_management(soil_condition)}")
print(f"Possible disease diagnosis: {identify_disease(symptom)}")

