# rule_based_system.py

def get_symptoms_list():
    """Returns a master list of all possible symptoms for the UI."""
    symptoms = [
        # Respiratory
        "Sneezing", "Nasal Discharge", "Swollen Eyes", "Coughing", "Gasping",
        "Rattling Noises", "Swollen Sinuses", "Bloody Mucus in Trachea",

        # Digestive
        "Bloody Diarrhea", "Watery Greenish Diarrhea", "Yellowish Diarrhea",
        "Pasting of Feces on Vent", "Foul-smelling Diarrhea",

        # Neurological
        "Nervous Signs (Paralysis)", "Paralysis of Legs/Wings", "Tremors in Young Chicks",
        "Twisting of Head/Neck (Torticollis)",

        # General / Systemic
        "Loss of Appetite", "Ruffled Feathers", "Huddling Together", "Sudden Death",
        "Cyanosis of Comb/Wattles", "Lameness", "Swollen Hocks",

        # Production
        "Sudden Drop in Egg Production", "Soft-shelled/Misshapen Eggs",

        # External / Physical
        "Feather Loss", "Skin Irritation", "Visible Insects", "Scaly Lesions on Legs",
        "Wart-like Lesions", "Cheesy Deposits in Mouth"
    ]
    return sorted(symptoms)

def diagnose_diseases(selected_symptoms):
    """
    Applies a comprehensive set of rules (~40) to the selected symptoms.
    Returns a dictionary mapping diseases to their likelihood scores.
    """
    # Initialize scores for all potential diseases
    disease_scores = {
        "Infectious Coryza": 0, "Infectious Bronchitis": 0, "Newcastle Disease": 0,
        "Mycoplasmosis (CRD)": 0, "Infectious Laryngotracheitis": 0, "Coccidiosis": 0,
        "Fowl Cholera": 0, "Pullorum Disease": 0, "Necrotic Enteritis": 0,
        "Marek's Disease": 0, "Avian Encephalomyelitis": 0, "Egg Drop Syndrome": 0,
        "Lice or Mites": 0, "Scaly Leg Mites": 0, "Fowl Pox": 0,
        "Avian Influenza (HPAI)": 0, "Mycoplasma Synoviae": 0
    }

    # --- Rule Set (40+ individual checks) ---

    # General Symptoms (low score, but can support a diagnosis)
    if "Loss of Appetite" in selected_symptoms:
        for disease in ["Coccidiosis", "Newcastle Disease", "Fowl Cholera", "Necrotic Enteritis", "Avian Influenza (HPAI)"]:
            disease_scores[disease] += 1
    if "Ruffled Feathers" in selected_symptoms or "Huddling Together" in selected_symptoms:
        for disease in ["Coccidiosis", "Pullorum Disease", "Infectious Bronchitis"]:
            disease_scores[disease] += 1

    # Respiratory Rules
    # R1-R3: Infectious Coryza
    if "Sneezing" in selected_symptoms: disease_scores["Infectious Coryza"] += 1
    if "Nasal Discharge" in selected_symptoms: disease_scores["Infectious Coryza"] += 2
    if "Swollen Eyes" in selected_symptoms: disease_scores["Infectious Coryza"] += 2
    
    # R4-R7: Infectious Bronchitis
    if "Coughing" in selected_symptoms: disease_scores["Infectious Bronchitis"] += 1
    if "Gasping" in selected_symptoms: disease_scores["Infectious Bronchitis"] += 1
    if "Rattling Noises" in selected_symptoms: disease_scores["Infectious Bronchitis"] += 2
    if "Sudden Drop in Egg Production" in selected_symptoms or "Soft-shelled/Misshapen Eggs" in selected_symptoms:
        disease_scores["Infectious Bronchitis"] += 2
        disease_scores["Egg Drop Syndrome"] += 2

    # R8-R12: Newcastle Disease
    if "Gasping" in selected_symptoms and "Coughing" in selected_symptoms:
        disease_scores["Newcastle Disease"] += 1
    if "Nervous Signs (Paralysis)" in selected_symptoms:
        disease_scores["Newcastle Disease"] += 2
    if "Twisting of Head/Neck (Torticollis)" in selected_symptoms:
        disease_scores["Newcastle Disease"] += 3 # Strong indicator
    if "Watery Greenish Diarrhea" in selected_symptoms:
        disease_scores["Newcastle Disease"] += 1
    if "Sudden Drop in Egg Production" in selected_symptoms:
        disease_scores["Newcastle Disease"] += 1

    # R13-R14: Mycoplasmosis (CRD)
    if "Nasal Discharge" in selected_symptoms and "Rattling Noises" in selected_symptoms:
        disease_scores["Mycoplasmosis (CRD)"] += 2
    if "Swollen Sinuses" in selected_symptoms:
        disease_scores["Mycoplasmosis (CRD)"] += 2
        
    # R15-R16: Infectious Laryngotracheitis (ILT)
    if "Gasping" in selected_symptoms and "Coughing" in selected_symptoms:
        disease_scores["Infectious Laryngotracheitis"] += 1
    if "Bloody Mucus in Trachea" in selected_symptoms:
        disease_scores["Infectious Laryngotracheitis"] += 4 # Very strong indicator

    # Digestive Rules
    # R17-R18: Coccidiosis
    if "Bloody Diarrhea" in selected_symptoms:
        disease_scores["Coccidiosis"] += 4 # Very strong indicator
    if "Loss of Appetite" in selected_symptoms and "Ruffled Feathers" in selected_symptoms:
        disease_scores["Coccidiosis"] += 1

    # R19-R21: Fowl Cholera
    if "Watery Greenish Diarrhea" in selected_symptoms or "Yellowish Diarrhea" in selected_symptoms:
        disease_scores["Fowl Cholera"] += 2
    if "Cyanosis of Comb/Wattles" in selected_symptoms:
        disease_scores["Fowl Cholera"] += 2
    if "Sudden Death" in selected_symptoms:
        disease_scores["Fowl Cholera"] += 1

    # R22: Pullorum Disease
    if "Pasting of Feces on Vent" in selected_symptoms and "Huddling Together" in selected_symptoms:
        disease_scores["Pullorum Disease"] += 3 # Strong indicator in chicks

    # R23: Necrotic Enteritis
    if "Foul-smelling Diarrhea" in selected_symptoms and "Sudden Death" in selected_symptoms:
        disease_scores["Necrotic Enteritis"] += 3

    # Neurological Rules
    # R24: Marek's Disease
    if "Paralysis of Legs/Wings" in selected_symptoms:
        disease_scores["Marek's Disease"] += 4 # Very strong indicator
        disease_scores["Nervous Signs (Paralysis)"] += 1 # Add to generic nervous signs

    # R25: Avian Encephalomyelitis
    if "Tremors in Young Chicks" in selected_symptoms:
        disease_scores["Avian Encephalomyelitis"] += 4 # Strong indicator in young birds

    # External / Physical Rules
    # R26-R28: Lice or Mites
    if "Feather Loss" in selected_symptoms: disease_scores["Lice or Mites"] += 1
    if "Skin Irritation" in selected_symptoms: disease_scores["Lice or Mites"] += 1
    if "Visible Insects" in selected_symptoms: disease_scores["Lice or Mites"] += 3 # Strong indicator

    # R29: Scaly Leg Mites
    if "Scaly Lesions on Legs" in selected_symptoms:
        disease_scores["Scaly Leg Mites"] += 3 # Very specific

    # R30-R31: Fowl Pox
    if "Wart-like Lesions" in selected_symptoms:
        disease_scores["Fowl Pox"] += 4 # Strong indicator (dry form)
    if "Cheesy Deposits in Mouth" in selected_symptoms:
        disease_scores["Fowl Pox"] += 3 # Strong indicator (wet form)

    # R32-R34: Avian Influenza (High Pathogenicity - HPAI)
    if "Sudden Death" in selected_symptoms:
        disease_scores["Avian Influenza (HPAI)"] += 2
    if "Cyanosis of Comb/Wattles" in selected_symptoms:
        disease_scores["Avian Influenza (HPAI)"] += 2
    if "Gasping" in selected_symptoms and "Nervous Signs (Paralysis)" in selected_symptoms:
        disease_scores["Avian Influenza (HPAI)"] += 2

    # R35-R37: Mycoplasma Synoviae
    if "Lameness" in selected_symptoms: disease_scores["Mycoplasma Synoviae"] += 2
    if "Swollen Hocks" in selected_symptoms: disease_scores["Mycoplasma Synoviae"] += 2
    if "Rattling Noises" in selected_symptoms: disease_scores["Mycoplasma Synoviae"] += 1

    # R38: Egg Drop Syndrome
    if "Soft-shelled/Misshapen Eggs" in selected_symptoms and "Sudden Drop in Egg Production" in selected_symptoms:
        disease_scores["Egg Drop Syndrome"] += 2


    # Final step: Filter out diseases with a score of 0
    probable_diseases = {disease: score for disease, score in disease_scores.items() if score > 0}
    
    return probable_diseases