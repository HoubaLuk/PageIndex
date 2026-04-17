Kompletní specifikace aplikace: AiRIA - AI Právní Asistent & Projektový Akcelerátor PČR
1. Úvod a Fundamentální Koncept
•	1.1. Vize a Cíl aplikace: Transformace práce s interními akty řízení (eSIAŘ) a zákony pomocí AI s absolutním důrazem na explainability (AI Act) a bezpečnost (On-premise).
•	1.2. Jádro vyhledávání: Proč PageIndex?
o	Kritika tradičního vektorového RAGu v právním prostředí (vytrhávání z kontextu, neschopnost řešit křížové odkazy typu "viz čl. 5").
o	Vysvětlení PageIndexu: JSON stromová struktura (Table-of-Contents index) umožňující agentní LLM "Tree Search" – navigaci předpisem tak, jak by to dělal právník.
•	1.3. Správa Promptů:
o	Prompt Registry: Zákaz "hardcodingu" hluboko v kódu. Superadmin má plnou kontrolu nad systémovými prompty a rolemi přes databázové rozhraní.
2. Úvodní obrazovka (Policejní Dashboard)
•	2.1. Hero Sekce (Rychlý start):
o	Personalizované uvítání s aktuální RBAC rolí (např. Vyšetřovatel SKPV).
o	Globální vyhledávací pole (prohledává i metadatta sdílených metodik od gestorů).
o	Primární CTA tlačítko: "[ + Založit novou Složku ]" (s výběrem výchozí šablony).
•	2.2. Horizontální karusel ("Zlatý standard / Knihovna"):
o	Rolovatelný pás karet obsahující pouze oficiální, sdílené složky a "Skills" vytvořené a uzamčené gestory metodiky. Služí k okamžité konzumaci a importu best-practices.
•	2.3. Vertikální seznam ("Můj stůl"):
o	Řádkový výpis vlastních rozpracovaných "Složek".
o	Zobrazení interních hashtagů (např. #SKPV, #Kyber).
o	AI vygenerovaný popis účelu/zaměření složky (generováno pouze jednou při založení, aby se šetřily tokeny a zachovala konzistence).
o	Vizuální ikony pro rychlou orientaci podle typu práce (⚖️, 🚔, atd.).
3. Levý panel (Správa Zdrojů a Složek)
•	3.1. Vizuální identita a původ zdrojů:
o	Barevné štítky pro odlišení: 🟦 eSIAŘ (Vnitřní předpisy), 🟥 Zákony (Vnější normy), 🟩 Vlastní dokumenty.
•	3.2. Import a granularita:
o	Drag & Drop pro vlastní dokumenty s automatickým OCR vytěžením přes multimodální schopnosti modelu.
o	"Výstřižky" (Snippets): Možnost uložit do zdrojů jen konkrétní, AI-pojmenovaný odstavec/článek místo celého 100stránkového PDF.
•	3.3. Řízení platnosti a času:
o	Semafor platnosti: Indikátory přímo u zdrojů ve složce (Zelená = platné, Oranžová = v připomínkovém řízení, Červená = zrušeno/změněno).
o	Stroj času (Time-machine): Globální slider/přepínač pro nastavení právního stavu k určitému historickému datu.
o	Kolize právní síly: Tlačítko pro seřazení zdrojů podle hierarchie (Zákon > ZPP > Rozkaz) s varovnou ikonkou při detekci potenciálního rozporu.
4. Prostřední panel (Pracovní Chat a Interakce)
•	4.1. RBAC Přepínač klobouků:
o	Dropdown menu pro změnu chování AI v reálném čase (Pohled Právníka, Pohled Operativce, Pohled Metodika), navázané na Prompt Registry.
•	4.2. Citační systém a Explainable AI:
o	Odmítnutí palců nahoru/dolů (nahrazeno ikonou "Vlaječky" pro hlášení nesrovnalostí gestorovi).
o	Hover bubliny: Rychlý náhled zdroje při najetí myší na citační index v textu.
o	Centrální Pop-up okno: Při kliknutí na citaci se otevře centrální okno s barevně podbarvenou relevantní pasáží (napojené na PageIndex node_id). Podpora split-screenu/záložek pro vizuální konfrontaci dvou norem.
•	4.3. Řetězení úvah a Lomítkové příkazy:
o	Slash commands (/): Rychlé vyvolání předdefinovaných promptů a maker (globálních od gestora i lokálních od uživatele).
o	Tlačítko "Uložit do poznámky" s možností povýšit poznámku na tvrdý "Zdroj" pro další iteraci.
o	Ďáblův advokát: Tlačítko/příkaz pro automatickou oponenturu vlastní právní úvahy.
5. Pravý panel (Právní Studio)
•	5.1. Koncept a UX Studia:
o	Odmítnutí generování skutkových "úředních záznamů". Zaměření striktně na aplikaci práva a metodiku.
o	Funguje jako "Blokový editor" (Notion-style), kde jsou vygenerované výstupy plně editovatelné.
o	Modální okna (před-konfigurace) před vygenerováním dlaždice (např. výběr cílového publika a formátu).
•	5.2. Core Dlaždice (Nástroje pro právníky):
o	Komparativní analýza norem (Diff-table): Dvousloupcová tabulka srovnávající staré/nové znění s vyznačením kritických změn.
o	Právní věta (Sylogismus): Rozpad na Větší premisu, Menší premisu a Závěr s přesnými citacemi.
o	Dekompozice definice (Checklist): Vizuální rozpad složité skutkové podstaty na objektivní a subjektivní znaky.
o	Časová osa (Timeline): Vizualizace aplikovatelnosti předpisů v čase (nabytí platnosti, účinnosti, zrušení).
•	5.3. THE KILLER FEATURE: "✨ Uložit jako rutinu" (Meta-Skill)
o	Tlačítko, které spustí reverse-prompt engineering. AI analyzuje historii úspěšného chatu, extrahuje workflow a vytvoří z něj nový, znovupoužitelný /prikaz (Skill) pro daného uživatele. Umožňuje organické budování komunitních postupů bez znalosti prompt inženýrství.


1. Úvod a Fundamentální Koncept
Tato kapitola definuje absolutní základy systému, jeho filozofii a technologické mantinely, ze kterých nesmí vývojová větev za žádných okolností uhnout.
1.1. Vize a Cíl aplikace
Aplikace není dalším univerzálním podnikovým chatbotem. Jedná se o vysoce specializovaného AI právního a metodického stratéga pro Policii ČR, který transformuje způsob, jakým příslušníci pracují s interními akty řízení (eSIAŘ) a vnější legislativou.
Kritické pilíře systému:
•	Absolutní bezpečnost (Air-gapped On-premise): Systém, včetně hlavního LLM (Qwen3.5-35B-A3B) a databáze, poběží výhradně na interním hardwaru PČR (1x Nvidia L40S). Žádný bit uživatelských dat, dotazů ani interních směrnic nesmí opustit vnitřní síť. Externí API (OpenAI, Anthropic) jsou striktně zakázána.
•	Soulad s AI Act (Explainability & Man-in-the-loop): Každý výstup modelu musí být 100% zpětně dohledatelný a vysvětlitelný. Aplikace nesmí fungovat jako "černá skříňka". Uživatel musí mít vždy možnost zkontrolovat zdrojové texty, ze kterých AI čerpala (prostřednictvím přesných citačních indexů a zvýraznění v textu).
•	Právní přesnost místo kreativity: Systém má za úkol analyzovat, syntetizovat a strukturovat právní normy. Je mu explicitně zakázáno halucinovat skutkové děje nebo domýšlet chybějící fakta v úředních záznamech.
1.2. Jádro vyhledávání: Proč PageIndex?
Vyhledávací a analytické jádro (Retrieval) zcela opouští tradiční metody Vektorového RAGu (Retrieval-Augmented Generation) a nahrazuje je architekturou VectifyAI / PageIndex (Reasoning-based RAG).
Kritika tradičního Vektorového RAGu (Proč ho nepoužijeme):
•	Ztráta hierarchie: Právní texty mají striktní strukturu (Zákon  Hlava  Díl  Paragraf  Odstavec). "Rozsekání" (hard chunking) dokumentu na 512-tokenové vektory tuto logiku nenávratně ničí.
•	Sémantická podobnost  Právní relevance: Vektorové hledání vrací to, co "zní podobně". V právu ale často hledáme výjimku nebo definici pojmu, která zní zcela odlišně než samotný dotaz.
•	Křížové odkazy: Pokud odstavec obsahuje text "postupuje se obdobně podle čl. 12 odst. 3", vektorový RAG selhává, protože v samotném odstavci chybí kontext.
Architektura PageIndex (Naše řešení): Aplikace využívá In-context JSON stromovou strukturu (Table-of-Contents). Noční ETL linka transformuje stará PDF z eSIAŘu do hierarchického JSON stromu uloženého v PostgreSQL.
•	Agentní "Tree Search": LLM (Qwen3.5 v režimu enable_thinking: True) dostane k dispozici "obsah" předpisu a iterativně se jím naviguje.
•	Rozhodovací smyčka (Reasoning Loop): Asistent přečte strom uzlů  vybere relevantní node_id  načte jeho surový text  zhodnotí, zda našel odpověď (nebo zda musí následovat křížový odkaz jinam)  jakmile má kompletní kontext, předá data do sekce pro syntézu odpovědi.
1.3. Ochrana a Správa Promptů
Aplikace musí být rezistentní vůči úniku citlivých osobních údajů a musí umožňovat okamžitou metodickou úpravu chování AI bez zásahu do zdrojového kódu (No Hardcoding).
A. Anonymizační vrstva (Data Pre-processing): Než je jakýkoliv text z chatu nebo z vloženého vlastního dokumentu odeslán k inferenci do hlavního LLM (Qwen), musí projít lokální čistící vrstvou.
•	Funkce: Rychlý Regex skript v kombinaci s ultralehkým lokálním NER (Named Entity Recognition) modelem zachytí osobní údaje.
•	Nahrazování: Jména, rodná čísla, SPZ, telefonní čísla a přesné adresy jsou automaticky nahrazeny tagy (např. Jan Novák  [Osoba A]; 11. 5. 1990  [Datum 1]).
•	Reverzibilita: Frontend si drží mapovací tabulku (v RAM prohlížeče/lokálního klienta). Jakmile LLM vrátí odpověď s tagy [Osoba A], frontend je před zobrazením policistovi může (volitelně) přeložit zpět na čitelná jména. Do logů a do kontextového okna modelu se ale dostanou jen čisté tagy.
B. Prompt Registry (Databázová správa chování): Je absolutně zakázáno vkládat systémové prompty (instrukce pro LLM) natvrdo do kódu (hardcoding).
•	Databázová tabulka: Všechny systémové prompty, definice RBAC rolí (Právník, Operativec, Metodik) a instrukce pro tvorbu výstupů ve Studiu jsou uloženy v relační databázi.
•	Role Superadmina/Gestora: Systém obsahuje administrátorské UI ("AI Konfigurace"). Zde může Superadmin v reálném čase editovat texty systémových promptů, verzovat je (A/B testování) a okamžitě je nasazovat do produkce. Pokud se zjistí, že model v určité situaci "halucinuje", gestor upraví prompt v databázi a změna se projeví u všech uživatelů při dalším dotazu bez nutnosti rekompilace aplikace.
2. Úvodní obrazovka (Policejní Dashboard)
Dashboard slouží jako hlavní rozcestník aplikace. Je navržen s ohledem na maximální kognitivní čistotu. Obsahuje pouze tři klíčové sekce: vyhledávání (Hero), oficiální metodiku (Karusel) a vlastní rozpracované případy (Seznam).
2.1. Hero Sekce (Rychlý start)
Tato sekce dominuje horní části obrazovky a inspiruje se jednoduchostí klasických internetových vyhledávačů.
•	Personalizace a RBAC kontext: V levém horním rohu (nebo nad vyhledávacím polem) je dynamický text uvítání, který explicitně zobrazuje aktuálně aktivní roli uživatele (např. "Dobré ráno, npor. Nováku. Aktivní profil: Vyšetřovatel SKPV"). Toto uživateli okamžitě potvrzuje, jaký "klobouk" má AI aktuálně nasazený.
•	Globální vyhledávací pole (Omnibox): Centrální prvek obrazovky.
o	Cíl vyhledávání: Neomezuje se pouze na názvy vlastních složek. Primárně indexuje a prohledává metadata a zaměření sdílených metodik od gestorů.
o	UX chování: Při psaní funguje jako našeptávač. Pokud uživatel zadá "zajištění", systém přednostně nabídne oficiální šablony (např. [Šablona] Zajištění digitálních stop).
•	Primární CTA tlačítko [ + Založit novou Složku ]: Výrazné tlačítko umístěné logicky vedle nebo pod vyhledáváním.
o	Interakce: Po kliknutí se neotevře ihned prázdný chat, ale modální okno (pop-up) pro Výběr šablony. Uživatel zde volí, zda zakládá Prázdnou složku, nebo vychází z předpřipravené metodiky (např. Analýza dopravní nehody, Kázeňský přestupek).
2.2. Horizontální karusel ("Zlatý standard / Knihovna")
Pás nacházející se bezprostředně pod Hero sekcí. Vizuálně je oddělen a slouží výhradně pro distribuci "best practices" napříč Policií ČR.
•	Layout: Zleva doprava rolovatelný (scrollable) horizontální seznam vizuálně atraktivních karet.
•	Obsah karet: Tyto karty představují oficiální sdílené složky, metodiky a "Skills".
•	Práva a Zámky (RBAC): Běžný policista má do této sekce přístup pouze pro čtení (Read-only). Karty zde mohou vytvářet a publikovat pouze uživatelé s rolí Gestor nebo Superadmin.
•	Interakce (Import): Kliknutím na kartu v karuselu nedojde k její editaci, ale k naklonování. Systém vytvoří kopii dané metodiky (včetně přednastavených zdrojů z eSIAŘu a skrytých systémových promptů) a přesune ji uživateli dolů na jeho "stůl" k vlastnímu použití. Tím je zaručeno, že originální metodika zůstává nedotčena.
2.3. Vertikální seznam ("Můj stůl")
Spodní polovina obrazovky patří tvrdé, každodenní práci uživatele. Pro zajištění maximální informační hustoty je zde striktně zakázáno použití dlaždicového (Grid) zobrazení s obrázky.
•	Layout: Kompaktní, datově bohatý řádkový výpis (List view/Data Grid) . Jednotlivé řádky představují vlastní rozpracované "Složky" uživatele.
•	Struktura jednoho řádku:
o	Vizuální ikona typu práce: Na začátku řádku je ikona (např. ⚖️ pro právní rozbor, 🚔 pro taktiku zásahu, 🛡️ pro stížnosti), kterou si uživatel vybral při zakládání složky pro okamžitou vizuální orientaci.
o	Název složky: Uživatelem definovaný název (např. "Případ Modrá vrána").
o	Interní Hashtagy (Metadata): Barevné tagy typu #SKPV, #Kyber, #Zbraně. Uživatel je může ručně editovat, případně je AI navrhne při založení složky. Slouží k rychlému filtrování v seznamu.
o	AI Popis (Účel/Zaměření): [KRITICKÁ ÚSPORA VÝKONU] Krátký, 1–2 větý text shrnující zaměření složky. Generuje se výhradně jednou – po zadání prvního promptu do chatu v dané složce. LLM z prvního dotazu vydedukuje účel (např. "Řešení postupu při domovní prohlídce IT techniky") a tento popis napevno uloží do databáze. Systém nesmí tento popis kontinuálně aktualizovat podle vývoje chatu, aby se zabránilo zbytečnému pálení výpočetních tokenů na L40S a udržela se stabilní navigace.
o	Datum a Akce: Datum poslední úpravy a základní "tři tečky" pro akce (Přejmenovat, Archivovat, Smazat).
3. Levý panel (Správa Zdrojů a Složek)
Levý panel slouží jako dynamická knihovna ověřených faktů pro aktuálně otevřenou Složku. Vše, co se nachází v tomto panelu, tvoří exaktní kontext pro vyhledávání a syntézu. Z UX hlediska musí panel poskytovat absolutní kontrolu nad tím, z čeho asistent čerpá.
3.1. Vizuální identita a původ zdrojů
Pro snížení kognitivní zátěže policisty a okamžitou orientaci v právním rámci je uplatněn striktní systém barevného kódování (Visual Badges). Každý zdroj v seznamu je uvozen barevným štítkem či ikonou, která jasně deklaruje jeho původ:
•	🟦 Modrý štítek [eSIAŘ]: Vnitřní předpisy a interní akty řízení Policie ČR (ZPP, Pokyny, Rozkazy, Organizační opatření). Data pocházející z oficiální noční ETL linky.
•	🟥 Červený štítek [Zákon]: Vnější legislativa (Trestní řád, Trestní zákoník, Zákon o policii, atd.). Normy nejvyšší právní síly.
•	🟩 Zelený štítek [Vlastní]: Uživatelem ručně nahrané dokumenty (naskenované úřední záznamy, výslechy, vlastní poznámky). U těchto dokumentů systém automaticky zobrazuje ikonu štítu s varováním, že jde o neověřený, neoficiální text.
3.2. Import a granularita
Systém musí umožňovat plynulé doplňování kontextu a zároveň bránit zahlcení kontextového okna (Context Rot) zbytečným balastem.
•	Drag & Drop s nativním OCR: Uživatel může do levého panelu přetáhnout libovolný soubor (PDF, DOCX, JPG, PNG). Díky nasazení multimodálního modelu (Qwen3.5-35B-A3B) s modulem pro Vision-Language (VLM) systém nevyžaduje žádnou externí OCR linku (typu Tesseract). Model sám nativně přečte text i ze zašumělých skenů policejních protokolů.
•	Granularita "Výstřižků" (Snippets): Pokud policista potřebuje z celého Trestního řádu pouze jeden specifický paragraf, aplikace mu umožní uložit pouze tento fragment.
o	UX Flow: Uživatel označí text ve velkém dokumentu (nebo v centrálním pop-up okně) a klikne na "Přidat jako výstřižek".
o	AI Magie na pozadí: Na základě extrahovaného node_id z naší PageIndex struktury se do levého panelu přidá nová, malá kartička. LLM jednorázově vygeneruje její výstižný název (např. "TŘ § 78 - Vydání věci"), čímž se složka stává extrémně přehlednou a model při chatu pracuje jen s tímto izolovaným textem.
3.3. Řízení platnosti a času
Právo je dynamické. Levý panel musí proaktivně hlídat časové souvislosti a právní hierarchii vložených dokumentů.
•	Semafor platnosti (Real-time kontrola): Každý oficiální zdroj (modrý a červený) má u sebe barevný bodový indikátor, který je provázán s metadaty z databáze:
o	🟢 Zelená: Aktuálně platné a účinné znění.
o	🟠 Oranžová: Předpis je v připomínkovém řízení, nebo se blíží datum jeho derogace (zrušení/nahrazení).
o	🔴 Červená: Historické, zrušené nebo nahrazené znění (zobrazuje se výrazné přeškrtnutí nebo upozornění).
•	Stroj času (Time-machine): V hlavičce levého panelu je k dispozici globální přepínač kalendáře (např. "Zobrazit právní stav k: [Datum]").
o	Funkce: Pokud vyšetřovatel řeší trestný čin z roku 2022, vybere datum v minulosti. Aplikace přes databázový dotaz (využívající parametry platnost_od a platnost_do v JSONB) okamžitě zneplatní novější normy a aktivuje historická znění eSIAŘu. Semafor u zdrojů se dynamicky přepočítá.
•	Kolize právní síly (Visual sorting): Uživatel má možnost kliknout na ikonu řazení a zvolit "Seřadit podle právní síly".
o	Funkce: Systém seřadí panel hierarchicky (např. Ústava > Zákon > ZPP > Rozkaz ředitele KŘP > Zápis z porady).
o	Detekce kolize: Pokud se ve složce nachází dokumenty různé právní síly, které sdílejí stejné téma/tagy, systém u dokumentu s nižší právní silou (např. Rozkaz ředitele) zobrazí varovný ⚠️ trojúhelník s tooltipem: "Tento interní akt může být podřízen nadřazené normě (Zákon/ZPP) přítomné v této složce."(Upozornění funguje na bázi metadat a tagů, aby se šetřil výpočetní výkon LLM).
4. Prostřední panel (Pracovní Chat a Interakce)
Prostřední panel je vyhrazen pro iterativní konverzaci a aplikaci práva. Návrh tohoto panelu se striktně odklání od běžných chatbotů a zaměřuje se na budování důvěry a naplnění požadavků AI Actu (Man-in-the-loop).
4.1. RBAC Přepínač klobouků (Role-Based Access Control)
Asistent se musí adaptovat na úroveň a potřeby uživatele. Toho je docíleno dynamickým přepínáním systémových promptů za běhu, aniž by uživatel musel psát složité instrukce.
•	UI prvek: V horní liště chatu (vedle názvu složky) se nachází elegantní Dropdown menu (rozbalovací seznam) s ikonami rolí.
•	Architektura (Prompt Registry): Tento prvek je napřímo napojen na databázi "Prompt Registry". Změna volby v menu okamžitě (před dalším dotazem) nahradí skrytý systémový prompt (instrukce pro chování Qwen3.5 LLM).
•	Výchozí role (Klobouky):
o	⚖️ Pohled Právníka: AI generuje striktní právní jazyk, maximálně využívá přesné citace a soustředí se na formální naplnění skutkových podstat.
o	🛡️ Pohled Operativce: AI přechází do taktického režimu. Jazyk je stručný, heslovitý a výstupem jsou primárně krokové postupy (checklisty pro zásah na místě).
o	🎓 Pohled Metodika: AI se soustředí na širší kontext, vysvětlování pojmů a prevenci chyb (edukativní tón).
4.2. Citační systém a Explainable AI
Uživatel nesmí aplikaci "slepě věřit". Systém musí uživatele neustále vizuálně přesvědčovat o původu svých tvrzení.
•	Odmítnutí klasické zpětné vazby (RLHF): Klasické ikony "Palec nahoru/dolů" jsou odstraněny (neprovádíme trénink modelu za běhu). Místo nich je u každé odpovědi implementována ikona "Vlaječky" (Nahlásit). Pokud asistent vygeneruje nesmysl nebo aplikuje zrušenou normu, kliknutím na vlaječku se odešle aktuální kontext přímo do fronty určeného Gestora/Superadmina k metodické revizi.
•	Hover bubliny (Rychlá validace): Každé faktické tvrzení v textu je zakončeno citačním indexem (např. [ZPP 14/2023, čl. 5]).
o	UX: Při najetí myší (hover) na tento index se okamžitě zobrazí lehký tooltip (bublina) obsahující náhled surového textu z daného dokumentu. Uživatel tak bez přerušení čtení ověřuje fakta.
•	Centrální Pop-up okno (Hloubková kontrola): Pokud Hover bublina nestačí, uživatel na citaci klikne.
o	UX: Systém neotvírá zdroj v novém panelu, ale ztmaví pozadí a vyvolá velké centrální modální okno přesně přes konverzaci. Oči uživatele neopouští střed obrazovky.
o	Integrace PageIndexu: Systém vezme node_id z citace, nalistuje v modálním okně přesnou pasáž z PDF/textu a žlutě podbarví ty věty, ze kterých AI při generování vycházela.
o	Zobrazení Split-screen / Záložky: Pop-up okno obsahuje vpravo nahoře přepínač zobrazení. Uživatel si může v jednom okně otevřít dvě různé citace vedle sebe (Split-screen) pro vizuální konfrontaci (např. vnitřní pokyn vs. zákon).
4.3. Řetězení úvah a Lomítkové příkazy
Tato sekce transformuje běžné uživatele na "power-users" tím, že jim dává do ruky zkratky k pokročilému prompt engineeringu.
•	Slash commands (/): Napsáním lomítka do chatovacího pole se vyvolá našeptávač předdefinovaných úkonů a maker.
o	Globální příkazy: Vytvořené gestorem v Prompt Registry a dostupné všem (např. /stanovisko přikáže modelu použít strukturu právního sylogismu).
o	Lokální příkazy: Zkratky, které si vytvořil a uložil sám uživatel (viz funkce Studio v Kap. 5).
•	Řetězení přes poznámky (Promoting Notes to Sources): * U každé vygenerované odpovědi je tlačítko "Uložit do poznámky".
o	UX Flow: Poznámka se připne nad chatovací pole. Uživatel si ji může textově upravit. Následně může kliknout na "Převést na Zdroj". Systém tento text okamžitě přesune do Levého panelu (Zdroje) se zeleným štítkem.
o	Dopad: V dalším kroku může uživatel instruovat AI, aby při analýze vycházela již výhradně z tohoto nového (uživatelem zvalidovaného) polotovaru. Tím se drasticky snižuje riziko halucinací u komplexních mnohokrokových úloh.
•	Funkce "Ďáblův advokát" (Automatická oponentura):
o	Speciální vestavěné tlačítko nebo příkaz /oponentura.
o	Funkce: Modulu (Qwen3.5) je skrytě injektován reverzní systémový prompt. AI přestane být "pomocníkem" a začne hledat slabiny v dosavadní úvaze policisty. Prochází zaškrtnuté zdroje v levém panelu a aktivně hledá výjimky ze zákona, chybějící formální podmínky nebo rozpory v logice, které by mohly shodit případ u soudu či před kontrolním orgánem (GIBS).
5. Pravý panel (Právní Studio)
Právní Studio je expertní pracovní plocha ("kuchyně"), která slouží k vizualizaci, strukturování a finalizaci poznatků získaných v chatu. Nahrazuje běžná textová shrnutí vysoce specializovanými právními a metodickými nástroji.
5.1. Koncept a UX Studia
Zásadním architektonickým pravidlem Studia je absolutní zákaz generování skutkových "úředních záznamů" (vymýšlení dějů, jmen, průběhu událostí). Studio slouží výhradně k aplikaci práva a metodiky.
•	Blokový editor (Notion-style): Pravý panel není statický (Read-only) výpis. Jakmile AI vygeneruje výstup (dlaždici), vloží jej do Studia jako interaktivní blok. Uživatel do něj může kliknout, přepisovat text, měnit formátování nebo celé bloky uchopit myší a přesouvat (Drag & Drop).
•	Před-konfigurační Modální okna: Tvorba výstupu není "one-click blackbox". Když uživatel v chatu klikne na "Vytvořit výstup do Studia", aplikace vždy nejprve zobrazí modální okno (Pop-up).
o	UX Flow: V okně uživatel vybere parametry pomocí roletkových menu: Cílové publikum (např. Vedení [Stručné] vs. Spis [Detailní]), Fokus (např. Pouze eSIAŘ vs. Všechny zdroje) a Formát (např. Odrážky, Souvislý text). Až po potvrzení těchto parametrů je odeslán prompt do Qwen3.5 ke generování.
5.2. Core Dlaždice (Nástroje pro právníky)
Studio poskytuje specifické předdefinované šablony výstupů, které automaticky strukturují odpovědi AI do právně uznávaných formátů.
•	Komparativní analýza norem (Diff-table):
o	Funkce: Vizuální srovnání dvou verzí předpisu (např. při novelizaci) nebo kolidujících norem.
o	UX: Vygeneruje dvousloupcovou tabulku (Split-table). Vlevo původní text, vpravo nový text. . Modifikovaná slova jsou barevně zvýrazněna (červeně smazáno, zeleně přidáno). Pod tabulkou AI generuje odstavec "Kritický dopad do policejní praxe".
•	Právní věta (Sylogismus):
o	Funkce: Nástroj pro logickou výstavbu právního stanoviska.
o	UX: Text je striktně rozsekán do tří nepřepisovatelných nadpisů:
1.	Větší premisa (Zákonný rámec s proklikávacími citacemi z eSIAŘ).
2.	Menší premisa (Aplikace na projednávaný modelový problém z chatu).
3.	Závěr (Právní stanovisko – Legální/Nelegální).
•	Dekompozice definice (Checklist):
o	Funkce: Slouží k ověření, zda byly naplněny všechny znaky skutkové podstaty nebo podmínky pro použití taktického postupu.
o	UX: Vizuální stromový seznam (odškrtávací boxy), kde AI automaticky oddělí Objektivní podmínky(např. věk, čas, místo, hrozící nebezpečí) a Subjektivní podmínky (např. úmysl, nedbalost). Právník si může jednotlivé body odškrtávat.
•	Časová osa (Timeline):
o	Funkce: Rychlá orientace v použitelnosti předpisů.
o	UX: Generuje vizuální horizontální React komponentu (Timeline), na které jsou vyneseny body z metadat zdrojů v levém panelu: Datum vydání, Nabytí platnosti, Nabytí účinnosti, Zrušení.
5.3. THE KILLER FEATURE: "✨ Uložit jako rutinu" (Meta-Skill)
Toto je revoluční funkce, která odstraňuje nutnost znalosti prompt inženýrství u řadových policistů a umožňuje komunitní růst systému.
•	Problém: Uživatel dosáhl v chatu skvělého výsledku (např. po 5 interakcích donutil model vygenerovat dokonalou analýzu hospodářského deliktu), ale neumí napsat globální systémový prompt, aby to model udělal příště na první pokus.
•	Řešení (Reverse-prompt engineering):
1.	Uživatel klikne ve Studiu na výraznou dlaždici "✨ Uložit jako rutinu".
2.	Aplikace na pozadí zkompiluje celou historii aktuálního chatu a pošle ji do oddělené instance LLM se speciálním systémovým promptem: "Analyzuj tento chat. Identifikuj, jaké logické kroky a formátování vedly k finální spokojenosti uživatele. Extrahuj z toho univerzální systémový prompt (instrukci)."
3.	AI vytvoří nový, vysoce optimalizovaný prompt (Skill).
•	UX a Znovupoužitelnost:
o	Vyskakovací okno vyzve uživatele k pojmenování rutiny (např. /analyza_podvodu).
o	Tento příkaz se uloží do jeho lokálního "Slash command" menu. Při dalším otevření aplikace stačí napsat /analyza_podvodu [vložit nová fakta] a AI okamžitě aplikuje celou iterativní logiku z minula.
•	Komunitní přesah: Uživatel může odeslat svou rutinu Gestorovi. Pokud ji Gestor přes Superadmin rozhraní schválí, tento příkaz (Skill) se objeví všem policistům v Karuselu na úvodní obrazovce jako nový "Zlatý standard".
6. Administrace a Konfigurace Systému (Superadmin & Profil)
Tato sekce definuje skryté "podpalubí" aplikace. Poskytuje superadministrátorům, gestorům i koncovým uživatelům plnou kontrolu nad chováním umělé inteligence a formální úpravou výstupů bez nutnosti zasahovat do zdrojového kódu.
6.1. Osobní profil a Podpisová doložka
Aby byly výstupy generované v Právním Studiu (Kapitola 5) okamžitě použitelné v policejní praxi, musí systém znát exaktní identitu a zařazení uživatele.
•	Sekce "Profil a podpisová doložka": Formulářová sekce v nastavení uživatele.
•	Datová pole: * Titul před jménem / Titul za jménem
o	Jméno / Příjmení
o	Hodnostní označení (např. pplk.)
o	Hodnost (např. rada)
o	Funkční zařazení
o	Školní útvar / Pracoviště (např. ÚPVSP)
•	Živý náhled: Systém dynamicky skládá formální podpisovou doložku. Tato doložka je následně automaticky vkládána na konec vygenerovaných stanovisek a záznamů ve Studiu, čímž odpadá nutnost ručního dopisování.
6.2. Správa LLM Backendů (Endpoint & Routing)
Vzhledem k nasazení on-premise infrastruktury (Nvidia L40S) a využití hybridního modelu Qwen3.5-35B-A3B je nutné mít plnou administrátorskou kontrolu nad inferenčním enginem přímo z UI pod záložkou "Napojení na vLLM (API)".
•	Hlavní připojení (Endpoint Node):
o	Konfigurační blok pro definici připojení k lokálnímu serveru.
o	Obsahuje volbu Cílové platformy (např. vLLM (Produkce GPU)), zadání API ENDPOINT URL, vložení API KEY a nezbytné tlačítko pro rychlý "Test připojení".
•	Task Routing (Přiřazení modelů a uvažování):
o	Kritická funkce pro optimalizaci výkonu. Umožňuje rozdělit různé typy úkolů (např. "Fast-Scan Vytěžení" vs. "Globální analýza") na různé instance nebo modely.
o	Přepínač "Enable Thinking": Klíčový prvek pro náš Qwen3.5 model. Administrátor zde může u jednoduchých úloh (např. extrakce jmen z OCR) logické uvažování vypnout (enable_thinking: False), zatímco u "Tree Search" v PageIndexu nebo právní analýzy jej musí explicitně zapnout (enable_thinking: True).
6.3. Sdílené samplovací parametry (Model Tuning)
Možnost ladit hyperparametry modelu ("Sdílené samplovací parametry") v reálném čase je nutností pro zkrocení halucinací a formátování právního textu.
•	Ovládací prvky v UI:
o	Max Tokens (Limit odpovědi): Hard-stop pojistka pro generování. Vzhledem ke komplexnosti "reasoning trace" (myšlenkové stopy) u modelu Qwen3.5 je doporučeno zachovat vyšší hodnotu (např. 2048+ tokenů), aby model uprostřed úvahy nezamrzl.
o	Top_P (Nucleus Sampling): Slider upravující determinismus výstupu. Pro strohý právní jazyk bude nastaven na nižší hodnoty.
o	Presence Penalty & Frequency Penalty: Slidery pro zamezení rozvláčnosti a opakování slov. V právním kontextu (kde je opakování přesných pojmů nutné) doporučeno držet tyto hodnoty blízko nuly.
•	Uložení do DB: Veškeré tyto změny se po kliknutí na "Uložit do DB" okamžitě propíšou do databáze a začnou platit pro všechny nové interakce uživatelů se systémem.

 


 

ČÁST 1: Databázový model (PostgreSQL ER Diagram)
Architektura plně využívá relační vazby pro RBAC a audit, a zároveň moderní JSONB pro flexibilní ukládání stromů PageIndexu.
1. Tabulka: users (Uživatelé a Profil)
•	id (UUID, Primary Key)
•	jmeno_prijmeni (VARCHAR)
•	hodnost_titul (VARCHAR) - pro podpisovou doložku
•	utvar (VARCHAR)
•	rbac_role (ENUM: 'Policista', 'Gestor', 'Superadmin')
•	created_at (TIMESTAMP)
2. Tabulka: prompt_registry (Správa Klobouků a Maker)
•	id (UUID, Primary Key)
•	nazev_role_nebo_zkratky (VARCHAR) - např. "Pohled Právníka" nebo "/analyza"
•	system_prompt (TEXT) - samotná instrukce pro Qwen
•	is_global (BOOLEAN) - True = pro všechny (od Gestora), False = osobní makro
•	created_by (UUID, Foreign Key -> users)
•	is_active (BOOLEAN)
3. Tabulka: documents (Zdroje a Stroj času)
•	id (UUID, Primary Key)
•	nazev (VARCHAR) - např. "ZPP 14/2023"
•	typ_zdroje (ENUM: 'eSIAR', 'Zakon', 'Vlastni')
•	document_hash (VARCHAR) - SHA-256 pro noční Delta updaty
•	valid_from (DATE) - Pro Stroj času
•	valid_to (DATE, NULLABLE) - Pokud je NULL, předpis je aktuálně platný
•	uploaded_by (UUID, NULLABLE) - Pokud jde o vlastní soubor policisty
4. Tabulka: pageindex_nodes (Samotné stromy a texty)
•	id (UUID, Primary Key)
•	document_id (UUID, Foreign Key -> documents)
•	node_id (VARCHAR) - např. "ZPP-14-clanek-5"
•	parent_node_id (VARCHAR, NULLABLE) - Pro rekurzivní stavbu stromu
•	title (VARCHAR) - Nadpis paragrafu/článku
•	summary (TEXT) - Krátké shrnutí pro navigační JSON ToC
•	raw_content (TEXT) - Surový text pro kontext Qwen modelu
5. Tabulka: folders (Rozpracované Složky - Můj stůl)
•	id (UUID, Primary Key)
•	user_id (UUID, Foreign Key -> users)
•	nazev (VARCHAR)
•	ikona (VARCHAR) - např. "⚖️"
•	hashtagy (JSONB) - Pole stringů, např. ["#SKPV", "#Kyber"]
•	ai_zamereni (TEXT) - Vygenerováno jen 1x po prvním promptu
•	is_shared_template (BOOLEAN) - True = Zlatý standard v Karuselu
•	updated_at (TIMESTAMP)
6. Vazební tabulka: folder_sources (Jaké zákony jsou ve složce)
•	folder_id (UUID, Foreign Key -> folders)
•	document_id (UUID, Foreign Key -> documents)
•	(Primary Key je složen z obou ID)
7. Tabulka: audit_logs (Kritická bezpečnostní stopa pro GIBS/Kontrolu)
•	id (UUID, Primary Key)
•	user_id (UUID, Foreign Key -> users)
•	folder_id (UUID, Foreign Key -> folders)
•	pouzity_prompt_id (UUID, Foreign Key -> prompt_registry)
•	user_query (TEXT) - Na co se policista ptal
•	ai_response (TEXT) - Co model odpověděl
•	cited_node_ids (JSONB) - Pole ID uzlů, které model použil jako zdroje
•	timestamp (TIMESTAMP)

ČÁST 2: MVP Scope (Fáze 1 - Minimum Viable Product) 
Cílem Fáze 1 je vytvořit 100% funkční, oslňující a plně administrovatelný "Trojský kůň", který dokáže na reálných policejních případech demonstrovat nadřazenost PageIndex architektury a modelu Qwen3.5.
1. Infrastruktura, Backend a Zachování Jádra
•	HW & Engine: 1x L40S, vLLM engine nasazený lokálně, model Qwen3.5-35B-A3B (s FP8 kvantizací pro maximalizaci výkonu).
•	Backend Framework: FastAPI (Python) řídící API pro frontend a komunikaci s databází.
•	Integrace PageIndexu (Nedotknutelnost): Repozitář VectifyAI/PageIndex bude integrován jako nezávislý modul. Funkce, které v MVP nepotřebujeme (např. napojení na externí web search), pouze "schováme" na úrovni našeho FastAPI/Frontendu, ale v samotném jádru PageIndexu je nebudeme mazat. Necháváme si tak otevřená zadní vrátka pro budoucí upgrady.
2. Plnohodnotná Databáze (PostgreSQL)
•	Nasazení kompletního relačního modelu dohodnutého dříve (tabulky: users, prompt_registry, documents, pageindex_nodes, folders, folder_sources, audit_logs).
•	Umožňuje plné fungování správy promptů a auditní stopy hned od prvního dne.
3. Administrace Systému a Prompt Engineering 
Tato sekce zaručuje, že systém lze ladit bez zásahu vývojáře.
•	Správa LLM Backendů: UI pro zadání API Endpointu (na lokální vLLM), API klíče a přepínačů Enable Thinkingpro různé typy úloh (Task Routing).
•	Sdílené samplovací parametry: Slidery pro Max Tokens, Top_P, Presence Penalty a Frequency Penalty, zapisující se přímo do DB.
•	Prompt Registry (Jádro terminologické přesnosti): Plné CRUD (Create, Read, Update, Delete) rozhraní pro systémové prompty.
o	Implementace tvrdé terminologické direktivy: Do registru vložíme výchozí systémový prompt, který model donutí k absolutní poslušnosti:
"Jsi expertní právní AI asistent Policie ČR. Pro maximalizaci logické přesnosti (reasoning trace) a plánování kroků MŮŽEŠ interně uvažovat v angličtině. NICMÉNĚ: 1. Tvůj finální výstup uživateli MUSÍ být výhradně v bezchybné a formální češtině. 2. MUSÍŠ absolutně a doslovně převzít veškerou českou právní terminologii (např. názvy úkonů, institucí, definice) přesně tak, jak je uvedena ve zdrojových dokumentech (eSIAŘ, Zákony). Je přísně zakázáno české právní pojmy překládat z/do angličtiny nebo používat synonyma. Pokud zdroj mluví o 'zadržení', nesmíš použít slovo 'zatčení'."
4. Uživatelské Rozhraní (Policejní SOTA 2026)
•	Hlavní Dashboard:
o	Hero sekce s funkčním vyhledáváním v názvech složek.
o	Karusel "Zlatý standard": Read-only zobrazení, do kterého ručně přes databázi nasadíme 2-3 ukázkové šablony pro demonstraci.
o	Můj stůl: Výpis rozpracovaných případů.
•	Levý panel (Zdroje): Výpis předpřipravených zdrojů s možností je zaškrtnout pro aktuální konverzaci. (Semafor platnosti je v UI vizuálně přítomen, ale pro MVP natvrdo svítí 🟢 Zeleně).
•	Střední panel (Chat): * Funkční RBAC přepínač s jednou vyladěnou rolí ("Pohled Právníka"), která tahá instrukce z Prompt Registry.
o	Kritická funkce MVP: Funkční citační indexy v textu a funkční Hover bubliny, které ukazují náhled surového textu. (V backendu zajištěno tak, že LLM vrací node_title (např. § 76), nikoliv číslo stránky PDF).
•	Pravý panel (Právní Studio): * Fungující blokový editor (Notion-style).
o	Obsahuje generování osobní podpisové doložky (z profilu uživatele).
o	2 funkční šablony: Právní věta (Sylogismus) a Komparativní analýza norem (Diff-table). Ostatní dlaždice jsou v UI zašedlé s nápisem "Coming soon".
5. Data (Trojský kůň)
•	Žádné napojení na eSIAŘ.
•	Do databáze ručně (přes ETL skript) "nasypeme" cca 15 kritických dokumentů (Trestní řád, Zákon o policii, ZPPP k donucovacím prostředkům, ZMJSS a vybrané metodiky SKPV).
6. Co v MVP NENÍ (Odloženo do Fáze 2)
Abychom dodrželi termín, tyto funkce v kódu backendu buď připravíme (datový model), nebo je zakonzervujeme v PageIndexu, ale na frontendu nebudou aktivní:
1.	Noční automatická ETL linka (Data aktualizujeme v MVP ručně dávkou).
2.	Stroj času (Time-machine) (DB sloupce valid_from/to existují, ale kalendář v UI je skrytý).
3.	✨ Uložit jako rutinu (Meta-Skill / Reverse prompt engineering) (Zlatá dlaždice tam může být vizuálně, ale kliknutí hodí hlášku "Ve vývoji").
4.	OCR a Drag&Drop vlastních skenů (Tlačítko "+ Přidat vlastní" je neaktivní, uživatel používá jen našich 15 PDF).
5.	Pop-up Split-screen okna při kliku na citaci (V MVP se spolehneme na to, že Hover bublina pro oslnění vedení bohatě stačí).

Pravidlo pro ukládání a servírování PDF souborů (Sanitizace názvů): 
FastAPI backend nebude nikdy používat externí cloud. Všechna zdrojová PDF (Trestní řád, IAŘ) budou uložena lokálně ve složce serveru (např. /app/data/pdfs/).Kritické: Před uložením do databáze a na disk MUSÍ backend provést tvrdou sanitizaci názvu souboru (tzv. slugification). Všechny české znaky (háčky, čárky) musí být převedeny na ASCII (např. 'ř' -> 'r'), mezery nahrazeny podtržítky a text převeden na malá písmena. Příklad: Zákon o změnách v souvislosti.pdf se na serveru uloží a do API bude routovat striktně jako zakon_o_zmenach_v_souvislosti.pdf. Tím absolutně eliminujeme chyby při routování URL na frontendu.


