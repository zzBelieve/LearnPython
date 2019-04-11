import requests
import os
import simplejson as json
os.makedirs('./images/', exist_ok=True)
os.makedirs('./media/', exist_ok=True)
def download():

    BaseUrl = "http://lagged.com/api/play/two-sides3/"
    response = requests.get(BaseUrl +"data.js")
    print(type(response))
    json_response = response.content.decode()
    # print(type(json_response))
    dict_json = json.loads(json_response, strict=False)
    print(type(dict_json["project"][3]))
    #
    laggedImageList = dict_json["project"][3];

    print(laggedImageList)
    laggedMp3List = dict_json["project"][7];

    print(laggedMp3List)

    for musicObject in laggedMp3List:
        a = musicObject[0]
        musicUrl = BaseUrl + a
        print(musicUrl)
        downloadMusic(musicUrl)



    for imageObject in laggedImageList:
        # print(type(imageObject[7]));
        a = imageObject[7]

        # print(isinstance(a, (list)))
        if(isinstance(a, (list))):
         imageName = a[0][7][0][0];

         imageUrl = BaseUrl + imageName

         print(imageUrl)

         downloadImage(imageUrl)
         #print(a[0][7][0][0]);
         #print("========");
        # a =  imageObject[7]
        # imageObject[0][7]

    # images = json.loads(dict_json["project"][3])
    # print(images)
    #
    # items = dict_json['items']
    #
    #
    # for obj in items:
    #     print(obj['url'])
    #     r = requests.get(obj["url"], stream=True)
    #     with open('./ani/' + obj['title'] + '.mp4', 'wb') as f:
    #         for chunk in r.iter_content(chunk_size=1024):
    #             f.write(chunk)


def downloadImage(imageUrl):

    print(imageUrl)
    imageL = imageUrl.split("/")[-1]
    r = requests.get(imageUrl, stream=True)
    with open('./images/' + imageL, 'wb') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)

def downloadMusic(musicUrl):

    print(musicUrl)
    musicL = musicUrl.split("/")[-1]
    r = requests.get(musicUrl, stream=True)
    with open('./media/' + musicL, 'wb') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)

if __name__ == '__main__':

    download()