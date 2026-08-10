# Home Assistant HEMS

An advanced Home Energy Management System for Home Assistant using a
Brain-and-Workers architecture.

This reference implementation coordinates:

- a Tesla Powerwall 2;
- a SolarEdge inverter and export limit;
- a SolarEdge EV charger;
- a BYD Atto 3;
- Amber Electric live and forecast prices; and
- Solcast solar forecasts.

> **Release status: alpha / commissioning reference.**
>
> The system has performed successful live control, but commissioning and
> hardware-specific validation are still in progress. Do not enable hardware
> Workers until every entity mapping and test scenario has been verified on
> your installation.

## Design principles

1. Real integrations feed effective sensors.
2. Test overrides affect effective sensors only—not live integration entities.
3. The Brain calculates desired outcomes and never controls hardware directly.
4. Workers compare desired state with actual state before issuing one command.
5. Manual override always wins.
6. Command guards prevent repeated Start, Stop, or mode commands.
7. Guardians report mismatches without independently fighting Workers.

## Repository layout

- `docs/` — architecture, installation, safety and entity-mapping guidance.
- `templates/` — Home Assistant template sensor state templates.
- `automations/` — complete UI-YAML automation replacements.
- `packages/` — package-based sensors/helpers where appropriate.
- `dashboards/` — Lovelace dashboard examples.
- `examples/` — example mapping and configuration files.
- `tools/` — offline YAML/Jinja validation used by CI.

## Important installation warning

This project contains installation-specific entity IDs. The public release uses
clearly documented mapping points; do not paste control automations unchanged
until you have mapped and tested every entity listed in
`docs/entity-mapping.md`.

Create the required helpers from [`docs/helpers.md`](docs/helpers.md) before
installing any automation. Keep all three hardware Workers disabled until the
read-only sensors and test platform have been commissioned.

## Current scope

- Powerwall target and cheap-grid coordination
- EV urgent recovery, approved recovery and target charging
- Powerwall/EV interlock and durable command guards
- negative-feed-in solar curtailment with minimum hold periods
- cloudy-day grid-price approval
- Amber advanced price forecasting
- Solcast forecast snapshots and forecast learning
- financial tracking, energy attribution and estimated system savings
- daily performance summaries, critical-data checks and Worker health reporting
- rolling 7/30-day solar-forecast and overnight-usage learning
- commissioning and visual energy-flow dashboards

## Optional observation package

[`packages/observability_learning.yaml`](packages/observability_learning.yaml)
adds read-only reliability, data-quality, forecast-learning, overnight-learning
and savings-confidence entities. It also records one daily snapshot and creates
one Home Assistant persistent notification. It never calls a hardware-control
service. The `Intelligence` view in
[`dashboards/energy_flow.yaml`](dashboards/energy_flow.yaml) displays these
entities.

## Privacy boundary

This repository is built from a separate private commissioning workspace. Home
Assistant backups, recorder databases, `.storage`, secrets, access tokens,
addresses, screenshots and personal traces are intentionally excluded. Never
replace this repository with a raw Home Assistant backup.
