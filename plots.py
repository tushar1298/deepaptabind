import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def interaction_barplot(data):

    df=pd.DataFrame(data.items(),columns=["Interaction","Count"])

    fig,ax=plt.subplots()

    sns.barplot(x="Interaction",y="Count",data=df,ax=ax)

    return fig
