# 🍅 Projet Potager OS v1.0 — Édition Solaire ☀️

**Joyeux Cadeau Papa !**

Puisque tu aimes avoir les mains dans la terre et la tête dans le code, on a décidé de fusionner tes deux passions. Fini le jardinage à l'aveugle ou "au doigt mouillé" : voici la version **Hardware & Open Source** de ton potager !

Ta mission, si tu l'acceptes : assembler et coder cette station météo 100% autonome et résistante aux intempéries.

---

## 🛠️ Ton Kit de Développement (Le Hardware)

Voici les composants que nous avons sélectionnés pour ton laboratoire de recherche agricole :

* **Le Cerveau (ESP32 + OLED) :** Une carte **TECNOULAB** avec écran intégré de 0,96 pouce. Elle gère le Wi-Fi, le Bluetooth et possède son propre support de batterie au dos.
* **L'Énergie Solaire (NIVIAN 6W) :** Un panneau solaire haute performance conçu pour l'extérieur. Grâce à son connecteur USB, il recharge la batterie en direct pour une autonomie totale.
* **Le Cœur (Piles JESSPOW 18650) :** Deux accus Lithium de 3000 mAh à "Haut Plat" (Flat Top) spécialement choisis pour s'insérer parfaitement au dos de ta carte.
* **Les Capteurs de Terre :**
    * **Modules Capacitifs (AZ-Delivery) :** Tes détecteurs de soif. Ils mesurent l'humidité du sol sans jamais s'oxyder.
    * **Sondes Inox (DS18B20) :** Des capteurs étanches avec 1 m de câble pour surveiller la température profonde du sol.
* **Le Capteur Air (DHT22) :** Pour surveiller le climat ambiant (Température & Humidité) avec une haute précision.
* **Le Châssis (Boîtier IP65) :** Une grande boîte de dérivation étanche de 20 cm avec **couvercle transparent**. Idéal pour protéger l'électronique tout en gardant l'écran OLED visible.
* **Le Système Nerveux :** Un kit complet de **Breadboards HUAREW** et de câbles Dupont pour tout relier sans aucune soudure.

---

## 💻 Ta Mission (Le Software)

On fournit le matériel, mais c'est toi l'informaticien ! Ton défi :

1.  **Le Montage "Sans Soudure" :** Utilise les plaques d'essai et les fils fournis pour créer ton circuit.
2.  **L'Optimisation Solaire :** Le système fonctionnant sur batterie, tu vas devoir dompter le mode *Deep Sleep*. La carte doit se réveiller, scanner le potager, envoyer les datas, et se rendormir immédiatement.
3.  **L'Interface :** À toi de décider si tu préfères lire les données sur l'écran OLED ou créer ton propre dashboard sur mobile via ton réseau local.

---

## 🧪 Prêt pour le déploiement ?

On a hâte de voir les premières courbes de température et d'humidité s'afficher sur ton écran. Bon développement dans ton nouveau laboratoire à ciel ouvert !

**Amuse-toi bien !**
*Ton équipe de développement (Tes enfants)*