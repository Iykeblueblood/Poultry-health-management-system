import streamlit as st
import google.generativeai as genai

def configure_generative_ai():
    """Configures the generative AI model with an API key from st.secrets."""
    api_key = st.secrets.get("GEMINI_API_KEY")
    
    if not api_key:
        st.error("GEMINI_API_KEY not found. Please add it to your .streamlit/secrets.toml file.")
        st.stop()
        
    genai.configure(api_key=api_key)

def get_generative_advice(disease_name):
    """
    Generates detailed management advice for a given poultry disease using the Gemini API.
    """
    try:
        # --- THIS IS THE LINE WE UPDATED ---
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""
        Act as a veterinary expert specializing in poultry health.
        For a small-scale poultry farmer who suspects their flock has '{disease_name}', provide a detailed and practical action plan. 
        Structure your response into the following sections using Markdown for formatting:
        
        ### 1. Immediate Actions
        What are the first 3-4 steps they should take right now (e.g., isolation, observation)?
        
        ### 2. Disease Description
        Briefly explain what {disease_name} is in simple, easy-to-understand terms.
        
        ### 3. Common Treatment & Management
        What are the typical management strategies or treatments? **Crucially, advise them to consult a licensed veterinarian for any prescriptions or a definitive diagnosis.**
        
        ### 4. Prevention & Biosecurity
        What long-term measures can they implement to prevent this disease in the future?
        
        Please provide a clear, concise, and actionable response.
        """
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        error_message = f"Could not generate advice for {disease_name}. Error: {e}. Please check your API key and internet connection."
        return error_message