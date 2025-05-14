# Delfi_TelegramBot
Šis projekts ir Telegram bots, kas automātiski pārbauda jaunākās ziņas no Delfi.lv RSS plūsmas un nosūta tās visiem lietotājiem. Tas darbojas pastāvīgi fonā un veic regulāras pārbaudes ik pēc 1 minutei.
# Projekta mērķis un uzdevumi
Izstrādāt automatizētu programmu Python valodā, kas:
- regulāri pārbauda RSS plūsmu no Delfi.lv
- nosūta jaunāko ziņu visiem Telegram lietotājiem, kuri ir pierakstījušies
- ļauj lietotājiem viegli pierakstīties un atteikties no ziņojumiem
- saglabā lietotāju sarakstu un pēdējo nosūtīto ziņu, lai novērstu atkārtotu sūtīšanu
# Izmantotās bibliotēkas
- _feeparser_ - RSS plūsmas nolasīšana un ziņu iegūšana
- _python-telegram-bot_ - Telegram API izmantošana, ziņu sūtīšana un komandu apstrāde
- _asyncio_ - Asinhronā darbība un cikliska pārbaude
- _json_ - Lietotāju un pēdējās ziņas datu saglabāšana
- _nest_asyncio_ - Nodrošina, ka viss darbojas arī Windows un citās vidēs, kur jau ir aktīvs event loop
# Projekta struktūra
Delfi_TelegramBot <br>
_main.py_ - Galvenais programmas fails <br>
_state.json_ - Saglabā pēdējo nosūtīto ziņu ID <br>
_subcribers.json_ - Saglabā Telegram lietotāju ID, kuri pierakstījušies <br>
_README.md_ - Projekta apraksts
# Datu Struktūras
- _state.json_ satur pēdējās nosūtītās ziņas ID, lai izvairītos no atkārtotas ziņošanas
- _subscribers.json_ - satur sarakstu ar chat_id visiem pierakstītajiem lietotājiem
- Ziņas tiek formatētas kā HTML ziņojumi, izmantojot _ParseMode.HTML_
# Komandas
- /start - Pierakstīties jaunu ziņu saņemšanai
- /stop - Atteikties no ziņojumu saņemšanas
# Kā darbojas
Bots pārbauda RSS plūsmu reizi minūtē (katras 60 sekundes). Ja tiek atrasta jauna ziņa, tās virsraksts, datums un saite tiek nosūtīta visiem lietotājiem, kas ir pierakstījušies. <br>
Ziņas ID tiek saglabāts failā _state.json_, lai nākamajā reizē tā netiktu nosūtīta atkārtoti. Visi lietotāji, kas nosūtījuši _/start_, tiek ierakstīti failā _subscribers.json_.
# Kopsapvilkums
Projektā tika iegūtas:
- darbs ar RSS arējiem datu avotiem
- asinhronas programmas darbība
- datu uzglābšana JSON formātā
