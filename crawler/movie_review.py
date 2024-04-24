import requests
from lxml import etree
import parsel
import csv
import re
import time as t

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Cookie' : 'bid=jRrJ4GZ1pfY; _pk_id.100001.4cf6=48a1331be8322404.1713623669.; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __utma=30149280.392054908.1713623670.1713623670.1713623670.1; __utmc=30149280; __utmz=30149280.1713623670.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.231643814.1713623670.1713623670.1713623670.1; __utmb=223695111.0.10.1713623670; __utmc=223695111; __utmz=223695111.1713623670.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __gads=ID=d3a2c4bf7e90ebe3:T=1713623673:RT=1713623673:S=ALNI_MZjwWfSQsAMDelBtY5EU6ghe-KHWA; __gpi=UID=00000de50870f7bb:T=1713623673:RT=1713623673:S=ALNI_MZh9XA-c_svEd6-RdVypnon7GFBBA; __eoi=ID=b622308785fd9187:T=1713623673:RT=1713623673:S=AA-AfjZEUKBYY9RHIcPBTok4oFf3; ll="118282"; _vwo_uuid_v2=DB853DE0C9E2302BF81133F566EC7D2BD|13bf265f4576e9e538d5f79662f1e940; __utmb=30149280.4.9.1713623735317; FCNEC=%5B%5B%22AKsRol8_AOnOvjGIS4ME6FtLpW8p36JViTwIJy4aQwmNSCfywFWoIdeqOXRi0xqPm_SKojTIQPzDLWYjeypMvpCf7lYtp8RacIpbgLj3JCxAWAksMtiU71_1nTI1pJfUBjAR2Im3ZNQ1Xwxvca3_dyqSMvkSCIxUGA%3D%3D%22%5D%5D'
}
comments_dict = {}
page = 0

while True:
    url = f'https://movie.douban.com/subject/35633650/comments?start={page}&limit=20&sort=new_score&status=P'
    print(url)
    res = requests.get(url=url, headers=headers).text
    selector = parsel.Selector(res)
    comment_list = selector.css('.comment-item')
    if len(comment_list) == 0:
        break
    for i, comment in enumerate(comment_list):
        index = i + page
        comments_dict[index] = {
            'name' : '',
            'content' : '',
            'stars' : 0,
            'upvote' : 0,
            'time' : 0,
            'location' : ''
                            }
        name = comment.css('.comment-info a::text').get().strip()
        content = comment.css('.comment-content span::text').get().strip()
        upvote = comment.css('.votes::text').get()
        time = comment.css('.comment-time').attrib['title'].split(' ')[0]
        location = comment.css('.comment-location::text').get()
        
        
        class_attribute = comment.css('.rating').attrib['class']
        stars = re.search(r'\d+', class_attribute).group()[0]

        comments_dict[index]['name'] = name
        comments_dict[index]['content'] = content
        comments_dict[index]['stars'] = stars
        comments_dict[index]['upvote'] = upvote
        comments_dict[index]['time'] = time
        comments_dict[index]['location'] = location

    page += 20
    t.sleep(100)

print("====================================")
print(len(comments_dict))
    
    