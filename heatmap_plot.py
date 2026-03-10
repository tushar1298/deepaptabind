import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def interaction_heatmap(data):

    df=pd.DataFrame(list(data.items()),
                    columns=["Interaction","Count"])

    fig,ax=plt.subplots()

    sns.heatmap(df[["Count"]],annot=True,cmap="viridis",ax=ax)

    ax.set_yticklabels(df["Interaction"])

    return fig
