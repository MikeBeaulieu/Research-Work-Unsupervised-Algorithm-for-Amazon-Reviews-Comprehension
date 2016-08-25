from nltk.tokenize import sent_tokenize,word_tokenize
import  testapi
from textblob import TextBlob
example_txt="""
The Nikon D3300 has some of the best low light and best picture quality of mid level DSLR cameras, in the APS-C sensor size (this is not a full size sensor, but to get a full size sensor you will need to spend about $2000 or $3000 more).

Nikon D3300 is rated 30% higher in image quality compared to the Canon 70D.

The Nikon D3300 has a slightly larger sensor than the Canon 70D.

I was torn between Canon and Nikon. If you look at all the complaints about Canon in the last 1 or 2 years, you will see that they have been going backwards or sideways, while other companies are making huge strides. The Canon 70D is a smooth fast auto-focusing camera that is silent, however if you set it to auto mode and go take pictures they don't look as good as the Nikon D3300 on auto mode.

Comparing pictures side by side with the Canon 70D, the Nikon D3300 has sharper pictures. Zooming in on the photos I took with the 70D yielded a loss of detail. At the same quality settings, same aperture, and shutter speed settings, and with the exact same scene, I am able to zoom in and get better photos from the Nikon D3300, the D3300 really captures crisp photos.

The D3300 may be the only camera that doesn't have image quality problems with the 24 Megapixels. There is a megapixel war going on, although sensor sizes aren't increasing, which means the image quality isn't getting better with many cameras, because they are simply trying to cram more pixels with even less light per pixel, which doesn't help matters. However, the D3300 pulls off the impossible and gets beautiful very sharp photos every time.

The D3300 does very good video, it's glassy smooth and has tremendously good low light video performance, although the focus noise of the lens will intrude on your videos, because you can hear the little motor churning away to maintain focus. You can alternately use manual focus which works just fine for video. Or you can just push the focus button momentarily to get focus and then maintain your distance, and that will allow the lens to stop hunting for focus, which means you won't hear any noise in your video. To eliminate video focus noise you will need an external mic. The auto focus isn't super fast in video mode but it does have video auto focus mode, and if you had an external mic you could do simple documentaries or YouTube clips just fine and have very clean, very smooth video.

For video you could also consider a Sony HX-300 1080 60P, or the HX-400 which has 24P mode too. I've tried the HX-300 and it has nowhere near the low light performance of the Nikon D3300 but it does do really good video and has smooth, fast, silent auto focus, even at up to 50x zoom, which is ridiculous.

The Nikon D3300 takes noise free pictures in any lighting conditions (I haven't tried in total darkness of course). I set it to auto on a black cloudy day, just before rain, and it takes extremely clear pictures with no noise. The same pictures in sunlight were much less sharp, on the Canon 70D. The Canon 70D may be able to match the Nikon if you manually tweak things, but the Nikon doesn't take bad pictures on Auto mode, where as, the Canon 70D on Auto mode takes very average pictures.

I noticed the Canon 70D JPG pictures looked very digitized, and not natural, some were not even usable on auto mode, but the Nikon default JPG pictures look more natural. This is probably caused by better JPG compression on the Nikon? In "Raw" shooting mode I'm sure the Canon 70D has nearly equal image quality but I never did try that.

Something to note, the Nikon D3300 does not have a low pass filter on the sensor like most current DSLR's, so in theory it should shoot sharper photos more easily. The purpose of the low pass filter is to slightly blur pixels to prevent artifacts, and moire. The Nikon figured out a way around this, so it can shoot sharper without a "blur" filter. Canon people don't seem to care about anything except loyalty to one brand, so good luck explaining this to them! hehe.

This is a very small camera, I would say it feels about 50% smaller than a Canon 70D. It is very light. The buttons are all exceptional. The shutter is very loud as most DSLR cameras probably are. Taking pictures is as easy as turning it on and snapping photos. You'll get amazing results in almost any lighting with this camera.

If you want the best quality pictures, and you want to step up to a professional camera without the professional price, here is the camera you want. Image quality is within 1 point of the Nikon D7100. The entry level Canon DSLR mid-frame cameras cannot match the image quality of the newest Nikons.

Purchase an 18-200mm lens in the future to give you wide angle room shots, or scenic shots at 18mm, or to zoom in, at 200mm. The stock lens works fine, but it doesn't zoom in very far. That is something to consider in your purchase because of the price of lenses. However, this camera will last you for years, and it is a good investment.

Edit: The low light performance of the D3300 is supposed to be very good compared to older Nikon models. I can attest that this is true. In fact, I am shocked at how good the low light performance is. With the use of a tripod, you can turn down the shutter speed so it stays open for several seconds or longer. The picture I took in a non-lighted region of my house looked identical to a normally lit room with bright crisp exposure, and I was able to use ISO 100 setting, there was NO noise. Now this is something you simply cannot do with a point and shoot camera with a smaller sensor. So exciting!

I highly recommend the Nikon D3300 because it does everything very well.
I like the camera. It appears very well built and ergonomic. I was surprised though to see that you can only get high
definition in RAW format. In fine definition the average picture is much lower than the 24 mp they claim.
The lens kit is also fine for the price. I came from Canon world and transitioned into the Lumix world for digital.
I think their lenses are better but they do not offer (at least not on mine) the capabilities of a d-SLR camera.
Last thing and the reason for my rating is a terrible customer service. My battery run out in less than 30 days.
Nikon would not replace it as they indicated it was not covered. They would charge $50-$60 for a replacement.
It is not a a good experience and not acceptable from such a reputable company.

Horrible. My lenses motor was faulty out of the box.
Don't buy it is not worth wasting 500 dollars on a faulty product.
"""
print("The acutal review"+example_txt)
url = "http://text-processing.com/api/sentiment/"

