# This is an example how the code could be used
from scraper.scraper import Scraper
from scraper.client import Client

Client(api_id=...,
       api_hash="...",
       phone="...")

scraper = Scraper(num_messages=None,
                  step_size=200,
                  maximum_iterations=2)
                  #, timeframe=

seed_channels = ["Bauern_Verbraucher_geeint_Kanal",
    "Bauernprotest_0801",
    "bauernprotesteschweiz",
    "BauernprotestbewegungSchweiz",
    "Bauernproteste",
    "Bauernaufstand",
    "ehrlichalexander",
    "bauernprotestschweiz",
    "BauernprotestRealitat",
    "Bauernproteste2",
    "bauernprotestevideos",
    "bauernprotesteinfosbilder",
    "BauernprotesteundProteste",
    #"coronaquerfront", -> nothing directly with covid
    "martinsellnerIB",
    "freiesachsen",
    "auf1tv",
    "neuesausrussland",
    "unzensiertv2",
    "EvaHermanOffiziell",
    "Bauernaufstand"
]

'''
# weniger seeds & gleiche seeds wie aleksandra: martinsellner [right-extremist actor] & anderer
seed_channels = [
    #"lionmediatelegram", -> NA
    #"haunsiappmann", -> NA (chat exists: https://t.me/HaunsiAppmannChat)
    #"qwwg1wga16plus1", -> NA
    #"ra_ludwig",
    #"anonymousschweizorginal", -> NA
    "unzensiertkontaktbot", #(Bot; echter Channel: https://t.me/unzensiert)
    #"newsostberlin", -> NA
    #"coronavirushilfe", -> NA
    "tonitano",
    "militaernews",
    #"legitimnews",
    #"gemeinsamgegennwo",
    #"vaxxed_greatawakenig",
    #"weissesarmband",
    #"cnconspiracynewsroom",
    #"into_the_light_news",
    #"connectivevents",
    #"q_gold",
    #"bleibtstark",
    #"rt_deutsch",
    #"sandysteen1", -> NA
    #"fragunsdoch_wwg1wga", -> NA (Nachahmer: https://t.me/fragunsdoch_WWG1WGAgibMirGeld)
    # "donald_j_trump_q_family_germany", -> NA (Nachahmer https://t.me/DONALD_J_TRUMP_Q_FAMILY_GERMAN)
    #"miriamhope", -> NA (Nachfolgeraccount: https://t.me/MiriamHope_Original)
    #"qpluswatnn", -> NA
    #"stefanraven",
    "durov",
    #"aerztefueraufklaerungoffiziell",
    #"buergerinformative",
    #"weltdergesundheittv",
    #"project_veritas",
    #"q74you",
    #"wahrheitstraeumer",
    #"demotermine!", -> NA (alternative: https://t.me/Demotermine)
    #"holistischegesundheitheilung",
    #"anons17",
    #"ddddoffiziell",
    #"globaleserwachen",
    #"zehnmin",
    #"qbavaria",
    #"trumpcomesback", -> NA (Nachahmer exists: https://t.me/Trumpcomesback1)
    #"vereinigtewahrheitsbewegung",
    #"jackdawkins",
    #"police_frequency",
    #"q_proofs",
    #"notisolate",
    #"ayse_meren_hp",
    #"kampf_fuer_unsere_zukunft",
    #"verbindediepunkte",
    #"michaelwendlerofficial",
    #"bitchbotboiilive",
    #"verstehenhandeln", -> NA
    #"saraslightfight",
    #"meinednews",
    #"rtintl",
    #"reitschusterdechat",
    #"einerfueralle_allefuereinen",
    #"timmkellner",
    #"klartext2021gemeinsam",
    #"digitalsoldiersgermanynews",
    #"qlobalchangeusa",
    #"mstpatriotnrw",
    #"wwg1wgaworldwide",
    #"polizeigewalt",
    #"translatedpressde",
    #"bewussttv",
    #"dokukiste",
    #"fletchersvisionen", -> NA (bot exists)
    #"mutflash",
    #"billsix",
    #"flacheerdegemeinschaft",
    #"q_anonymous_kanal_deutschland",
    #"mannmitbartarchiv", -> NA
    "news1g",
    #"erwachen2021",
    #"betterknownow",
    #"lionmediatv",
    #"defender_shaef_2q2q", -> NA
    #"marry3456", -> NA
    #"oli_redet", -> NA (Nachahmer exist)
    #"q_d_r_area17",
    #"digitalerchronist_allgemeinchat",
    #"ostberlin_shaef_2q2q",
    #"qanoninternational", -> NA (alternative exist: https://t.me/QAnonInternationalInfo)
    #"chatignazbearth", -> NA
    #"infokrieg", -> NA (undirect alternatives exist)
    #"paedagogenfueraufklaerunggroup", -> NA
    #"nityachatroom", -> NA
    #"wdchurlinks", -> NA
    #"qgoldenage", -> NA
    #"augenaufchataac", -> NA
    #"q_for_you_chat", -> NA
    #"mig_chat", -> NA
    # "informationsaustauschch", -> NA (gesperrt, alternative https://t.me/InformationsaustauschCH2; https://t.me/+9eRwK0bZBQQyMTk0)
    #"gfdv_chat", -> NA
    #"dasweiber2021", -> NA
    #"internationalcoronanews", -> NA
    #"quicksatnet", -> NA
    #"einerfueralle_allefuereinen_chat", -> NA (alternative exists: https://t.me/EinerFuerAlle_AlleFuerEinen_2020 => scrape also?)
    #"diehelfendehandtalk", -> NA
    #"werner_altnickel_info", -> NA
    #"q_d_r_area", -> NA
    #"libertetalk", -> NA
    #"globalawakeningartchat", -> NA
    #"verruecktesjahr202q", -> NA
    #"suefortruth", ->NA
    #"wombels_kunst", -> NA
    #"erwache20", -> NA
    #"infokanalberlin_chat", -> NA
    #"erwachen2023", -> NA
    #"trick_siebzehn", -> NA
    #"chiemseefeechat", -> NA
    #"mstpatriotnrwchat", -> NA
    #"talawolf", -> NA
    #"schaebelsblog", -> NA (bot exists)
    #"kaiaushannover", -> NA
    #"dt64infoampulsderzeit207", -> NA
    #"chat_einerfueralle_allefuereinen", -> NA (alternative exists: https://t.me/EinerFuerAlle_AlleFuerEinen_2020 => scrape also?)
    #"gehlkenronald",
    #"dt64infoproundcontra207", -> NA
    #"friede_freiheit_demokratie_chat", -> NA
    #"technicus_news", -> NA
    #"aufwachen369", -> NA
    #"widerstand81", -> NA
    #"aufklaerung2020", -> NA
    #"gegennwochat", -> NA
    #"wie_bitte_echt_jetzt", -> NA (bot exists)
    "derschwarzeritter",
    #"freiheitschat2020", -> NA
    #"huerdenflug_chat", -> NA
    #"wiserwithkaiser", -> NA
    #"q_d_r_army", -> NA (bot exists)
    #"bioapis",
    #"defender2020kanal", -> NA
    #"lichtanonsmensch", -> NA
    #"checkmatenewsgroup", -> NA
    #"heimatgewaltfreivereint" -> NA
]
[
  "defender_shaef_2q2q",
  "qanons_deutschland",
  "marry3456", # no
  "oli_redet", # no
  "q_d_r_area17",
  "digitalerchronist_allgemeinchat",
  "ostberlin_shaef_2q2q", # no
  "qanoninternational", # no
  "impfkritisch",
  "diemaske_themask",
  "chatignazbearth",
  "bandofanons",
  "gemeinsamgdnweltordnung",
  "energyistalles", # no
  "vereinigtewahrheitsbewegungchat", # no
  "infokrieg", # no
  "paedagogenfueraufklaerunggroup", # no
  "deutschelobbychat", # no
  "ernergieistalles", # no
  "karinschatzbaechtiger",
  "traugottickerothliveticker",
  "vereinigtescharfschuetzenchat", # no
  "nityachatroom", # no
  "impfen_nein_danke",
  "nuochat", # no
  "wdchurlinks", # no
  "qgoldenage",
  "dumm_gehaltenchat", # no
  "trump_17",
  "augenaufchataac", # no
  "demostreamgruppe",
  "preussenspatriotenelite", # no
  "q_for_you_chat", # no
  "peacecrowd_gruppe", # no
  "digitalsoldiersgermany", # no
  "mig_chat",
  "rbk_2020",
  "karpfsebastian",
  "expresszeitungdiskussion",
  "informationsaustauschch",
  "gurkenpauleseinflugschneise",
  "pnewschat",
  "gfdv_chat",
  "dasweiber2021",
  "tao_chatgruppe",
  "earth_reboot_chat",
  "stuttgart_widerstand_demos",
  "internationalcoronanews",
  "infowellechat",
  "marieallin",
  "quicksatnet",
  "dieanderewahrheit",
  "join_platt_form_now",
  "einfachzumkotzen",
  "wissen",
  "folgedemplan",
  "liebeisstleben",
  "neustart_jetzt_gruppe",
  "einerfueralle_allefuereinen_chat",
  "contracoma",
  "diehelfendehandtalk",
  "aufwach",
  "werner_altnickel_info",
  "freier_informationskanal",
  "conspiracyfactstalk",
  "maskenfrei_zuerich",
  "gruppenkanaele",
  "q_d_r_area",
  "sonsofpatriots",
  "widerstand100",
  "libertetalk",
  "globalawakeningartchat",
  "verruecktesjahr202q",
  "trostinfo",
  "suefortruth",
  "mgshow",
  "drdaniellanghans",
  "donnerstein_chat",
  "wwg1wgachat",
  "demoterminechat",
  "we_r_free",
  "augenaufma",
  "wombels_kunst",
  "teamheimatgruppe",
  "derstrammegermanechat",
  "scharfschuetzenbewegung1",
  "fruehwaldinformiert",
  "verschwoerungspraktiker",
  "standpunktgequake",
  "erwache20",
  "paulapcay",
  "chatderfreiheit",
  "infokanalberlin_chat",
  "geheimnis_gesundheit",
  "erwachen2023",
  "patriotsandra",
  "patriotch",
  "vmfgruppenchat",
  "wir_holenunsere_freiheit_zurueck",
  "diewahrheitundnurdiewahrheit",
  "trick_siebzehn",
  "chiemseefeechat",
  "mstpatriotnrwchat",
  "disclosetv_chat",
  "talawolf",
  "qhammernews",
  "schaebelsblog",
  "kaiaushannover",
  "dt64infoampulsderzeit207",
  "chat_einerfueralle_allefuereinen",
  "futureunlimited",
  "gehlkenronald",
  "dt64infoproundcontra207",
  "gemeinsamschweizchat",
  "wahreoffenbarung",
  "karolineseibt",
  "friede_freiheit_demokratie_chat",
  "topnews_at_chat",
  "neustart_jetzt",
  "technicus_news",
  "aufwachen369",
  "widerstand81",
  "badenwuerttemberginfochat",
  "bestinfochat",
  "gesundheitdiskussion",
  "qdrops",
  "teamheimatchat",
  "aufklaerung2020",
  "gegennwochat",
  "qanalwwg1wga",
  "deutschetagesnews",
  "wie_bitte_echt_jetzt",
  "vollekannetrost",
  "derschwarzeritter",
  "nachrichtenohnezensur",
  "freyjasbulletininternationalchat",
  "freiheitschat2020",
  "aerztefueraufklaerung",
  "mindofheart",
  "huerdenflug_chat",
  "wiserwithkaiser",
  "andrerasv",
  "accepted4valuechat",
  "daserwachen2022",
  "q_d_r_army",
  "nixistwieesscheint",
  "bioapis",
  "augenaufaa",
  "chiemseefee",
  "defender2020kanal",
  "heinrichs_gedanken",
  "patriotnews",
  "conspiracyfactsdeutsch",
  "q17trump",
  "lichtanonsmensch",
  break-----------------------------
  "unzensiert",
  "checkmatenews",
  "truelife18",
  "faktenfriedenfreiheit",
  "freiemedientv",
  "expresszeitung",
  "oliverjanich",
  "wirsindvielmehr",
  "unblogd",
  "coronainformationskanal",
  "politische_bildersprueche",
  "kenjebsen",
  "frieden_rockt_offiziell",
  "kulturstudio",
  "evahermanoffiziell",
  "rabbitresearch",
  "uncut_news",
  "qlobalchange",
  "royalallemand",
  "fufmedia",
  "werbegruppe_deutschsprachig",
  "wissenistmacht1",
  "xavier_naidoo",
  "geheimeswissendereliten",
  "compactmagazin",
  "einmal_hin_alles_drin",
  "mh171702q2q",
  "attilahildmann",
  "lionmediatelegram",
  "aktivistmann",
  "haintz",
  "q_d_r_a",
  "globalpatriots",
  "nachrichtenportal",
  "qparadise",
  "bitteltv",
  "davebrych_public",
  "servusdeutschland",
  "allesaussermainstream",
  "haunsiappmann",
  "disclosetv",
  "epochtimesde",
  "antiilluminaten",
  "qwwg1wga16plus1",
  "nityatelegram",
  "videodump1",
  "klagemauertv",
  "samueleckert",
  "waldgangalbdruck",
  "doqusthreads",
  "freiesachsen",
  "reitschusterde",
  "demotermine",
  "we_r_q",
  "schubertslm",
  "freiheitdergedanken",
  "corona_fakten",
  "dawidsnowden",
  "markmobil",
  "alexander_ehrlich",
  "der17stammtisch",
  "ignazbearth",
  "reinerfuellmich",
  "spioniker",
  "frmawa",
  "ra_ludwig",
  "uncutnewsschweiz",
  "freeyourmindkanal",
  "neuzeitnachrichten",
  "martinsellnerib",
  "daniel_prinz_offiziell",
  "vivoterra",
  "kinder_schuetzen",
  "aerzte",
  "gwisnewski",
  "ddb_radio",
  "checkmatenewsgroup",
  "lknews2",
  "anonymousschweizorginal",
  "unzensiertkontaktbot",
  "sandragabriel269",
  "eltern_stehen_auf",
  "stuttgartgrundgesetzdemos",
  "nachrichtenwelt",
  "wim4u",
  "rasattelmaier",
  "oliverflesch",
  "valkuerer",
  "der_impulsgeber",
  "corona_ausschuss",
  "macklemachtgutelaune",
  "infoplatz",
  "newsostberlin",
  "corona_reset",
  "gerechtigkeitfuersvaterland",
  "klagepaten_eu",
  "q_faktor_germany",
  "coronavirushilfe",
  "tonitano",
  "tommyrobinsonnews",
  "schrangtv",
  "rt_de",
  "freiheitmachtwahr",
  "naomiseibt",
  "inakarb",
  "wochenblick",
  "absicherungnachwelt",
  "militaernews",
  "herzensmenschenunited",
  "legitimnews",
  "wirmachenauf_de",
  "gemeinsamgegennwo",
  "vaxxed_greatawakenig",
  "weissesarmband",
  "kilezmore",
  "cnconspiracynewsroom",
  "heimatgewaltfreivereint",
  "into_the_light_news",
  "connectivevents",
  "q_gold",
  "marioamenti",
  "bleibtstark",
  "rt_deutsch",
  "dr_heinrich_fiechtner",
  "sandysteen1",
  "fragunsdoch_wwg1wga",
  "donald_j_trump_q_family_germany",
  "kranztv",
  "miriamhope",
  "qpluswatnn",
  "rechtsanwaeltin_beate_bahner",
  "thueringer_widerstand",
  "stefanraven",
  "pankalla",
  "thueringer_widerstand_chat",
  "taufertshoefer",
  "durov",
  "aerztefueraufklaerungoffiziell",
  "buergerinformative",
  "weltdergesundheittv",
  "project_veritas",
  "q74you",
  "wahrheitstraeumer",
  "demotermine!",
  "holistischegesundheitheilung",
  "anons17",
  "ddddoffiziell",
  "globaleserwachen",
  "zehnmin",
  "qbavaria",
  "danielprinzoffiziell",
  "trumpcomesback",
  "vereinigtewahrheitsbewegung",
  "georgswzg",
  "peacecrowd",
  "jackdawkins",
  "digitalchronist",
  "police_frequency",
  "q_proofs",
  "notisolate",
  "ayse_meren_hp",
  "kampf_fuer_unsere_zukunft",
  "verbindediepunkte",
  "michaelwendlerofficial",
  "markus_lowien",
  "bitchbotboiilive",
  "verstehenhandeln",
  "saraslightfight",
  "meinednews",
  "rtintl",
  "stefanmagnet",
  "reitschusterdechat",
  "einerfueralle_allefuereinen",
  "derdeutschamerikaner",
  "timmkellner",
  "klartext2021gemeinsam",
  "digitalsoldiersgermanynews",
  "eingeschenkt",
  "qlobalchangeusa",
  "mstpatriotnrw",
  "wwg1wgaworldwide",
  "polizeigewalt",
  "translatedpressde",
  "bewussttv",
  "dokukiste",
  "fletchersvisionen",
  "mutflash",
  "billsix",
  "flacheerdegemeinschaft",
  "q_anonymous_kanal_deutschland",
  "mannmitbartarchiv",
  "news1g",
  "livestreamsfuerdich",
  "erwachen2021",
  "betterknownow",
  "kenfm",
  "coachcecil",
  "busfahrerthomas",
  "lionmediatv"
  lalalala
]'''


