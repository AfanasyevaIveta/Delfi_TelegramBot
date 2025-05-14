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
Delfi_TelegramBot
- _main.py_ - Galvenais programmas fails
- _state.json_ - Saglabā pēdējo nosūtīto ziņu ID
- _subcribers.json_ - Saglabā Telegram lietotāju ID, kuri pierakstījušies
- _README.md_ - Projekta apraksts
# Datu Struktūras
- _state.json_ satur pēdējās nosūtītās ziņas ID, lai izvairītos no atkārtotas ziņošanas
- _subscribers.json_ - satur sarakstu ar chat_id visiem pierakstītajiem lietotājiem
- Ziņas tiek formatētas kā HTML ziņojumi, izmantojot _ParseMode.HTML_
# Komandas
- /start - Pierakstīties jaunu ziņu saņemšanai
- /stop - Atteikties no ziņojumu saņemšanas
