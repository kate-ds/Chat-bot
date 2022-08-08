from environs import Env

env = Env()
env.read_env()

telegram_token = env.str("API_TOKEN")
weather_token = env.str("WEATHER_API_TOKEN")
kinopoisk_token = env.str("KINOPOISK_TOKEN")
dialogflow_project_id = env.str("DIALOGFLOW_PROJECT_ID")
dialogflow_lang_code = env.str("DIALOGFLOW_LANGUAGE_CODE")
dialogflow_session_id = env.str("SESSION_ID")
