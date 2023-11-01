import gdown
url = 'https://docs.google.com/document/d/1XQFo3Wb6WiQAXPqN86ISt2-gqMSDNp0y/edit?usp=sharing&ouid=118008663280403480434&rtpof=true&sd=true'
url = url.split('/')
url = f'{url[0]}//{url[2]}/uc?id={url[5]}'

gdown.download(url, quiet=False)