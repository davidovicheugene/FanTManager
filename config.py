from book_data import CatalogSection, NovelSettingsSelectors, Novel

# Functions settings
EC_wait_secs = 2

prelogin_rulate_url = "https://tl.rulate.ru/site/about"

rulate_profiles_ids = {"Honyaku_Hajime": 407401,
                       }

# TEST CONFIG

# Testing auth config
t_auth_username = "Honyaku_Hajime"


# Novel creation test config
n = Novel()
n.catalog_section = CatalogSection.SKIP  # skips catalog section choice
# Basic information
n.original_lang = NovelSettingsSelectors.OriginalLang.CHINESE
n.original_title = "I’M SORRY FOR GETTING A HEAD START BUT I DECIDED TO LIVE EVERYDAY EROTICALLY"
n.translation_lang = NovelSettingsSelectors.TranslationLang.DEFAULT
n.translation_title = "ПРОСТИТЕ, ЧТО Я ЗАБЕГАЮ ВПЕРЕД, НО Я РЕШИЛА ЖИТЬ КАЖДЫЙ ДЕНЬ ЭРОТИЧНО"
n.author = "Sasaki Kazu"
n.novelupdates_link = ""
n.webnovel_link = ""
n.publication_year = 2021
n.total_chapters = 156
n.alternative_title_1 = "I’m Sorry for Getting a Head Start but I Decided to Live Everyday Erotically"
n.alternative_title_2 = "Простите за то, что я не успела, но я решила жить каждый день эротично"
n.alternative_title_3 = ""
n.b_download_access = False
# Description
n.original_pub_status = NovelSettingsSelectors.OriginalPubStatus.ONGOING
n.description = """Я учусь в старшей школе на втором курсе и состою в клубе "Исследования человеческой культуры".
В клуб вступила красивая студентка-переводчица Мия Курусу.
У Курусу была идеальная внешность и характер.
Конечно же, все парни в клубе были очарованы Курусу.
Так или иначе, они отчаянно пытались сблизиться с ней.
По странному стечению обстоятельств я обошел их, чтобы приблизиться к ней.
После этого меня ждали ослепительно эротичные дни."""
# genres =
# tags =
# fandoms =
n.b_is_adult = True
n.theme = NovelSettingsSelectors.NovelTheme.LIGHT
n.notes = ""
n.image_path = ""
n.image_url = "https://novelbin.com/media/novel/im-sorry-for-getting-a-head-start-but-i-decided-to-live-everyday-erotically.jpg"
n.adds_images = []
# Subscription
n.chapter_price = 5
n.chapter_audio_price = 3
n.discount = 10  # percents
n.subscription_1 = [10, (n.chapter_price * 10) - n.chapter_price]
n.subscription_2 = [20, (n.chapter_price * 20) - (n.chapter_price * 3)]
n.subscription_3 = [50, (n.chapter_price * 50) - (n.chapter_price * 5)]
n.disable_subs_at_sale = True
# Team and chapter publication
# team // NONE by default //
# сделать позже считывание доступных команд и их выгрузку в файл, оттуда же и чтение для выбора
n.vk_group_link = "https://vk.com/labelcom"
n.telegram_chanel_link = "https://t.me/asafevstas"
n.translation_status = NovelSettingsSelectors.TranslationStatus.IN_PROGRESS
n.comment = ""
n.b_is_copyright = False
n.b_display_frequency = False
n.subs_take_off = [1, 2, 20]
n.b_auto_sub_take_off = False
n.b_auto_add_chapters = False
n.chapter_pub_delay = [1, 5, 12]
n.b_notify_new_comments = True
n.b_show_raising_progress = False
n.b_take_text_mistakes = True
# Auto voiceover
n.b_auto_voiceover = True
n.auto_voiceover_gender = NovelSettingsSelectors.VoiceoverGender.FEMALE
