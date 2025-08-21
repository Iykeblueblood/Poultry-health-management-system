import pandas as pd
import plotly.express as px

def create_diagnosis_chart(disease_scores):
    """
    Creates a horizontal bar chart to visualize the likelihood of diagnosed diseases.
    """
    if not disease_scores:
        return None

    df = pd.DataFrame(list(disease_scores.items()), columns=['Disease', 'Likelihood Score'])
    df = df.sort_values(by='Likelihood Score', ascending=False)
    
    fig = px.bar(
        df,
        x='Likelihood Score',
        y='Disease',
        orientation='h',
        title='Potential Disease Diagnosis Likelihood',
        labels={'Likelihood Score': 'Likelihood Score (Higher is more likely)', 'Disease': ''},
        text='Likelihood Score',
        color='Likelihood Score',
        color_continuous_scale=px.colors.sequential.Reds
    )
    
    fig.update_traces(textposition='outside')
    fig.update_layout(
        yaxis={'categoryorder':'total ascending'},
        title_font_size=20,
        xaxis_title_font_size=14,
        yaxis_title_font_size=14
    )
    
    return fig