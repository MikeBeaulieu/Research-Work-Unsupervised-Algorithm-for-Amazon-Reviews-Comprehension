import nltk
import unirest
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import webtext
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
text = webtext.raw("sample_review.txt")
sent_tokenizer = PunktSentenceTokenizer(text)
image_list=[]
battery_list=[]
cs_list=[]
night_list=[]
LCD_list=[]
video_list=[]
price_list=[]
A_list=[["Battery/Charger","Battery","power","charge"],["Image Quality","image","picture","photo","pic","photograph","jpeg""jpg"],["Customer service","service","dealer","seller","customer"],["Night Mode","night","low light","noise","ISO","noisy"],["LCD Display","LCD","display","screen"],["Video Recordings","video","HD","FULL HD","recording"],["price","price","money","$"]]
battery_list1=[]
score_battery=[]
pos_noise=[]
neg_noise=[]
neu_noise=[]
len_pos_noise=[]
len_neg_noise=[]
len_neu_noise=[]
print("Generating sentences related to battery")
for a in sent_tokenizer.tokenize(text):
#for a in nltk.sent_tokenize(apple1):
    for i in range(1,len(A_list[0])):
      if A_list[0][i] in a :
        battery_list.append(a)
len(battery_list)


print("Sentences related to Customer Service/Dealer")
for a in sent_tokenizer.tokenize(text):
#for a in nltk.sent_tokenize(apple1):
    for i in range(1,len(A_list[2])):
      if A_list[2][i] in a :
        cs_list.append(a)

print("Sentences related to picture quality")
for a in sent_tokenizer.tokenize(text):
#for a in nltk.sent_tokenize(apple1):
    for i in range(1,len(A_list[1])):
      if A_list[1][i] in a :
        image_list.append(a)
print("Sentences related to Night Shot/Low Light")
for a in sent_tokenizer.tokenize(text):
#for a in nltk.sent_tokenize(apple1):
    for i in range(1,len(A_list[3])):
      if A_list[3][i] in a :
        night_list.append(a)

print("Sentences related to LCD")
for a in sent_tokenizer.tokenize(text):
#for a in nltk.sent_tokenize(apple1):
    for i in range(1,len(A_list[4])):
      if A_list[4][i] in a :
        LCD_list.append(a)

print("Sentences related to video")
for a in sent_tokenizer.tokenize(text):
#for a in nltk.sent_tokenize(apple1):
    for i in range(1,len(A_list[5])):
      if A_list[5][i] in a :
        video_list.append(a)

print("Sentences related to price")
for a in sent_tokenizer.tokenize(text):
#for a in nltk.sent_tokenize(apple1):
    for i in range(1,len(A_list[6])):
      if A_list[6][i] in a :
        price_list.append(a)

feature_list=[battery_list,image_list,cs_list,night_list,LCD_list,video_list,price_list]
#for t in nltk.sent_tokenize(text):
for z in range(0,len(feature_list)):
 pos_noise=[]
 neg_noise=[]
 neu_noise=[]
 for t in feature_list[z]:

    response = unirest.post("https://twinword-sentiment-analysis.p.mashape.com/analyze/",
      headers={
        "X-Mashape-Key": "tjjVtCG5jGmshJeVFdWA0miNaKLwp1xn80Mjsnz1zNsU6jtqdZ",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
      },
     params={
      "text": t
      }
    )


    if (response.body['type']=="positive"):
      pos_noise.append(t)
    if (response.body['type']=="neutral"):
      neu_noise.append(t)
    if (response.body['type']=="negative"):
      neg_noise.append(t)

 print("Feature:")
 print(A_list[z][0])
 pos_noise=list(set(pos_noise))
 neg_noise=list(set(neg_noise))
 neu_noise=list(set(neu_noise))
 print("\n")
 len_pos_noise.append(len(pos_noise))
 print("Positive sentences:"+str(len(pos_noise)))
 print("\n".join(pos_noise))
 print("\n")
 len_neg_noise.append(len(neg_noise))
 print("Negative sentences:"+str(len(neg_noise)))
 print("\n".join(neg_noise))
 print("\n")
 print("Neutral sentences:"+str(len(neu_noise)))
 print("\n".join(neu_noise))
 len_neu_noise.append(len(neu_noise))
n_groups = 7
means_frank = (int(len_pos_noise[0]),int(len_pos_noise[1]),int(len_pos_noise[2]),int(len_pos_noise[3]),int(len_pos_noise[4]),int(len_pos_noise[5]),int(len_pos_noise[6]))
means_guido = (int(len_neg_noise[0]),int(len_neg_noise[1]),int(len_neg_noise[2]),int(len_neg_noise[3]),int(len_neg_noise[4]),int(len_neg_noise[5]),int(len_neg_noise[6]))
means_neu=    (int(len_neu_noise[0]),int(len_neu_noise[1]),int(len_neu_noise[2]),int(len_neu_noise[3]),int(len_neu_noise[4]),int(len_neu_noise[5]),int(len_neu_noise[6]))
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.6

rects1 = plt.bar(index, means_frank, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Positive')


rects2 = plt.bar(index + bar_width, means_guido, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Negative')


plt.xlabel('Feature Names')
plt.ylabel('Ratings')
plt.title('Sigma SC-DP1')
plt.xticks(index + bar_width , ('Battery/Charger', 'ImageQuality','Service', 'NightMode', 'LCDDisplay',"Video", 'Price'))
plt.legend()

plt.tight_layout()
plt.show()