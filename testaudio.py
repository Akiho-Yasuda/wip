curl -X POST \
--data-binary @'audio/kakita.wav' \
--header 'Content-Type: audio/l16; rate=16000;' \
'https://www.google.com/speech-api/v2/recognize?output=json&lang=en-us&key=<AIzaSyB4uC8ZsBbnWCHD8yZ-lBE-DoT-do86jmw>'
