# Greenhouse monitor for my dad's tomato obsession

My dad has a small backyard greenhouse and overwaters everything because
he "feels it might be dry." I want a small IoT sensor array that just
tells him, on his phone, whether to water today. No fancy automation —
just data + a recommendation.

Hardware:
- ESP32 with deep-sleep (battery powered, solar trickle)
- Soil moisture sensor (capacitive, not resistive — those corrode)
- Air temp + humidity (DHT22 or BME280)
- Optional: light sensor for daylight hours

Cloud/firmware features:
- Firmware in MicroPython (I know it; my dad sometimes wants to tinker)
- MQTT over TLS to a hosted broker (HiveMQ cloud free tier?)
- A backend that ingests readings and stores in TimescaleDB
- A simple PWA showing: current state + "water today: yes/no" + 7-day chart
- Push notification at 7am if action needed

Constraints:
- Must survive a Mediterranean summer (50°C inside the greenhouse)
- Total BOM under $40
- Setup: must be doable by my dad (who is 68) without me on site
- Privacy: data stays in EU region

Risks:
- Risk: capacitive sensors drift over months — need calibration UX
- Risk: WiFi range from greenhouse to house might be marginal
- Concern: condensation killing the board. Conformal coating needed?

Unknowns:
- Best way to handle multi-zone (he might want 3 sensors eventually)?
- Should the "water today" rule live on device or in cloud?
- TLS on ESP32 + deep sleep — is the handshake cost killing battery?
