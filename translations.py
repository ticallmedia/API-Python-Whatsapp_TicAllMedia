MESSAGES = {
    "es":{
        "welcome_initial": "👋😊!Hola¡ Bienvenido a TicAll Media. Por favor selecciona tu idioma preferido",
        "lang_prompt": "Por favor, elige tu idioma: 👆 \n",
        "selected_language": "👌!Idioma configurado en Español¡. ",
        "invalid_option": "Opción no válida. Por favor, selecciona. ",
        "default_response": "¿En qué puedo ayudarte?",
        "change_language": "Claro, ¿a que Idioma te gustaría cambiar?. ", 
        "greeting_text": "¡Saludos! 🤖 ¿Intrigado por una estrategia de marketing más inteligente?\n\n En TicAll Media, tenemos ideas que podrían sorprenderte.\n\n¿Te animas a explorar?",
        "job": "💼 ¿En que industria te desempeñas?", 
        "advice": "🧐¿Buscas asesoría sobre algún servicio especial? "
    },
    "en": {
        "welcome_initial": "👋😊Hello! Welcome to TicAll Media. Please select your preferred language.",
        "lang_prompt": "Please choose your language: 👆 \n",
        "selected_language": "👌Language set to English.",
        "invalid_option": "Invalid option. Please select.",
        "default_response": "How can I help you?",
        "change_language": "Sure, which language would you like to change to?",
        "greeting_text": "Greetings! 🤖 Intrigued by a smarter marketing strategy? At TicAll Media, we have ideas that might surprise you. Are you ready to explore? ",
        "job": "💼 What industry do you work in?", 
        "advice": "🧐You are looking for advice on a special service? "
    }
}

def get_message(lang,key):
    """
    Obtine el mensaje traducido leyendo el diccionario MESSAGE
    lang: 'en' para inglés, 'es' para español
    key: la clave del mensaje ('welcome_initial','selected_language)    
    """
    #Sí el idioma no existe o no se elige por defecto sera ingles
    return MESSAGES.get(lang, MESSAGES["en"]).get(key,MESSAGES["en"][key])
