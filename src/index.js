/** Author: Perry Gowdy
    Application: Pathfinder Spellbook for Amazon echo
    Description: This AlexaSkill developed for the Amazon echo allows users to
    access the Pathfinder Rulebook to look up spells. The application is used
    by asking Alexa to look up a spell from Pathfinder.


    Examples:
    One-shot model:
        User: "Alexa, ask Spellbook to look up Fireball"
        Alexa: "A fireball spell generates a searing explosion of flame that
         detonates with a low roar and deals 1d6 points of
         fire damage per caster level (maximum 10d6) to every creature
         within the area. Unattended objects also take this damage.
         The explosion creates almost no pressure."

         User: "Alexa, Spellbook Magic Missile"
         Alexa: "A missile of magical energy darts forth from your fingertip
         and strikes its target, dealing 1d4+1 points of force damage."

    Copyright 2017 Perry Gowdy or his affiliates. All Rights Reserved.

*/


var APP_ID = undefined; //TODO replace with 'amzn1.echo-sdk-ams.app.[MY UNIQUE ID]'

var AlexaSkill = require('./AlexaSkill');

var Spellbook = function() {
  AlexaSkill.call(this, APP_ID)
}

//Extend AlexaSkill
Spellbook.prototype = Object.create(AlexaSkill.prototype);
Spellbook.prototype.constructor = Spellbook;

//------------------------ Override AlexaSkill request and intent handlers -------------------------

Spellbook.prototype.eventHandlers.onSessionStarted = function(sessionStartedRequest, session) {
  console.log("onSessionStarted requestID: " + sessionStartedRequest.requestId
    + ", sessionId: " + session.sessionId);
    //any initilization logic goes here
};

Spellbook.prototype.eventHandlers.onLaunch = function(launchRequest, session, response) {
  console.log("launchRequest requestID :" + launchRequest.requestId
    + ", sessionId: " + session.SessionId);
  handleWelcomeRequest(response);
}

Spellbook.prototype.eventHandlers.onSessionEnded = function(sessionEndedRequest, session) {
  console.log("OnSessionEnded requestId: " + sessionEndedRequest.requestId
    + ", sessionId: " + session.sessionId);
};

/**
*   Override intentHandlers to map intent handling functions
*/

Spellbook.prototype.intentHandlers = {
    "OneshotSpellbook": function(intent, session, response) {
        handleOneshotSpellbookRequest(intent, session, resonse);
    }
};

function handleWelcomeRequest(response) {
  var whichSpellPrompt = "Which spell would you like to look up?",
    speechOutput = {
      speech: "<speak>Welcome to the Pathfinder Spellbook. "
        + whichSpellPrompt
        + <"/speak">,
      type: AlexaSkill.speechOutputType.SSML
    },
    repromptOutput = {
      speech: "I can lead you through looking up a spell "
        + "or you can open Spellbook and ask a question like, "
        + "look up spell Fireball. "
        + whichSpellPrompt,
      type: AlexaSkill.speechOutputType.PLAIN_TEXT
    };

  response.ask(speechOutput, repromptOutput);
}

function handleOneshotSpellbookRequest (intent, session, response) {

    //Determine spell
    var spellToFind = getSpellFromIntent(intent, true),
      repromptText,
      speechOutput;

    if(spellToFind.error) {
        rempromptText = "I cannot find that spell in the Spellbook. Try again "
          + "or try a different spell.";

        speechOutput = "I'm sorry, I can't find that spell. ";

        response.ask(speechOutput.repromptText);
        return;
    }

    //all slots filled. Move to final request
    getFinalSpellbookResponse(spellToFind, response);
}
