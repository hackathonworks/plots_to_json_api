# 1. Library imports
import uvicorn
from fastapi import FastAPI
#from fastapi.responses import HTMLResponse
import pandas as pd
import plotly_express as px
from scatterjs import scatterjs

app = FastAPI()

@app.post('/scatterplot')
def predict_results(data:scatterjs):
    data = data.dict()
    df_link=data['df_link']
    x=data['x']
    y=data['y']
    z=data['z']
    color_attribute=data['color_attribute']
    df=pd.read_csv(str(df_link))
    fig = px.scatter_3d(df, x=str(x), y=str(y), z=str(z),color=str(color_attribute))
    return fig.to_json()
    #return [df_link,x,y,z,color_attribute]


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn plotweb:app --reload