#Problem C: 54 Years of Historical Distortion
import random 

movie_list = [
    'Alaala: A Martial Law Special (2017) - youtube.com/watch?v=ULUgKp7EbYg',
    'Ang Pasiong Mahal ni Beverly Apostol (2017) - cinemata.org/view?m=IIJ1pHICD',
    'Arrogance of Power (1983) - cinemata.org/view?m=OODYtm9W4',
    'Bakit Dilaw ang Gitna ng Bahaghari? (1994) - youtube.com/watch?v=TrpVynO420c',
    'Batas Militar (1997) - vimeo.com/314920652',
    "Betamax '83 (2020) - facebook.com/ActiveVista/videos/630523444278320/",
    "Coup d'Etat: The Philippines Revolt (1986) - youtube.com/watch?v=BWQHSJJ8OYE",
    'Daluyong (1984) - cinemata.org/view?m=0mjk7nzoV',
    'Edjop (1986) - cinemata.org/view?m=fhm0KLINd',
    'Imelda (2003) - youtube.com/watch?v=rBS7A_-bnwA',
    'In Search of the Marcos Millions (1987) - youtube.com/watch?v=PEofQrkoOak',
    'Liway (2018) - youtube.com/watch?v=jVzF8xqctco',
    'Marcos: A Malignant Spirit (1986) - youtube.com/watch?v=4iF0k4VRPyo',
    'No Time for Crying (1986) - cinemata.org/view?m=tVJCudKQd',
    'Portraits of Mosquito Press (2015) - facebook.com/watch/?v=656141078485057',
    'Remembering Martial Law in Escalante (2015) - cinemata.org/view?m=pDxEByiBk',
    'Sabangan (1983) - cinemata.org/view?m=MmBx6sKj7',
    'Signos (1983) - vimeo.com/304516355',
    'The Imelda Tapes (2022) - youtube.com/watch?v=y9qkOLcpWJ4',
    'The Kingmaker (2019) - youtube.com/watch?v=5gNujHs-Gho'
]

movies = int(input('How many movies to retrieve? '))

def HoldAccountable(number):
    number = min(number, len(movie_list))  
    chosen_movie = random.sample(movie_list, number)
    chosen_movie.sort()

    if number == 1:
        print(chosen_movie[-1])
    else:
        for movie in chosen_movie[:-1]:
            print(movie)
    print(f"and {chosen_movie[-1]}")