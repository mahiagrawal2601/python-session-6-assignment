playlist_prices = {'Bollywood Hits': 99, 'Romantic songs': 149, 'Party mix': 199,
                   'Lo-fi beats': 79, 'Workout music': 129}

def update_playlist_price(playlist,new_price):
    playlist_prices[playlist] = new_price

update_playlist_price('Bollywood Hits', 199)

print(playlist_prices)