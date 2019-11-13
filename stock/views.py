from django.shortcuts import render
import json
from pandas.io.json import json_normalize
import urllib.request
import numpy as np
import pandas as pd
# Create your views here.
def home(request):
    if request.POST:
        c=request.POST['company']
        token='OIKFPW67DYMKB4VT'
        url=f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={c}&interval=5min&apikey={token}'
        print(url)
        
        
        with urllib.request.urlopen(url) as response:

            elevations = response.read()
            data = json.loads(elevations)
            df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
            df.reset_index(level=0, inplace=True)
            
            
            closing=list(df['4. close'])
            
            date=list(df['index'])
            
            context={
                'c':closing,
                'i':date,
                'latest':closing[0],
                'ldate':str(date[0])
            }   
            return render(request,'index.html',context) 
            

            
    return render(request,'index.html')
