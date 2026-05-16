# RISKS — Greenhouse monitor for my dad's tomato obsession

## Known risks

- Risk: capacitive sensors drift over months — need calibration UX
- Risk: WiFi range from greenhouse to house might be marginal
- Concern: condensation killing the board. Conformal coating needed?

## Open questions / unknowns

- MQTT over TLS to a hosted broker (HiveMQ cloud free tier?)
- Best way to handle multi-zone (he might want 3 sensors eventually)?
- Should the "water today" rule live on device or in cloud?
- TLS on ESP32 + deep sleep — is the handshake cost killing battery?
- - Concern: condensation killing the board. Conformal coating needed?
- - Best way to handle multi-zone (he might want 3 sensors eventually)?
- - Should the "water today" rule live on device or in cloud?
- - TLS on ESP32 + deep sleep — is the handshake cost killing battery?

## Constraints

- Must survive a Mediterranean summer (50°C inside the greenhouse)
- Setup: must be doable by my dad (who is 68) without me on site

## Decisions to make this week

- [ ] Confirm primary user persona
- [ ] Lock in tech stack (or commit to a 2-day spike)
- [ ] Define what's explicitly **out of scope** for v0.1
