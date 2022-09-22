import streamlit as st
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_wine, load_iris
import plotly.express as px

iris_data = load_iris()

df_form = pd.DataFrame(
    data=iris_data.data, 
    columns=[" ".join(f.split(" ")[:-1]) for f in iris_data.feature_names]
)
df_form['species'] = iris_data.target
st.write(
    """
    # Iris Dataset
    How do iris petal characteristics vary by species? 
    """
)

plotly_fig = px.scatter_3d(
    data_frame=df_form,
    x='petal length',
    y='petal width',
    z='sepal length',
    color='species',
    opacity=.8,
)
plotly_fig.update_traces(marker={'size':5})
st.plotly_chart(plotly_fig)