# MQTT Notarization Demo (de)
Ein n8n Workflow, der die Notarisierung von Sensordaten zeigt. 
Ein MQTT Trigger überwacht Messwerte ("hacb/random/sensors/#"), die auf einem MQTT Server einlangen. Mit diesen wird eine Json Datenstruktur zusammengestellt und daraus ein DatNoS-Request generiert.
Dieser wird in (eine Testinstanz) einer DatNosS-Blockchain gesendet und damit in eine Transaktion eingetragen und notarisiert. Der DatNoS-Request und das Ergebnis des API-Calls werden auf einem Log-Server protokolliert.


# MQTT Notarization Demo (en)
An n8n workflow demonstrating the notarization of sensor data.
An MQTT trigger monitors measured values ​​("hacb/random/sensors/#") arriving on an MQTT server. These values ​​are compiled into a JSON data structure and used to generate a DatNoS request.
This request is sent to (a test instance of) a DatNoS blockchain, where it is entered into a transaction and notarized. The DatNoS request and the result of the API call are logged on a log server.
