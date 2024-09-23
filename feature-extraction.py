import re

def extract_features(transcription):
    features = {
        "name": None,
        "age": None,
        "weight": None,
        "height": None
    }

    # Define patterns for each feature
    
    # Name extraction (simple pattern matching)
    name_match = re.search(r"मेरा नाम ([\w\s]+) है|मैं ([\w\s]+) हूँ|My name is ([\w\s]+)", transcription, re.IGNORECASE)
    if name_match:
        features["name"] = name_match.group(1) or name_match.group(2) or name_match.group(3)

    # Age extraction
    age_match = re.search(r"मैं (\d{1,2}) साल का हूँ|My age is (\d{1,2})|I am (\d{1,2}) years old", transcription)
    if age_match:
        features["age"] = age_match.group(1) or age_match.group(2) or age_match.group(3)

    # Weight extraction (kg)
    weight_match = re.search(r"मेरा वजन (\d{1,3}) किलो है|My weight is (\d{1,3}) kg|I weigh (\d{1,3}) kg", transcription)
    if weight_match:
        features["weight"] = weight_match.group(1) or weight_match.group(2) or weight_match.group(3)

    # Height extraction (cm, feet)
    height_match_cm = re.search(r"मेरी ऊंचाई (\d{2,3}) सेंटीमीटर है|My height is (\d{2,3}) cm", transcription)
    height_match_ft = re.search(r"मेरी ऊंचाई (\d) फीट (\d{1,2}) इंच है|My height is (\d) feet (\d{1,2}) inches", transcription)
    
    if height_match_cm:
        features["height"] = f"{height_match_cm.group(1)} cm"
    elif height_match_ft:
        features["height"] = f"{height_match_ft.group(1)} feet {height_match_ft.group(2)} inches"

    return features
