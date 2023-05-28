import tweepy
import wget

# Defina suas chaves de API do Twitter
consumer_key = 'SUA_CONSUMER_KEY'
consumer_secret = 'SUA_CONSUMER_SECRET'
access_token = 'SEU_ACCESS_TOKEN'
access_token_secret = 'SEU_ACCESS_TOKEN_SECRET'

# Autenticação com a API do Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# ID do tweet que contém o vídeo desejado
tweet_id = 'ID_DO_TWEET'

# Obter informações sobre o tweet
tweet = api.get_status(tweet_id, tweet_mode='extended')

# Procurar o URL do vídeo no tweet
video_url = None
if 'media' in tweet.entities:
    for media in tweet.extended_entities['media']:
        if media['type'] == 'video':
            video_info = media['video_info']
            variants = video_info['variants']
            # Escolha a variante com maior bitrate como o vídeo de melhor qualidade
            variant = max(variants, key=lambda x: x['bitrate'])
            video_url = variant['url']
            break

# Baixar o vídeo
if video_url:
    print('Baixando vídeo...')
    wget.download(video_url, 'video.mp4')
    print('Vídeo baixado com sucesso!')
else:
    print('Nenhum vídeo encontrado neste tweet.')
