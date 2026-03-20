# 🛠️ NOTICE DE MONTAGE - ÉTAPE 3 : Le Wi-Fi (Le téléphone)

*Pour voir les données sur ton téléphone, on va transformer ta carte en un mini-site web accessible depuis le Wi-Fi de la maison.*

## 📡 ACTION 1 : Le Code Wi-Fi
1. Sur ton ordinateur (logiciel Arduino), efface le code précédent.
2. Copie-colle le nouveau code ci-dessous.
3. **⚠️ L'ÉTAPE CRUCIALE :** Tout en haut du code, remplace `"NOM_DE_TA_BOX"` et `"MOT_DE_PASSE_BOX"` par le vrai nom et le mot de passe de ton Wi-Fi. (Garde bien les guillemets autour !).

```cpp
#include <WiFi.h>
#include <WebServer.h>
#include <DHT.h>
#include <OneWire.h>
#include <DallasTemperature.h>

// --- 📡 TES IDENTIFIANTS WI-FI (À MODIFIER !) ---
const char* ssid = "NOM_DE_TA_BOX";
const char* password = "MOT_DE_PASSE_BOX";

// --- 🔌 DÉCLARATION DES CAPTEURS ---
DHT capteurAir(14, DHT22);                     // Le capteur blanc sur le trou 14
OneWire filSondeTerre(4);                      // La sonde en métal sur le trou 4
DallasTemperature sondeTerre(&filSondeTerre);

WebServer serveur(80);

void setup() {
  Serial.begin(115200);
  capteurAir.begin();
  sondeTerre.begin();

  // 1. Connexion au Wi-Fi de la maison
  Serial.println("\n🌱 Allumage du système...");
  Serial.print("Connexion au Wi-Fi ");
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500); 
    Serial.print(".");
  }
  
  // 2. Affichage de l'adresse magique sur l'ordinateur
  Serial.println("");
  Serial.println("✅ Wi-Fi Connecté !");
  Serial.print("📱 Tape cette adresse dans ton navigateur : ");
  Serial.println(WiFi.localIP());

  // 3. Création du Mini-Site Web (Le Tableau de bord)
  serveur.on("/", []() {
    
    // --- LECTURE DES 4 VALEURS ---
    int humiditeTerre = analogRead(34);             // 1. Humidité du sol
    
    sondeTerre.requestTemperatures(); 
    float tempTerre = sondeTerre.getTempCByIndex(0); // 2. Température du sol
    
    float tempAir = capteurAir.readTemperature();    // 3. Température de l'air
    float humiditeAir = capteurAir.readHumidity();   // 4. Humidité de l'air

    // --- FABRICATION DE LA PAGE WEB (Avec un peu de design CSS) ---
    String pageWeb = "<!DOCTYPE html><html><head><meta charset=\"UTF-8\">";
    pageWeb += "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">";
    pageWeb += "<title>Potager OS v1.0</title>";
    // Un peu de style pour faire joli sur le téléphone
    pageWeb += "<style>body{font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif; text-align:center; background-color:#e8f5e9; color:#2e7d32; margin-top:30px;} ";
    pageWeb += ".carte{background:white; padding:20px; border-radius:15px; box-shadow:0 4px 8px rgba(0,0,0,0.1); display:inline-block; margin:15px; width:280px; text-align:left;} ";
    pageWeb += "h1{color:#1b5e20;} h2{border-bottom:2px solid #a5d6a7; padding-bottom:5px; margin-top:0;} </style>";
    pageWeb += "</head><body>";
    
    pageWeb += "<h1>🍅 Potager OS v1.0 ☀️</h1>";
    
    // Bloc 1 : La Terre
    pageWeb += "<div class=\"carte\"><h2>🌱 Dans la Terre</h2>";
    pageWeb += "<p>💧 Humidité (brute) : <b>" + String(humiditeTerre) + "</b></p>";
    pageWeb += "<p>🌡️ Température : <b>" + String(tempTerre) + " &deg;C</b></p></div>";
    
    // Bloc 2 : L'Air
    pageWeb += "<div class=\"carte\"><h2>☁️ Dans l'Air</h2>";
    pageWeb += "<p>🌡️ Température : <b>" + String(tempAir) + " &deg;C</b></p>";
    pageWeb += "<p>💧 Humidité : <b>" + String(humiditeAir) + " %</b></p></div>";
    
    pageWeb += "</body></html>";
    
    // On envoie la page au téléphone
    serveur.send(200, "text/html", pageWeb);
  });

  // On lance le serveur web
  serveur.begin();
}

void loop() {
  // La carte écoute en permanence si un téléphone demande à voir la page
  serveur.handleClient(); 
}
```

## 📱 ACTION 2 : L'Affichage sur le Canapé
1. Clique sur le bouton **Téléverser** (la flèche vers la droite) pour envoyer ce nouveau code dans la carte.
2. Ouvre la **Loupe** (Moniteur Série) en haut à droite.
3. Attends quelques secondes. L'ordinateur va afficher un message du type : `✅ Connecté ! Tape cette adresse dans ton téléphone : 192.168.1.XX`
4. **Prends ton smartphone** (assure-toi qu'il est connecté au même Wi-Fi que la maison).
5. Ouvre ton navigateur Internet (Safari, Chrome...) et tape exactement les 4 nombres séparés par des points dans la barre d'adresse tout en haut.
6. **Magie !** Une page blanche apparaît avec le titre "Potager OS v1.0" et tes relevés en direct !
