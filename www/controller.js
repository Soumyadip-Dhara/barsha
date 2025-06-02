$(document).ready(function () {


    //Display speak message
    eel.expose(displaySpeakMessage);
    function displaySpeakMessage(message) {
        $('.siri-message li:first').text(message);
        $('.siri-message').textillate('start');

    }

    //Display hood
    eel.expose(displayHood);
    function displayHood() {
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
    }
});