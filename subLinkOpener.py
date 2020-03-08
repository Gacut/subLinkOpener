#! python3

import webbrowser
from requests_html import HTMLSession


print('''

                                 
		 _____     _   __    _     _     
		|   __|_ _| |_|  |  |_|___| |_   
		|__   | | | . |  |__| |   | '_|  
		|_____|___|___|_____|_|_|_|_,_|  
		                                 
		                                 
		   _____                         
		  |     |___ ___ ___ ___ ___     
		  |  |  | . | -_|   | -_|  _|    
		  |_____|  _|___|_|_|___|_|      
		        |_|                      
		        	Made by Gacut
		        	Ascii text: http://patorjk.com
	''')

# skrypt, który otwiera stronę podaną przez użytkownika w postaci'google.pl'.


def OtwierajStrone(link):
    webbrowser.get('windows-default').open('https://' + link)

# Skrypt, który otwiera wszystkie podstrony
# na podanej przez użytkownika stronie.


def OtwLink(strona):
    session = HTMLSession()
    r = session.get('https://' + strona)
    r.html.absolute_links
    ls = r.html.absolute_links
    ls2 = list(ls)
    ls3 = len(ls2)
    print('Podstron na podanym adresie: ' + str(ls3))
    print('Czy otworzyć stronę? t/n')
    odp = input().lower()
    if odp == 't':
        OtwierajStrone(s)
    elif odp == 'n':
        print('Ok')
    else:
        print('Błąd, włącz program jeszcze raz i podaj poprawną wartość.')
    print('Czy otworzyć podstrony? UWAGA! MOŻE ZAWIESIĆ KOMPUTER!')
    odp2 = input().lower()
    if odp2 == 't':
        for i in range(ls3):
            webbrowser.open(ls2[i])
    if odp2 == 'n':
        print('Ok')
    else:
        print('Błąd, włącz program jeszcze raz i podaj poprawną wartość.')
print('Podaj adres strony, która ma być otwarta')
s = input()
# pobiera stronę z wartości 's' i uruchamia skrypt
if s:
    OtwLink(s)
# Jeżeli użytkownik nie poda żadnej wartości, zostanie poproszony
# o podanie poprawnej nazwy strony
else:
    print('podaj poprawną nazwe strony')
