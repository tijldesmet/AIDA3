# 🧠 AIDA3 – AI Document Assistent / Document AI Assistant

> 🇳🇱 Dit project is beëindigd. Gebruik is op **eigen risico**. Geen aansprakelijkheid of ondersteuning.
> 🇬🇧 This project is discontinued. Use at **your own risk**. No liability or support.

---

## 📌 Over het project / About this project

**AIDA3 is een AI-gebaseerde assistent die documenten analyseert met behulp van GPT-4.** Je kan vragen stellen over documenten in een Google Drive-map of een lokale map met submappen. De AI zoekt het antwoord en toont relevante bronnen.

> ⚠️ Dit project is **afgesloten**. Alle rechten zijn voorbehouden. Eerlijk gebruik is toegestaan, maar **zonder enige aansprakelijkheid of ondersteuning**.

This is a **finished project**. All rights reserved. Fair use is allowed, but **without any warranty or support**.

---

## 📚 Wat doet AIDA3? / What does AIDA3 do?

* 🔍 Leest **PDF, DOCX, RTF, PPT(X), XLS(X)** en afbeeldingsbestanden (OCR)
* 📂 Werkt met **lokale mappen** (met submappen) of **Google Drive mappen** (via ID)
* 🧠 Beantwoordt vragen over de inhoud van meerdere documenten tegelijk
* 🌐 Gebruikt OpenAI GPT-4 en Tesseract OCR (multitaal: NL/FR/EN/DE/...)
* 🧾 Bronnen worden weergegeven bij elk antwoord

---

## 💡 Voor wie is dit? / Who is it for?

**Niveau:** Beginnende tot gemiddelde gebruiker

### 🧠 Vereiste kennis / Required Skills

* Basiskennis Python en terminal/powershellgebruik
* Weten hoe je bestanden kopieert/plaatst
* Een API sleutel en credentials kunnen invullen

### 🖥️ Hardware vereisten / Hardware Requirements

* Minstens 4 GB RAM (8 GB aanbevolen)
* 1 GB vrije schijfruimte
* Rechten om als administrator taken uit te voeren

### 🧰 Software vereisten / Software Requirements

* Python 3.10+ met `venv` en `pip`
* Git
* Chrome, Edge of Firefox browser

---

## 🔐 OpenAI API Key instellen / Set your OpenAI API key

