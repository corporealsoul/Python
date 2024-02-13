import random
import urllib.request

def downlod_image(url):
    image_name = random.randrange(100,500)
    full_image_name = str(image_name)+'.jpg'
    urllib.request.urlretrieve(url,full_image_name)

downlod_image('https://img.freepik.com/premium-photo/selective-focus-red-kite-standing-tree-branch-sunlight-blurred-scene_181624-47318.jpg?size=626&ext=jpg&ga=GA1.1.925871703.1706378270&semt=ais')