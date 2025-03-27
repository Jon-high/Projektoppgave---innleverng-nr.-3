# Projektoppgave---innleverng-nr.-3

## Jeg har laget en oppgave basert på de vedlegga som er tilgjengelig i oppgaven. Takk for utfordringen. Håper dere blir fornøyd!

### Filen(support_uke_24.xlsx) må være lagt til i samme mappe for at programmet skal kunne hente inn korrekt informasjon fra tabell . 
### Kjør hele programet for at tilgangen til support_uke_24.xlsx skal laste inn sikkelig. 
### Dette gjøres før man kjører hver enkelt deloppgave-program, dersom det er utfordringer med dette kan utvikler kontaktes.

#### Prosjektoppgaven:

Python - Valgt å løse den ferdigdefinerte oppgaven trenger du i tillegg denne Excel

Det er viktig at Excel filen: suppot_uke_24 blir lastet sikkelig inn i Python programmet og at hele programmet kjøres før man kjører de enkelte del oppgavene. 
Dette gjøres for å sikre at importen av excel-filen går riktig for seg. 
NB: Dersom det skjer en feil med importen av nevnt excel-fil, kan dette stoppe opp funksjonen til del programmene og føre til feil. 


Info om selve oppgaven: 

Prosjekt i PY1010
Prosjektets problemstilling kan bestå av en selvdefinert oppgave, eller du kan arbeide med
en ferdigdefinert oppgave gitt av oss faglærere.
Dersom du velger å jobbe med en selvdefinert oppgave:
Definer gjerne en oppgave med bakgrunn fra din egen jobbsituasjon eller lignende.
Oppgaven er fri, men må inneholde følgende kodetekniske temaer: arrays, vektoriserte
beregninger, if/else-tester, for- eller while-løkke, lese data fra fil, skrive data til fil, plotting,
og egendefinerte funksjoner. Innleveringen skal inneholde:
• En kort beskrivelse av problemet du ønsker å løse
• Kjørbar kode (en py-fil eller JNB-fil som inneholder all kode). All kode skal
dokumenteres med korte informative kommentarer
• Tilleggsfiler, f.eks. filer med data som skal leses inn
• Et viktig moment med innleveringen er at koden du leverer fra deg er grundig testet
og at den er kjørbar for mottaker
Selv om oppgaven er individuell, kan du selvsagt diskutere med kollegaer og søke hjelp fra
våre studentassistenter underveis.
Dersom du velger å løse den ferdigdefinerte oppgaven:
Innleveringen skal inneholde kjørbar kode (en py-fil eller JNB-fil (Jupyter Notebook) hvor alle
deloppgavene besvares i en og samme fil). All kode skal dokumenteres med korte
informative kommentarer. Et viktig moment med innleveringen er at koden du leverer fra
deg er grundig testet og at den er kjørbar for mottaker.
Den ferdigdefinerte oppgaven består av 6 deloppgaver, hvor minst 5 av de 6 deloppgavene
skal besvares. Oppgaven Support dashboard er gitt nedenfor.
Support dashboard.
Du skal her utføre diverse analyser av data som er loggført for supportavdelingen ved
telefonselskapet MORSE. Enhver kundehenvendelse til MORSE blir loggført i en xlsx-fil og du
skal i dette prosjektet jobbe med dataloggen for uke 24. Filen ‘support_uke_24.xlsx’ finner
du sammen med prosjektoppgaven i Canvas under menyen Oppgaver -> Prosjektoppgaven,
og filen er organisert på følgende måte:
Kolonne 1: Ukedag henvendelsen fant sted
Kolonne 2: Klokkeslett kunden tok kontakt med supportavdelingen
Kolonne 3: Samtalens varighet
Kolonne 4: Kundens tilfredshet (skala fra 1-10 hvor 1 indikerer svært misfornøyd og 10
indikerer svært fornøyd).
Merk: kolonne 4 er ikke komplett da mange kunder unnlater å gi tilbakemelding på sin
tilfredshet.
Del a) Skriv et program som leser inn filen ‘support_uke_24.xlsx’ og lagrer data fra kolonne 1
i en array med variablenavn ‘u_dag’, dataen i kolonne 2 lagres i arrayen ‘kl_slett’, data i
kolonne 3 lagres i arrayen ‘varighet’ og dataen i kolonne 4 lagres i arrayen ‘score’. Merk:
filen ‘support_uke_24.xlsx’ må ligge i samme mappe som Python-programmet ditt.
Del b) Skriv et program som finner antall henvendelser for hver de 5 ukedagene. Resultatet
visualiseres ved bruk av et søylediagram (stolpediagram).
Del c) Skriv et program som finner minste og lengste samtaletid som er loggført for uke 24.
Svaret skrives til skjerm med informativ tekst.
Del d) KREVENDE: Skriv et program som regner ut gjennomsnittlig samtaletid basert på alle
henvendelser i uke 24.
Del e) Supportvaktene i MORSE er delt inn i 2-timers bolker: kl 08-10, kl 10-12, kl 12-14 og kl
14-16. Skriv et program som finner det totale antall henvendelser supportavdelingen mottok
for hver av tidsrommene 08-10, 10-12, 12-14 og 14-16 for uke 24. Resultatet visualiseres ved
bruk av et sektordiagram (kakediagram).
Del f) Kundens tilfredshet loggføres som tall fra 1-10 hvor 1 indikerer svært misfornøyd og
10 indikerer svært fornøyd. Disse tilbakemeldingene skal så overføres til NPS-systemet (Net
Promoter Score).
NPS-systemet er konstruert på følgende måte:
Score 1-6 oppfattes som at kunden er negativ (vil trolig ikke anbefale MORSE til andre).
Score 7-8 oppfattes som et nøytralt svar.
Score 9-10 oppfattes som at kunden er positiv (vil trolig anbefale MORSE til andre).
Supportavdelingens NPS beregnes som et tall, prosentandelen positive kunder minus
prosentandelen negative kunder. Ved en formel kan dette gis slik:
NPS = % positive kunder - % negative kunder
Et eksempel på utregning av NPS er gitt i figuren under.
Kilde: https://www.blueprnt.com/2018/09/17/net-promoter-score/
Lag et program som regner ut supportavdelings NPS og skriver svaret til skjerm. Merk:
Kunder som ikke har gitt tilbakemelding på tilfredshet, skal utelates fra utregningene.
