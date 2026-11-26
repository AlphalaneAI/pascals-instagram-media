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
- Finanzinhalte: keine Rendite-/Ertragsversprechen, kein «garantiert»/«risikolos», Hinweis «Allgemeine Information, keine Anlageberatung». Schweizer Rechtschreibung (ss). Keine Alphalane-Werbung auf diesem Profil. Krafttagebuch: @krafttagebuch in Fitness-Captions.
- Nur belegte Fakten über Pascal. Unsichere Aussagen vorher fragen.
- Pascal gibt jede Woche gesammelt frei. Bedarf an Material eine Woche vorher melden, immer optional.

## Rhythmus
- Woche 1: 26.–30.11. täglich 18:30 (Do r1, Fr r2, Sa r3, So Karussell, Mo r5)
- Ab Woche 2 (ab Di 1.12.): Mo/Mi/Fr je 2 Reels (12:00 + 18:30), Di/Do 1 Reel, 1 Karussell, 3 Storys (ohne Sticker). Zeiten nach 2 Wochen anhand der Daten anpassen.

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
