# Helper inventory

Create these helpers before installing the control automations. Preserve the
entity IDs exactly; friendly names may be changed. The ranges below are safe
reference ranges, not electrical ratings. Verify every operating value for the
target installation.

The helpers created by `packages/energy_attribution.yaml` and
`packages/system_savings.yaml` are listed separately at the end and should not
be duplicated in the UI.

## Control and approval booleans

| Entity ID | Initial | Purpose |
|---|---:|---|
| `input_boolean.automatic_grid_charging_enabled` | off | Master permission for automatic grid charging |
| `input_boolean.enable_ev_automation` | off | EV Worker hardware-control permission |
| `input_boolean.ev_expected_back_today` | off | Keeps a returning EV in today's plan |
| `input_boolean.hems_ev_long_drive_today` | off | Raises today's EV target to 100% |
| `input_boolean.hems_ev_manual_override` | off | Blocks EV Worker commands |
| `input_boolean.hems_ev_recovery_approved` | off | Approval for an optional recovery charge |
| `input_boolean.hems_ev_urgent_charge_active` | off | Durable EV urgent-recovery state |
| `input_boolean.hems_ev_worker_session_active` | off | Worker-owned EV session latch |
| `input_boolean.hems_powerwall_manual_override` | off | Blocks Powerwall Worker commands |
| `input_boolean.hems_simultaneous_grid_charging_allowed` | on | Allows EV and Powerwall grid charging together |
| `input_boolean.hems_solar_automatic_control_enabled` | off | Solar Worker hardware-control permission |
| `input_boolean.hems_solar_manual_override` | off | Blocks Solar Worker commands |
| `input_boolean.byd_morning_reminder_sent` | off | Daily plug-in reminder de-duplication |

## Test booleans

All test helpers must be **off** outside commissioning.

| Entity ID | Initial |
|---|---:|
| `input_boolean.hems_test_mode` | off |
| `input_boolean.hems_test_battery_export` | off |
| `input_boolean.hems_test_ev_away` | off |
| `input_boolean.hems_test_ev_home_plugged_low_soc` | off |
| `input_boolean.hems_test_negative_feed_in` | off |
| `input_boolean.hems_test_powerwall_low` | off |
| `input_boolean.hems_test_solar_finished` | off |

## Operating numbers

| Entity ID | Unit | Reference initial value | Suggested range / step |
|---|---|---:|---|
| `input_number.maximum_grid_charge` | currency/kWh | 0.10 | -1 to 10 / 0.01 |
| `input_number.cloudy_day_grid_price` | currency/kWh | 0.20 | -1 to 10 / 0.01 |
| `input_number.ev_target` | % | 80 | 50 to 100 / 1 |
| `input_number.powerwall_target` | % | 80 | 20 to 100 / 1 |
| `input_number.minimum_power_reserve` | % | 20 | 0 to 100 / 1 |
| `input_number.maximum_solar_export` | W | 5000 | use the site-approved range / 100 |
| `input_number.hems_solar_minimum_export_limit` | W | 100 | use the inverter-approved range / 100 |
| `input_number.hems_ev_planning_charge_power` | kW | 6.5 | 0 to charger rating / 0.1 |
| `input_number.hems_powerwall_planning_charge_power` | kW | 5.0 | 0 to battery rating / 0.1 |
| `input_number.hems_test_ev_soc` | % | 60 | 0 to 100 / 1 |
| `input_number.hems_ev_session_start_powerwall_soc` | % | 20 | 0 to 100 / 1 |

The following numeric helpers are written by automations. Give them ranges
large enough for the installation and do not use their values as electrical
limits:

- `input_number.hems_advanced_cheap_grid_minutes_before_target` — minutes,
  initial `0`, suggested range `0–1440`;
- `input_number.hems_advanced_cheapest_visible_import_price` — currency/kWh,
  initial `0`, suggested range `-1–10`;
- `input_number.hems_export_credit_today`, `hems_import_cost_today`,
  `hems_net_cost_today` — currency, initial `0`, suggested range
  `-10000–10000`;
- `input_number.hems_last_grid_export`, `hems_last_grid_import` — cumulative
  source readings in kWh; size the maximum above the source meter lifetime;
- `input_number.hems_overnight_start_house_energy`,
  `hems_overnight_start_powerwall`, `hems_overnight_end_powerwall`,
  `hems_overnight_usage`, `hems_overnight_usage_average` — kWh or percent as
  indicated by the friendly name, initial `0`, suggested maximum `200`;
- `input_number.hems_overnight_usage_sample_count` — count, initial `0`,
  suggested maximum `10000`;
- `input_number.hems_solar_morning_forecast_central` and
  `input_number.hems_solar_morning_forecast_conservative` — kWh, initial `0`,
  suggested range `0–200`.

## Dropdown helpers

Create options exactly as shown and in the same letter case.

### `input_select.hems_ev_worker_command_state`

Initial: `idle`

```text
idle
start_pending
running
stop_pending
cooldown
interlock_lost_waiting_stop
protective_stop_pending
fault
```

### `input_select.hems_ev_worker_session_type`

Initial: `none`

```text
none
cheap_grid
urgent_recovery
approved_recovery
```

### `input_select.hems_cloudy_day_grid_charge_decision`

Initial: `not_asked`

```text
not_asked
pending
approved
declined
```

### `input_select.hems_ev_connection_charge_plan`

Initial: `Unanswered`

```text
Unanswered
Cheap Grid
Solar Only
Charge Now
```

## Date/time and text helpers

| Entity ID | Type | Initial guidance |
|---|---|---|
| `input_datetime.hems_charging_target_time` | time only | `14:30:00` |
| `input_datetime.hems_ev_expected_return_time` | date and time | current date/time |
| `input_datetime.hems_ev_worker_last_command` | date and time | a time at least two minutes in the past |
| `input_datetime.hems_advanced_forecast_last_updated` | date and time | current date/time |
| `input_datetime.hems_advanced_forecast_latest_end` | date and time | current date/time |
| `input_text.hems_advanced_forecast_status` | text | `NOT_CACHED` |
| `input_text.hems_financial_date` | text | blank or today's ISO date |
| `input_text.hems_solar_morning_forecast_date` | text | blank or today's ISO date |

## Package-defined helpers

Do not create these manually when the supplied packages are enabled:

- `input_select.hems_energy_source_view`
- `input_select.hems_energy_timescale`
- `input_select.hems_savings_timescale`
- `input_number.hems_solar_historical_lifetime_energy`
- `input_number.hems_solar_historical_average_value`
- `input_number.hems_powerwall_historical_discharge_energy`
- `input_number.hems_powerwall_historical_average_value`

The following packages also declare their own complete helper sets. Do not
duplicate those helpers in the UI:

- `packages/powerwall_optimal_grid_native_excess.yaml`
- `packages/solar_ev_interlock.yaml`
- `packages/solar_powerwall_soc_cycle.yaml`

## Fresh-install limitation

This alpha preserves the proven UI-template workflow. The standalone `.jinja`
files contain complete state templates, but Home Assistant template entities
and their metadata must still be created through the UI and mapped using
`entity-mapping.md`. A future release may consolidate them into a single
portable package after further live commissioning.
