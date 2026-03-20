# 🍅 Potager Connecté (Gardening OS)

Bienvenue dans le dépôt du **Potager Connecté**. Ce projet est une station météo intelligente conçue pour surveiller la santé de vos plantes en temps réel.

## 🌟 Fonctionnalités
- **Surveillance 4-en-1** : Température de l'air, Humidité de l'air, Température du sol, et Humidité du sol.
- **Interface Web Locale** : Visualisez vos données en direct sur votre smartphone via Wi-Fi.
- **Écran Intégré** : Suivi immédiat sur l'écran OLED embarqué.
- **Autonome** : Alimenté par batterie et panneau solaire pour une installation extérieure IP65.

## 🛠️ Matériel (Hardware)
- **Cerveau** : ESP32 Dev Module (LILYGO TTGO avec écran OLED).
- **Capteurs** :
  - DHT22 (Air)
  - DS18B20 Inox (Terre - Température)
  - Capacitive Soil Moisture Sensor v1.2 (Terre - Humidité)
- **Énergie** : Batterie Li-ion 3.7V + Panneau Solaire 6W.

## 📂 Structure du projet
- `/site-notice` : Le guide de montage interactif (HTML/CSS).
- `/notice` : Les fichiers sources du guide au format Markdown.
- `/assets` : Images et schémas du projet.
- `product-list.md` : Liste détaillée des composants avec liens d'achat.

## 🚀 Installation & Montage
1. Consultez le guide interactif dans `/site-notice/index.html`.
2. Suivez les 4 phases :
   - **Phase 1** : Montage sur plaque d'essai.
   - **Phase 2** : Programmation via Arduino IDE.
   - **Phase 3** : Configuration Wi-Fi.
   - **Phase 4** : Mise en boîte étanche.

## 👨‍💻 Créé pour Papa
Ce projet a été conçu avec ❤️ comme cadeau pour faciliter le jardinage et l'apprentissage de l'électronique.

---
*Propulsé par Gardening OS v1.0.4*
