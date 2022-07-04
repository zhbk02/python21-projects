import requests

url = "https://cdn.pocket-lint.com/r/s/970x/assets/images/151442-cameras-feature-stunning-photos-from-the-national-sony-world-photography-awards-2020-image1-evuxphd3mr.jpg"

res = requests.get(url)

name = "photos/photo1.jpg"

with open(name, "wb") as file:
    file.write(res.content)