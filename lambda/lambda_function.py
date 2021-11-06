# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

# custom modules
import adelphi_news

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome, to navigate adelphi news, use the following commands:\n1. recent headlines. \n2. articles by category. \n3. menu. \n4. read 'article title'. \n5. stop/cancel."
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class RecentHeadlinesIntentHandler(AbstractRequestHandler):
    """Hanlder for Recent Headlines Intent"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("RecentHeadlinesIntent")(handler_input)
        
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The most recent headlines are the following: \n"
        
        # Adelphi news lists with title, date, body and category
        titles = adelphi_news.titles
        
        for i in range(4):
            speak_output += titles[i] + ", "
        
        speak_output += ". Would you like to see more articles?"
        
        
        return(
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )


class ViewMoreHeadlinesIntentHandler(AbstractRequestHandler):
    """Handler for View More Headlines"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ViewMoreHeadlinesIntent")(handler_input)
        
    def handle(self, handler_input):
        # type: (HanlderInput) -> Response
        speak_output = "More headlines:\n"
        
        titles = adelphi_news.titles
        
        for i in range(5, 9):
            speak_output += titles[i] + ", "
        
        speak_output += ". Which title would you like to read?"
        
        return(
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )


class TitleRequestIntentHandler(AbstractRequestHandler):
    """Hanlder for Title Request Intent"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TitleRequestIntent")(handler_input)
    
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        title = slots["title"].value
        
        #articles = adelphi_news.articles
        titles = adelphi_news.titles
        bodies = adelphi_news.bodies
        
        speak_output = ""
        
        for i in range(len(titles)):
            if title in titles[i]:
                speak_output = bodies[i] + ".\nWhat other article would you like to hear?"
            else:
                speak_output = f"Sorry, we couldn't find {title}, try again"
        
        return(
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
            )


class ViewCategoriesIntentHandler(AbstractRequestHandler):
    """Handler for View Articles Categories Intent"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ViewCategoriesIntent")(handler_input)
        
    def handle(self, handler_input):
        # type: (HanlderInput) -> Response
        speak_output = "The categories are the following: "
        
        unique_categories = adelphi_news.unique_categories
        
        for category in range(5):
            speak_output += category + ", "


        speak_output += ". Which category would you like to see?"
        
        return(
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )
    

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Here are the options:\n1. recent headlines. \n2. articles categories \n3. menu. \n4. read 'article title'. \n5. stop/cancel"

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )




class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Closing adelphi news!, goodbye"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

# Custom intents
sb.add_request_handler(RecentHeadlinesIntentHandler())
sb.add_request_handler(TitleRequestIntentHandler())
sb.add_request_handler(ViewMoreHeadlinesIntentHandler())
sb.add_request_handler(ViewCategoriesIntentHandler())

# make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers
sb.add_request_handler(IntentReflectorHandler()) 


sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()