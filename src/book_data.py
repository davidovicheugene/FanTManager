class CatalogSection:
    """Catalog section selection by CSS Selector implementation"""

    class Novels:
        class FanficsTranslations:
            NARUTO = "#n40 > a"
            ONE_PIECE = "#n41 > a"
            BLICH = "#n42 > a"
            MARVEL = "#n43 > a"
            HARRY_POTER = "#n52 > a"

        class Machine:
            CHINESE = "#n45 > a"
            JAPANESE = "#n46 > a"
            KOREAN = "#n47 > a"
            ENGLISH = "#n48 > a"
            VIETNAMESE = "#n49 > a"

        CHINESE = "#n5 > a"
        KOREAN = "#n7 > a"
        JAPANESE = "#n6 > a"
        ENGLISH = "#n28 > a"
        VIETNAMESE = "#n39 > a"
        COPYRIGHT = "#n18 > a"
        COPYRIGHT_FANFS = "#n51 > a"
        FOR_ADULTS = "#n50 > a"
        MACHINE = "#n44 > a"

    SKIP = "body > div:nth-child(4) > div:nth-child(3) > div > div > a"


class NovelSettingsSelectors:
    class OriginalLang:
        # English by default
        SELECT_ = "#Book_s_lang"
        ENGLISH = "#Book_s_lang > optgroup:nth-child(1) > option:nth-child(1)"
        CHINESE = "#Book_s_lang > optgroup:nth-child(1) > option:nth-child(2)"
        KOREAN = "#Book_s_lang > optgroup:nth-child(1) > option:nth-child(3)"
        RUSSIAN = "#Book_s_lang > optgroup:nth-child(1) > option:nth-child(4)"
        JAPANESE = "#Book_s_lang > optgroup:nth-child(1) > option:nth-child(5)"
        DEFAULT = ENGLISH

    class TranslationLang:
        # Russian by default
        SELECT_ = "#Book_t_lang"
        ENGLISH = "#Book_t_lang > optgroup:nth-child(1) > option:nth-child(1)"
        CHINESE = "#Book_t_lang > optgroup:nth-child(1) > option:nth-child(2)"
        KOREAN = "#Book_t_lang > optgroup:nth-child(1) > option:nth-child(3)"
        RUSSIAN = "#Book_t_lang > optgroup:nth-child(1) > option:nth-child(4)"
        JAPANESE = "#Book_t_lang > optgroup:nth-child(1) > option:nth-child(5)"
        DEFAULT = RUSSIAN

    class OriginalPubStatus:
        SELECT_ = "#Book_team"
        BLANK = "#Book_team > option:nth-child(1)"
        ONGOING = "#Book_team > option:nth-child(2)"
        ENDED = "#Book_team > option:nth-child(3)"
        ABANDONED = "#Book_team > option:nth-child(4)"

    class NovelTheme:
        SELECT_ = "#book_atmosphere"
        BLANK = "#book_atmosphere > option:nth-child(1)"
        LIGHT = "#book_atmosphere > option:nth-child(2)"
        DARK = "#book_atmosphere > option:nth-child(3)"

    class TranslationStatus:
        SELECT_ = "#Book_wealth"
        IN_PROGRESS = "#Book_wealth > option:nth-child(1)"
        DONE = "#Book_wealth > option:nth-child(2)"
        TIMEOUT = "#Book_wealth > option:nth-child(3)"
        WAITING = "#Book_wealth > option:nth-child(4)"
        DECLINED = "#Book_wealth > option:nth-child(5)"

    class VoiceoverGender:
        SELECT_ = "#Book_audible_voice"
        MALE = "#Book_audible_voice > option:nth-child(1)"
        FEMALE = "#Book_audible_voice > option:nth-child(2)"


class Novel:
    catalog_section = CatalogSection.SKIP  # skips catalog section choice
    # Basic information
    original_lang = NovelSettingsSelectors.OriginalLang.DEFAULT
    original_title = ""
    translation_lang = NovelSettingsSelectors.TranslationLang.DEFAULT
    translation_title = ""
    author = ""
    novelupdates_link = ""
    webnovel_link = ""
    publication_year = 0
    total_chapters = 0
    alternative_title_1 = ""
    alternative_title_2 = ""
    alternative_title_3 = ""
    b_download_access = True

    # Description
    original_pub_status = NovelSettingsSelectors.OriginalPubStatus.BLANK
    description = ""
    # genres =
    # tags =
    # fandoms =
    b_is_adult = False
    theme = NovelSettingsSelectors.NovelTheme.BLANK
    notes = ""
    image_path = ""
    image_url = ""
    adds_images = []

    # Subscription
    chapter_price = 0
    chapter_audio_price = 0
    discount = 0
    subscription_1 = [10, (chapter_price * 10) - chapter_price]
    subscription_2 = [20, (chapter_price * 20) - (chapter_price * 3)]
    subscription_3 = [50, (chapter_price * 50) - (chapter_price * 5)]
    disable_subs_at_sale = False

    # Team and chapter publication
    # team // NONE by default //
    # сделать позже считывание доступных команд и их выгрузку в файл, оттуда же и чтение для выбора
    vk_group_link = ""
    telegram_chanel_link = ""
    translation_status = NovelSettingsSelectors.TranslationStatus.IN_PROGRESS
    comment = ""
    b_is_copyright = False
    b_display_frequency = True
    subs_take_off = []
    b_auto_sub_take_off = False
    b_auto_add_chapters = False
    chapter_pub_delay = []
    b_notify_new_comments = True
    b_show_raising_progress = False
    b_take_text_mistakes = True

    # Auto voiceover
    b_auto_voiceover = True
    auto_voiceover_gender = NovelSettingsSelectors.VoiceoverGender.MALE
