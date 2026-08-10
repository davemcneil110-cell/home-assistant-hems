# Changelog

## 0.2.0-alpha - 2026-08-10

- Added an optional observation-only learning and reliability package.
- Added the Energy Flow dashboard Intelligence view.
- Added daily forecast-error snapshots, rolling overnight usage and savings-confidence reporting.
- Expanded EV charge decisions above 30% SOC and refined return planning,
  commitment resets and deadline warnings.
- Added EV Worker restart recovery so stale restored command helpers cannot
  block a new session after Home Assistant restarts.
- Removed the EV Worker's dependency on the legacy charging-availability
  sensor when claiming a new guarded session.
- Improved energy attribution and system-savings dashboard reporting.

## 0.1.0-alpha

Initial public commissioning reference release.

- Brain-and-Worker Home Assistant architecture.
- Tesla Powerwall, SolarEdge inverter/EV charger, BYD EV, Amber Electric and
  Solcast-oriented reference configuration.
- Guarded Powerwall, EV and Solar control workers.
- Test-effective sensor layer for controlled commissioning.
- Energy attribution, savings and dashboard examples.

This is an alpha release. Entity mapping and staged commissioning are required
before hardware control is enabled.