# altaltalt
''', 'ImpfGenozidKinder',
                 'querdenken215', 'querdenken381', 'querdenken_7171', 'querdenken8331', 'Maskenverbot',
                 'querdenken_911', 'querdenken511', 'corona', 'querdenken231', 'querdenken235', 'querdenken_791',
                 'querdenken_201', 'querdenken341_aktiv', 'MASKENFREI_ME', 'querdenken30', 'querdenken_775',
                 'querdenken215_aktiv', 'corona_infokanal_bmg', 'querdenken_334', 'querdenken911_aktiv',
                 'querdenken361', 'querdenken7141_aktiv', 'querdenken831', 'querdenken751', 'Pandemie1',
                 'querdenken6051_aktiv', 'querdenken238_aktiv', 'querdenken53', 'impfenchippenbargeldlos',
                 'QuerdenkenTV', 'querdenken7192_aktiv', 'querdenken_241', 'querdenken_231', 'querdenken453_aktiv',
                 'querdenken7451', 'querdenken5221', 'querdenken762_aktiv', 'querdenken_8341', 'querdenken615_aktiv',
                 'querdenken_571pw', 'querdenken_773', 'querdenken_235', 'querdenken203', 'querdenken228',
                 'querdenken201_aktiv', 'QUERDENKEN', 'querdenken242', 'querdenken242_aktiv', 'querdenken410',
                 'querdenken743', 'querdenken763', 'querdenken773_aktiv', 'querdenken351', 'querdenken_8331',
                 'querdenken_228', 'querdenken_861', 'querdenken8341', 'querdenken761', 'querdenken831_aktiv',
                 'querdenken7261', 'FakePandemie', 'querdenken615', 'Maske', 'QUERDENKEN_711', 'querdenken201',
                 'querdenken241_aktiv', 'querdenken_681', 'querdenken_793', 'coronavirus2020_kz', 'querdenken866_aktiv',
                 'GemeinsamMaskenfreiEinkaufen', 'querdenken_751', 'querdenken762', 'querdenken_242',
                 'impfenmussfreiwilligbleiben', 'querdenken_763', 'querdenken761_aktiv', 'querdenken763_aktiv',
                 'PandemieProdukte', 'querdenken234_aktiv', 'querdenken751_aktiv', 'querdenken_721', 'querdenken_615',
                 'querdenken_831', 'querdenken_571', 'querdenken791', 'querdenken453', 'MaskenfreiEinkaufenKanal',
                 'querdenken_351', 'querdenken6051', 'querdenken621', 'querdenken211_aktiv', 'querdenken381_aktiv',
                 'querdenken40_aktiv', 'querdenken7261_aktiv', 'querdenken8341_aktiv', 'querdenken_6201',
                 'querdenken_711', 'querdenken_794', 'cama_2Q2Q', 'querdenken361_aktiv', 'querdenken284_aktiv',
                 'querdenken211', 'impfenst', 'coronau', 'querdenken718', 'UKcoronavirusnews', 'querdenken7171',
                 'querdenken793_aktiv', 'querdenken841_aktiv', 'querdenken7192', 'querdenken_841', 'querdenken_713',
                 'querdenken_7261', 'querdenken_743', 'querdenken7551', 'querdenken571_aktiv', 'querdenken775_aktiv',
                 'querdenken702', 'querdenken_702', 'querdenken203_aktiv', 'querdenken5221_aktiv', 'querdenken2932',
                 'querdenken911', 'querdenken_441', 'querdenken30_aktiv', 'querdenken711', 'Nicht_impfenlassen',
                 'querdenken7171_aktiv', 'querdenken_761', 'querdenken775', 'querdenken234', 'querdenken841',
                 'querdenken238', 'querdenken_511', 'querdenken_5221', 'querdenken794_aktiv', 'querdenken228_aktiv',
                 'querdenken_284', 'querdenken_381', 'querdenken341', 'querdenken_453', 'querdenken69_aktiv',
                 'querdenken_238', 'querdenken861', 'querdenken_30', 'querdenken_621', 'querdenken791_aktiv',
                 'impfenhh', 'querdenken713', 'querdenken713_aktiv', 'querdenken_7141', 'Individuelle_Impfentscheidung',
                 'CoronaG', 'querdenken_866', 'fakepandemie1', 'Masken', 'querdenken711_aktiv', 'querdenken441_aktiv',
                 'querdenken_69', 'querdenken40', 'Impfen', 'querdenken69', 'querdenken_215', 'querdenken_341',
                 'querdenken793', 'querdenken_203', 'querdenken_718', 'wir_lassen_uns_nicht_impfen', 'querdenken_361',
                 'corona0', 'querdenken_2932', 'querdenken7551_aktiv', 'querdenken773', 'querdenken410_aktiv',
                 'querdenken6201', 'oliverjanich', 'querdenken334_aktiv', 'querdenken721', 'querdenken794',
                 'querdenken_40', 'querdenken681', 'querdenken_410', 'MyGovCoronaNewsdesk', 'CoronaOberlausitz',
                 'spcoronavirus', 'querdenken2932_aktiv', 'querdenken_7451', 'impfen_nein_danke', 'querdenken7141',
                 'querdenken_762', 'querdenken235_aktiv', 'querdenken6201_aktiv', 'fortschrittliche_corona_infos',
                 'querdenken441', 'querdenken571pw', 'querdenken866', 'querdenken718_aktiv', 'querdenken_53',
                 'querdenken53_aktiv', 'maskel', 'querdenken743_aktiv', 'WirStehenAuf', 'Corona_Fakten',
                 'querdenken_7551', 'querdenken861_aktiv', 'querdenken_234', 'querdenken702_aktiv',
                 'querdenken231_aktiv', 'querdenken721_aktiv', 'querdenken511_aktiv', 'querdenken8331_aktiv',
                 'maskenfreie_kids', 'querdenken334', 'querdenken284', 'querdenken681_aktiv', 'querdenken7451_aktiv',
                 'querdenken_7192', 'querdenken571pw_aktiv', 'Pandemie', 'querdenken571', 'querdenken_211',
                 'reitschusterde']'''

scraper.scrape(seed_channels)
