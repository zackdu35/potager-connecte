# 🛠️ NOTICE DE MONTAGE - ÉTAPE 2 : L'Ordinateur (La Magie)

⚠️ **RÈGLE D'OR :** L'ordinateur va parfois afficher des lignes de texte orange ou rouge pendant qu'il travaille. Pas de panique, c'est normal, il ne va pas exploser ! Laisse-le finir.

### 📦 INVENTAIRE DES PIÈCES POUR CETTE ÉTAPE :
* **[Le Puzzle]** : Le montage que tu viens de terminer avec succès à l'Étape 1.
  ![Le Puzzle](../assets/81aehZAwfAL._SL1500_.jpg)
* **[Le Câble]** : Un câble USB adapté à ta carte noire (Micro-USB ou USB-C, attention à bien prendre un câble qui fait "Transfert de données" et pas juste "Chargeur de téléphone").
  ![Le Câble](../assets/61XbB38i7YL._AC_SL1105_.jpg)
* **[L'Ordi]** : Ton ordinateur allumé.

---

## 🔌 ACTION 1 : Le Branchement
1. Prends **[Le Câble]** USB.
2. Branche le petit bout dans la prise de la carte noire **[Cerveau]**.
3. Branche le gros bout dans un port USB de ton **[Ordi]**.
4. *Bip !* Une petite lumière devrait s'allumer sur la carte noire. C'est en vie !

## 📚 ACTION 2 : Acheter les Dictionnaires (Les Bibliothèques)
*La carte noire parle "Électronique", ton ordi parle "Français". Il nous faut des traducteurs.*

1. Ouvre ton logiciel **Arduino IDE** sur l'ordinateur.
2. Va dans le menu tout en haut : Clique sur **Croquis** > **Inclure une bibliothèque** > **Gérer les bibliothèques**.
3. Une fenêtre de recherche s'ouvre. 
4. Tape `DHT sensor library` dans la barre de recherche. Trouve celle qui est faite par "Adafruit" et clique sur **Installer**.
5. Efface ta recherche et tape `OneWire`. Trouve celle de "Paul Stoffregen" et clique sur **Installer**.
6. Efface encore et tape `DallasTemperature`. Trouve celle de "Miles Burton" et clique sur **Installer**.
*(Ferme la fenêtre de recherche, on a tous nos dictionnaires !)*

## 📝 ACTION 3 : Le Texte Magique (Le Code)
1. Sur la grande page blanche de ton logiciel Arduino, efface tout le texte qui s'y trouve déjà. La page doit être 100% vide.
2. Copie ce bloc de texte gris juste en dessous, et colle-le sur ta page blanche :

```cpp
#include <DHT.h>
#include <OneWire.h>
#include <DallasTemperature.h>

DHT capteurAir(14, DHT22);
OneWire filSondeTerre(4);
DallasTemperature sondeTerre(&filSondeTerre);

void setup() {
  Serial.begin(115200);
  capteurAir.begin();
  sondeTerre.begin();
  Serial.println("Bonjour ! La station meteo demarre...");
}

void loop() {
  int humiditeTerre = analogRead(34);
  sondeTerre.requestTemperatures(); 
  float temperatureTerre = sondeTerre.getTempCByIndex(0);
  float temperatureAir = capteurAir.readTemperature();

  Serial.println("--- NOUVELLE MESURE ---");
  Serial.print("Terre (Humidite brute) : "); Serial.println(humiditeTerre);
  Serial.print("Terre (Temperature) : "); Serial.print(temperatureTerre); Serial.println(" C");
  Serial.print("Air (Temperature) : "); Serial.print(temperatureAir); Serial.println(" C");
  
  delay(5000); 
}
```

## 🎯 ACTION 4 : Cibler la carte (L'Étape Critique)
*Il faut dire à l'ordinateur à qui il doit envoyer ce texte.*
1. Va dans le menu **Outils** > **Carte**. Cherche et sélectionne **ESP32 Dev Module** (ou un nom qui ressemble à ta carte TTGO/ESP32).
2. Va dans le menu **Outils** > **Port**. Clique sur le port qui s'affiche (ça s'appelle souvent "COM3", "COM4" ou "USB Serial"). S'il y en a plusieurs, essaie le dernier de la liste.

## 🚀 ACTION 5 : L'Envoi (Le Téléversement)
1. En haut à gauche du logiciel, il y a un bouton rond avec une **Flèche vers la droite (➔)**. C'est le bouton "Téléverser".
2. Clique dessus.
3. ⏳ **PATIENTE.** En bas de l'écran, une barre verte va se remplir. L'ordinateur va écrire plein de choses. Attends de lire le message "Téléversement terminé".

## 🔎 ACTION 6 : La Récompense !
1. En haut à droite du logiciel, clique sur l'icône en forme de **Loupe** (Le Moniteur Série).
2. Une nouvelle fenêtre s'ouvre. En bas à droite de cette fenêtre, vérifie que le menu déroulant est bien réglé sur **115200 baud**.
3. Regarde l'écran : **La carte te dit Bonjour et t'affiche la température de la pièce en direct toutes les 5 secondes !**

---

**✅ FIN DE L'ÉTAPE 2 !**
Félicitations, tu viens de programmer ta première carte électronique. La station météo est fonctionnelle !