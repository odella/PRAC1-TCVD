# PRAC1-TCVD

Programa per a extreure totes les ofertes existents en el moment d'utilització de la pàgina https://www.capraboacasa.com

Per a poder executar-se es necessari tenir les següents llibreries disponibles:

requests
BeautifulSoup
numpy
pandas
datetime

No cal incloure cap parametre, el programa descarrega automaticament les dades i les enmagatzema en un arxiu amb el seguent nom:

ofertesCaprabo_dia.csv
 
Essent dia el dia actual.

Utilitzar el programa en dies diferents retorna ofertes diferents.

Actualment exteu els següents punts d'informació de cada producte:

- Nom
- ID
- Preu
- Ofertes o promocions
- Dia