1. Ga naar [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
2. Log in en klik op "Create new secret key"
3. Kopieer de sleutel
4. Hernoem `.env_default` naar `.env`
5. Plaats hierin:

```env
OPENAI_API_KEY=sk-...
```

> Let op: deze sleutel is **niet gratis**. Kosten worden gefactureerd per gebruik.

---

## ☁️ Google Drive: Folder-ID en OAuth instellen

### 📂 Hoe vind je een Google Drive folder-ID?

1. Open je map in Google Drive
2. URL ziet er zo uit: `https://drive.google.com/drive/folders/1A2B3CXYZ...`
3. Kopieer het stuk ná `folders/` – dat is je folder-ID

### 🧾 Google OAuth2 credentials.json verkrijgen:

1. Ga naar [Google Cloud Console](https://console.cloud.google.com/)
2. Maak een nieuw project aan
3. Ga naar **APIs & Services > OAuth consent screen**

   * Kies `External`
   * Vul naam, e-mail en scope in (Drive API)
4. Ga naar **Credentials > Create Credentials > OAuth 2.0 Client ID**

   * Type: Desktop app
   * Download het JSON bestand
5. Hernoem dit naar `credentials.json` en plaats in hoofdmap van AIDA3

> 📁 Zorg dat je Drive-map gedeeld is met **'Bewerker' rechten** voor het gebruikte account.

---

## 🧪 Ondersteunde bestandsformaten

| Type         | Ondersteund |
| ------------ | ----------- |
| PDF          | ✅           |
| DOCX         | ✅           |
| RTF          | ✅           |
| PPT(X)       | ✅           |
| XLS(X)       | ✅           |
| PNG/JPG/TIFF | ✅ (OCR)     |

---

## 🧪 Installatie (Linux)

```Terminal
cd /home/$USER/
sudo apt update && sudo apt install git -y
git clone https://github.com/tijldesmet/AIDA3.git
cd AIDA3
python3 -m venv ai-env
source ai-env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

bash -c "python3 main.py & sleep 5 && xdg-open http://127.0.0.1:7860"
```

### Starten:

```Terminal
bash -c "cd /home/$USER/AIDA3 && source ai-env/bin/activate && python3 main.py & sleep 5 && xdg-open http://127.0.0.1:7860"
```

---

## 🧪 Installatie (Windows)

```powershell
# Zorg ervoor dat je dit uitvoert als Administrator

# Navigate to Program Files and clone the repo
cd "C:\Program Files"
git clone https://github.com/tijldesmet/AIDA3.git
cd "AIDA3"

# Create virtual environment
python -m venv ai-env & "ai-env\Scripts\Activate.ps1"

# Install requirements
pip install --upgrade pip && pip install -r requirements.txt

# Start the main app
Start-Process powershell -ArgumentList "python main.py" -NoNewWindow

# Wait a few seconds before launching browser
Start-Sleep -Seconds 5

# Open in default browser
Start-Process "http://127.0.0.1:7860"

```

### Starten:

```powershell
# Zorg ervoor dat je dit uitvoert als Administrator

# Ga naar de juiste directory
Set-Location "C:\Program Files\AIDA3"

# Maak virtuele omgeving aan
python -m venv ai-env & "ai-env\Scripts\Activate.ps1"

# Start AIDA3
Start-Process powershell -ArgumentList "-NoExit", "-Command", "python main.py"

# Wacht 5 seconden zodat server kan starten
Start-Sleep -Seconds 5

# Open standaardbrowser met Gradio-interface
Start-Process "http://127.0.0.1:7860"


```

---

## 🧹 Verwijderen / Uninstall

### Linux

```bash
rm -rf /home/$USER/AIDA3
```

### Windows

```powershell
rmdir /s /q "C:\Program Files\AIDA3"
```

---

## 🧯 Troubleshooting

| Probleem                     | Oplossing                                                                         |
| ---------------------------- | --------------------------------------------------------------------------------- |
| `ModuleNotFoundError`        | Zorg dat je virtuele omgeving geactiveerd is en alle vereisten geïnstalleerd zijn |
| `Invalid Google credentials` | Controleer je `credentials.json` bestand en OAuth rechten                         |
| Geen antwoord van de AI      | Controleer of je internet hebt en of je OpenAI-tegoed op is                       |
| App start niet               | Herstart je systeem of probeer met `python main.py` in terminal                   |

---

## 💬 Tips voor gebruik

* 📌 Voeg een `.desktop` bestand toe in `~/Bureaublad` om snel te starten
* 📁 Gebruik duidelijke documentnamen – dit helpt bij het begrijpen van context
* 🌍 OCR ondersteunt meerdere talen tegelijk (NL, FR, DE, EN...)
* 🛠️ Je kan eigen scripts toevoegen in `backend/` om extra functionaliteit in te bouwen

---

## 🤖 Over de AI

Deze applicatie maakt gebruik van:

* OpenAI GPT-4
* LangChain voor chaining en vectoropslag (FAISS)
* Gradio voor de gebruikersinterface
* PyTesseract voor OCR van afbeeldingen

De code is deels gegenereerd door AI-modellen (zoals ChatGPT).

---

## 📜 Licentie / Disclaimer

> 🇳🇱 Dit project is beëindigd. Gebruik is op **eigen risico**. De ontwikkelaar is **niet verantwoordelijk** voor schade of fouten. Gebruik is **toegestaan** voor persoonlijke, educatieve en eerlijke toepassingen.

> 🇬🇧 This project is discontinued. Use at **your own risk**. The developer is **not liable** for any issues. Use is **permitted** for personal, educational, and fair-use scenarios.
