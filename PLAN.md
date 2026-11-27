# Instagram-Plan @pascals.solutions

## Positionierung
- Name: «Pascal | Finanzen, Fitness & Papa-Leben 🇨🇭»
- Bio: Papa & CEO @moonshine.solutions 🇨🇭 / 🤝 500+ Menschen finanziell begleitet (von Pascal bestätigt) / 💪 Geld, Gesundheit & Familie – ehrlich erklärt / 👇 Alles von mir
- Link: https://moonshine-solutions.com/links?utm_source=ig&utm_medium=social&utm_content=link_in_bio
- Versprechen: Papa aus der Schweiz teilt, was bei Geld, Gesundheit und Familie wirklich hilft. Jeder Beitrag hat eine Erkenntnis.

## Säulen
35 % Geld verständlich · 20 % Gesundheit & Training · 20 % Papa- & Unternehmer-Leben · 25 % KI im Alltag (ab KW 51 auf Pascals Wunsch gestärkt: praktische KI-Hilfe, konkrete Prompts. KI ist nicht das Hauptthema, kommt aber öfter vor, gern auch als Werkzeug innerhalb von Geld-, Gesundheits- und Familien-Beiträgen)
Serien: «Ausreden-Übersetzer», «Was die Bank dir nicht erklärt» (Fortsetzung des 428k-Reels vom 31.3.2025), «Gym × Geld», «Was ich mit 31 weiss», «Tagsüber Papa, abends Entwickler».

## Regeln
- Teilen-Aufruf («Schick das jemandem, der …») nur wo er natürlich passt, nicht in jedem Beitrag.
- Reels: ab 27.11. als NORMALE Reels (share_to_feed=true, keine trial_params), erscheinen im Reels-Tab und im Profilraster (Pascals Entscheid vom 26.11.).
- Karussells: im Raster, weiterhin erstes Bild immer Pascal (echtes Foto) oder Persönliches; Folgebilder Text/Erklärfigur. Ohne passendes Foto: kein Karussell.
- Reel-Stil: Ausreden-Übersetzer mit komplett unscharfem Porträt (grad=false, blur 8); andere persönliche Reels Porträt oben scharf, Text unten.
- Musik: selbst erzeugt (tools/music.py, Stile calm/lofi/lift/tech), abwechseln.
- Finanzinhalte: keine Rendite-/Ertragsversprechen, kein «garantiert»/«risikolos», Hinweis «Allgemeine Information, keine Anlageberatung» nur bei konkreten Geld-Schritten und Vorsorge-Erklärungen, und nur in der Bildunterschrift (nicht im Video). Bei Mindset-Reels (z. B. Ausreden-Übersetzer), Gesundheit, KI, Familie weglassen (Pascals Entscheid 26.11.). Schweizer Rechtschreibung (ss). Keine Alphalane-Werbung auf diesem Profil. Krafttagebuch: @krafttagebuch in Fitness-Captions.
- Nur belegte Fakten über Pascal. Unsichere Aussagen vorher fragen.
- Pascal gibt jede Woche gesammelt frei. Bedarf an Material eine Woche vorher melden, immer optional.

## Rhythmus
- Woche 1: 26.–30.11. täglich 19:33 (26.11. noch 18:30) (Do r1, Fr r2, Sa r3, So Karussell, Mo r5)
- Ab Woche 2 (ab Di 1.12.): Mo/Mi/Fr je 2 Reels (13:33 + 19:33), Di/Do 1 Reel, 1 Karussell, 3 Storys (ohne Sticker). Zeiten nach 2 Wochen anhand der Daten anpassen.

## Ziele
10k Follower Ende 2026 unrealistisch (Start 2'244 am 25.11.2026). 100k Ende 2027 ambitioniert.

## Wochenroutine
- Jeden Montagabend prüfen: Ist für die nächsten 7 Tage Content fertig und freigegeben? Wenn nicht: nächste Woche erstellen (tools/reel.py, tools/carousel2.py, tools/story.py, Specs in JJJJ-wKW/spec/), in JJJJ-wKW/ ablegen, pushen und Pascal gesammelt zur Freigabe schicken. Erst nach seinem OK die Veröffentlichungen einplanen.
- Woche 2: 2026-w50/ (1.–7.12.), Plan-Tabelle in 2026-w50/bildunterschriften.md.
- Erklärfigur-Posen: assets/figuren/pose_*.png (in Specs als "fig": "<name>").

## Videos von anderen (YouTube usw.)
- Keine fremden Clips zuschneiden und posten (Urheberrecht, Instagram drosselt wiederverwendete Inhalte).
- Erlaubt: 1) Pascals eigene Aufnahmen (Webinare, Vorträge, Interviews) zu Reels schneiden, nur Geld/Gesundheit/KI-Allgemeines, keine Alphalane-Werbung. 2) Clips mit freier Lizenz (CC BY) oder Erlaubnis des Creators. 3) Serie «Gelernt aus …»: Kernaussagen eines Videos als eigenes Reel mit Erklärfigur und Quellenhinweis.
- Pascal schickt Links, wenn ihm etwas begegnet (freiwillig).

