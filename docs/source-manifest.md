# Canonical source manifest

This manifest prevents obsolete commissioning iterations from being published.
Only the listed current files are candidates for the first alpha release.

## Workers and control automations

- EV Worker: `HEMS_EV_Worker_UI_Full_Replacement_2026-07-23.yaml`
  - internally revised 31 July 2026
- EV command guard: dated state-template version, internally revised 29 July
  with durable Worker-owned running sessions
- Powerwall Worker: `HEMS_Powerwall_Worker_2026-07-22.yaml`
- Solar Worker: `HEMS_Solar_Worker_30_Minute_Hold_UI_Full_Replacement_2026-07-26.yaml`
- Financial Worker: `financial_worker.yaml`
- EV 30–50% decision: `HEMS_EV_30_50_Charge_Choice_UI_Full_Replacement_2026-07-23.yaml`
- EV departure/return planner: `HEMS_EV_Departure_Return_Planner_UI_Full_Replacement_2026-07-23.yaml`
- EV commitment reset: `HEMS_EV_Charge_Commitment_Reset_UI_Full_Replacement_2026-07-23.yaml`
- EV Powerwall hold latch: `HEMS_EV_Powerwall_Hold_Latch_UI_Full_Replacement_2026-07-23.yaml`
- Charging deadline warning: `charging_deadline_warning.yaml`
- Morning plug-in reminder: `BYD_Morning_Plug_In_Reminder_UI_Full_Replacement_2026-07-23.yaml`
- Cloudy-day approval: `HEMS_Cloudy_Day_Grid_Charge_Approval_Full_Automation_2026-07-29.yaml`
- Amber forecast cache: `amber_advanced_forecast_cache.yaml`
- Solar morning snapshot: `solar_morning_forecast_snapshot.yaml`
- Overnight start/end: the two `HEMS_Record_Overnight_*_2026-07-26.yaml` files

## Current templates

- charging deadline feasibility
- cheapest visible price and cheap-grid minutes
- coordinated Powerwall mode and reserve
- effective EV SOC and effective grid-charge price limit
- EV permission, projected SOC, energy required, grid window and target
- EV Powerwall interlock request/status and hold reserve
- EV Worker command guard and EV guardian
- expected EV action and expected Powerwall mode
- genuine excess solar
- Powerwall guardian
- Solar guardian with 30-minute hold

Where a dated and undated version coexist, the dated version named by the latest
installation note wins. The obsolete copy is not included.

## Packages and dashboards

- `HEMS_Energy_Attribution_Package_2026-07-30.yaml`
- `HEMS_System_Savings_Package_2026-07-30.yaml`
- `HEMS_Energy_Flow_Dashboard_Full_YAML_2026-07-28.yaml`
- `HEMS_Selectable_Energy_Explorer_Full_YAML_2026-07-30.yaml`

## Explicit exclusions

- all Home Assistant backup archives and extracted backup content;
- recorder databases, Solcast caches and `.storage` data;
- screenshots, videos, traces and personal commissioning notes;
- superseded automation iterations;
- local Codex-to-Home-Assistant tokens and connection tooling;
- unrelated household-intelligence files and integrations.
