# Nettside for Akademiets skolekantine

**Laget av:** [Andreas], [2IM]

Nettsiden viser ukens meny og kantinas faste varer, og har kontaktinformasjon til kantina.
Den er laget med Flask (Python), HTML/Jinja2 og CSS. Alle sidene arver fra en felles
grunnmal (`base.html`) med navigasjonsmeny og footer.



### Hva brukerne kan gjøre på nettsiden

- **Hjem (`/`):** se navnet på kantina og en kort beskrivelse av hva nettsiden tilbyr, og navigere videre til de andre sidene
- **Meny (`/meny`):** se ukens meny fra mandag til fredag, med rett, kort beskrivelse, bilde og pris for hver dag
- **Varer (`/varer`):** se de faste varene (drikke, bakst og snacks), delt inn i kategorier, med navn, pris og bilde
- **Kontakt (`/kontakt`):** finne telefonnummer, e-post, adresse og åpningstider

### Viktigste funksjoner i koden

- Flask-ruter med `render_template()` for hver side
- Data om menyen og varene ligger i `data.py` (lister med ordbøker), importeres i `app.py` og sendes til HTML-filene
- Arv: alle sidene bruker `{% extends "base.html" %}`, og `base.html` inneholder navigasjon og felles footer
- For-løkker i Jinja for å vise menyen og varene
- Layout med Flexbox og CSS Grid


## Litteratur- og kildeliste
- [Claude](https://claude.ai) (KI-assistent fra Anthropic): se under

### Bruk av KI

Jeg har brukt Claude som hjelp i prosjektet. Delene under er laget med hjelp av KI, og er også merket med kommentarer i koden:

- Feilsøking av feilmeldinger i Flask og Jinja 
- CSS for kortene på Hjemsiden, og senere brukt det for å style kortene på meny og varesidene.
- Noe HTML for kontaktsiden
- Data settene på data.py