example_updated=(sent_tokenize(example_txt))
sentenced=[]
txt=[]
i=0
for sent in example_updated:
    i=i+1
    sentenced.append(sent)
x=0
pos=0
neg=0
positive=[]
negative=[]
zoom_sentenced=[]
price_sentenced=[]
shutter_sentenced=[]
lens_sentenced=[]
picture_sentenced=[]
battery_sentenced=[]
customer_review=[]

print "\n Sentences related to zoom \n"
for j in range(i):
    if "zoom" in sentenced[j]:
        b=TextBlob(sentenced[j])
        print("The Sentiment using TextBlob is \t")
        print(sentenced[j])
        print(b.sentiment)
        zoom_sentenced.append(sentenced[j])

testapi.app(zoom_sentenced,j)

print("\n Sentences related to price \n")
for j in range(i):
    if "price" in sentenced[j]:
        b=TextBlob(sentenced[j])
        print(sentenced[j])
        print(b.sentiment)
        price_sentenced.append(sentenced[j])
testapi.app(price_sentenced,j)

print("\n Sentences related to Shutter speed \n")
for j in range(i):
     if "shutter" in sentenced[j] and  "zoom" not in sentenced[j]:
        b=TextBlob(sentenced[j])
        print(sentenced[j])
        print(b.sentiment)
        shutter_sentenced.append(sentenced[j])
testapi.app(shutter_sentenced,j)

print("\n Sentences related to lens \n")
for j in range(i):
     if "lens" in sentenced[j] or "wide angle" in sentenced[j]:
        b=TextBlob(sentenced[j])
        print(sentenced[j])
        print(b.sentiment)
        lens_sentenced.append(sentenced[j])
testapi.app(lens_sentenced,j)

print("\n Sentences related to Picture quality \n")
for j in range(i):
     if "high definition" in sentenced[j] or "picture" in sentenced[j]:
        b=TextBlob(sentenced[j])
        print(sentenced[j])
        print(b.sentiment)
        picture_sentenced.append(sentenced[j])
testapi.app(picture_sentenced,j)

print("\n Sentences related to Battery\charger \n")
for j in range(i):
     if "battery" in sentenced[j] or "charge" in sentenced[j]:
        b=TextBlob(sentenced[j])
        print(sentenced[j])
        print(b.sentiment)
        battery_sentenced.append(sentenced[j])
testapi.app(battery_sentenced,j)

print("\n Sentences related to Customer Service \n")
for j in range(i):
     if "customer service" in sentenced[j]:
        b=TextBlob(sentenced[j])
        print(sentenced[j])
        print(b.sentiment)
        customer_review.append(sentenced[j])
testapi.app(customer_review,j)