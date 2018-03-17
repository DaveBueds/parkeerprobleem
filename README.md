# Parkeerprobleem

<h1>Main</h1>
<p>Hier start het cambio algoritme. Eerst wordt een csv ingelezen en initiele opl berekend. Vervolgens schrijft het de oplossing weg naar
een andere csv file</p>

<h1>CSV_read</h1>
  <p>Opgelet: bij het inlezen is alle data van het type str</p>
  <ul>
    <li>Leest de csv file in</li>
    <li>Zet alle csv data om in objecten</li>
    <li>Returned een object met de requestlijst, zonelijst, vehiclelijst en het aantal dagen</li>
  </ul>

<h1>initOplossing</h1>
  <ul>
    <li>Soorteert de request lijst op basis van starttijd</li>
    <li>Controleert eerst of de request wel een wagenlijst heeft</li>
    <li>Vervolgens loopt het over de lijst van de wagenlijst en controleert of het voertuig beschikbaar is</li>
    <li>Er wordt rekening gehouden met voertuigen die gereserveerd worden voor een bepaald tijdslot</li>
    <li>Returned of een request een voertuig krijgt toegewezen</li>
  </ul>


<h1>CSV_write</h1>
<ul>
  <li>Schrijft de oplossing gevonden door het algoritme weg in een csv file</li>
</ul>


<h1>Request</h1>
<ul>
  <li>Klasse file voor request</li>
</ul>


<h1>Vehicle</h1>
<ul>
  <li>Klasse file voor vehicle</li>
</ul>


<h1>Zone</h1>
<ul>
  <li>Klasse file voor zone</li>
</ul>
