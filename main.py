'''from pytube import YouTube

# creating YouTube object
yt = YouTube("https://www.youtube.com/watch?v=YkgrywnkLRU&t=4s")

# accessing audio streams of YouTube obj.(first one, more available)
stream = yt.streams.filter(only_audio=True).first()
# downloading a video would be: stream = yt.streams.first()

# download into working directory
stream.download()'''



  


from multiprocessing.dummy import Pool as ThreadPool
from tqdm import tqdm
import pikepdf
import time


pwd = list(range(0,99999))
loop = tqdm(total=len(pwd), position=0,leave=False)


def test (senha):
    try:
        pikepdf.Pdf.open('Fatura Claro.pdf', password=str(senha).zfill(5))
        print('Senha: ' + str(senha).zfill(5))
        print('Tempo: ' + str(time.time() - start))
        
        exit()
    except:
        loop.update(1)
        pass
    
    
start = time.time()
pool = ThreadPool(6)
result = pool.map(test,pwd)

pool.close()
pool.join()
