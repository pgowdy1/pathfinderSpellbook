


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
  console.log("onSessionStarted requestID: " + sessionStartedRequest.requestID
    + ", sessionId: " + session.sessionId);
    //any initilization logic goes here
};
