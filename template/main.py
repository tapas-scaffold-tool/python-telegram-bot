from {{ name }}_bot.app import {{ name_pascal_case }}BotApp


if __name__ == "__main__":
    exit({{ name_pascal_case }}BotApp().main())