## Technik Veröffentlichung (getestet 26.11.2026)
- Basis-URL funktioniert: https://raw.githubusercontent.com/AlphalaneAI/pascals-instagram-media/claude/clever-hopper-ecg49y (Instagram akzeptiert die MP4 trotz octet-stream).
- Windsor execute_action create_video_post kann nach 60 s mit «timed out» enden, obwohl das Reel veröffentlicht wird. Vor einem erneuten Versuch immer per get_data (media_id, timestamp, media_caption, last_2dT, ohne force_refresh) prüfen, ob der Beitrag schon da ist. Sonst entstehen Duplikate.
- 26.11.: Reel 1 veröffentlicht, https://www.instagram.com/reel/DgNpbRbxZOQ/
- 27.11.: Reel «Bank Teil 2» IG https://www.instagram.com/reel/DgQVe9xu1oq/ + Facebook Post 247693705095520_122337473762224192 (IG-Aufruf wieder mit Timeout, trotzdem online)

## Standard-Zeiten (ab 27.11.2026, Europe/Zurich)
- Mittag 13:33, Abend 19:33. Nicht mehr 12:00/18:30.
- Grund: die 4 Konten sollen nicht gleichzeitig posten (Moonshine 11:56 und 18:26, Alphalane 20:41, Krafttagebuch 10:43 und 15:47), mindestens 1 Stunde Abstand.

## Facebook (ab 27.11.2026, von Pascal bestätigt)
- Jedes Reel nach Instagram zusätzlich als Reel auf die Facebook-Seite «Pascal Schwab Solutions»: Windsor connector facebook_organic, account 247693705095520, action create_reel, gleiche video_url, description = gleiche Caption, aber «Link in Bio» (bzw. «Link in der Bio»/«Link in meiner Bio») durch https://moonshine-solutions.com/links ersetzen.
- Nur Reels, keine Storys, keine Karussells.
- Facebook-Vorgaben: 3–90 s, 9:16, mind. 540×960, 24–60 fps. Reels daher höchstens 90 s lang machen.
- Bei Fehler oder Timeout auf Facebook nicht wiederholen, nur melden. Meldung an Pascal nennt Instagram und Facebook.
- Jede neue Reel-Aufgabe gleich mit diesem Facebook-Schritt anlegen.

## Format «Durchhalte-Köder» (von Pascal am 27.11. gewünscht, einmal einplanen)
- Vorbild: @trainwithsarahg, Reel Dfo4ATyOlTT. Ruhiger Clip (Foto von Pascal mit langsamem Zoom), grosser Text in 3 Schritten, ca. 10 s, ohne Ton.
- Referenz-Umsetzung: instagram/build_durchhalte.js im Repo alphalaneai/moonshine-solutions, Branch claude/beautiful-noether-cqkrlq. Hier mit tools/reel.py umsetzbar (3 Slides, je ca. 3 s, keine Musik).
- Text (Pascals Entscheid 27.11., genau wie das Vorbild, bewusst als Joke): «Gib deine Träume nicht auf.» → «Ich habe mit 120 Followern angefangen.» → «Heute habe ich 2 Millionen.» Ziel: Leute gehen aufs Profil, um es zu prüfen. Keine echten Zahlen einsetzen.
- Caption löst den Gag auf, z. B. «Wenn ich dich erwischt habe, habe ich einen Follow verdient 😉 Ja, das war ein Joke, schau ruhig in mein Profil.» Keine Rendite- oder Erfolgsaussagen.
- Einplanen in Woche 3 (KW 51), Termin nach Plan.

## Weitere Medienquellen (von Pascal am 27.11. freigegeben)
- Google Drive «Moonshine Instagram» (gleiche Ablage wie @moonshine.solutions): Hauptordner 1SkJh5qCAUpiMofbLO43gB16xgLd03h0n, Fotos 14W39G8MmkROjlKqtguN7udJlYBzrGih_, Videos 1gOLSHnTERnIAycrHV3CVYVwciyrCg7q- (5 Clips, MOV/MP4, 13–85 MB, z. B. Gym, SUP, Drohne).
- Darf für @pascals.solutions genutzt werden, z. B. als Hintergrund für «Durchhalte-Köder» (Video statt Foto, ohne Ton).
- Nicht denselben Ausschnitt verwenden, den Moonshine kurz davor gepostet hat (in deren Repo instagram/posted.json bzw. build_video_reel.js prüfen).
- Grosse Videos vor dem Schnitt per ffmpeg auf 1080×1920, 30 fps, ≤ 90 s verkleinern.
