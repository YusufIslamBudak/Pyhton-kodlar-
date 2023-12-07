from gtts import gTTS
tts = gTTS(text="Gedik Üniversitesi İleri Programlama Dersi. Doktora Öğretim Üyesi Hikmet CANLI", lang='tr')
tts.save("audio1.mp3")