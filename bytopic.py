import requests
import bs4

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
def getdata(query):
    
    url="https://www.india.com/topic/"+query+"/page/"
    output=""
    
    

    for k in range(1,4):
        try:

            res = requests.get(url+f"{k}"+'/',headers).text
           
        except:
            
            return "Try another topic"

        soup = bs4.BeautifulSoup(res,'lxml')
        i = soup.find_all('li',class_="contentblk blkwrp")
        
        for a in range(0,len(i)):
            p=i[a].findAll("p")
            headline=i[a].img['title']
            paragraph=p[1].text
            image_url=i[a].img["data-lazy-src"]
            source_url=i[a].a['href']
            date=p[0].text
            date=date.replace('<a href="https://www.india.com/author/newsdesk/">India.com </a>',"")
            date=date.replace("\nIndia.com News Desk\n","")
            date=date.replace("India.com","")
            date=date.strip()
            

            #result={"headline":headline ,"paragraph":paragraph,"image url":image_url,"source url":source_url}
            #output.append(result)
            result=f""" <div class="gridelement" style="align-self: center;
    display: inline-block;
    font-family: 'Raleway', sans-serif;
    width: 45%;
    border-radius: 20px;
    border-left: salmon;
    margin-bottom:5px;
    
    
    padding: 5px 5px 5px 5px;
    box-shadow: 3px 3px 3px 3px #e1eaee;">
        <body style="text-align:center">
            <center style=" font-family:arial">
            
            
            <img src="{image_url}" alt="" width="97%" height="35%" style="border-radius:12px; object-fit:cover;"><br>
            <br>
            <h2 style="color:#000000;font-size:19px;">{headline}</h2>
            <div class="text" style="width:90%;>
            
            <h2 style="width:90%; font-size:12px;">Description: {paragraph}</h2><h2>
                <h1 style="font-size:18px; color: rgb(32, 7, 122);">{date}</h1>
            
            
            <div style="color:#0918B3">
            
            <div>
            </div>
            
            <button class="btn danger" onclick="window.location.href='{source_url}'" style="width:90%;
                border: 2px solid black;
                background-color: white;
                color: black;
                padding: 14px 28px;
                font-size: auto;
                cursor: pointer;
                border-radius:15px;
                float:center; 
                background: hsl(214, 81%, 51%);
                color: white;">Read More</button><br><br>
            
                
            
            </div></div></center></body>
    </div>"""
            output=output+result
    
    output=f""" <html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" type="image/x-icon" href="https://telegra.ph/file/ccba9696db89a8598b8fe.png">
    <title>Search Results</title>
    
<style>
    @import url('https://fonts.googleapis.com/css2?family=Kumbh+Sans&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans&family=Raleway:wght@100;500&display=swap');
   



</style>
</head>
<body>
    <center><h2>
    <div class="header" ><img src="https://telegra.ph/file/ccba9696db89a8598b8fe.png" alt="" style="max-width: 100px;"></div>
    <div class="header" style="border-radius: 20px;font-family:monospace;font-size:30px;align-self: center;vertical-align: middle;width: 50%; margin-top:2%">Search Results</div>
    </center></h2>
    <div class="gridcontainer" style="padding-top:1%;border-radius: 20px; align-self: center;vertical-align: middle;width: 100%;">
     {output}
    </div>
</body>
</html>"""
    print(f"bytopic {query}")
    return output







