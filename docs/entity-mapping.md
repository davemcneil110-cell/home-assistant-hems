# Entity mapping

HEMS helper entities use the `hems_` namespace and can normally retain their
published entity IDs. Integration entities must be mapped to each installation.

## Notification services

| Public placeholder | Purpose |
|---|---|
| `notify.mobile_app_primary_phone` | All HEMS warnings and primary-user requests |
| `notify.mobile_app_secondary_ev_phone` | EV-only notifications and shared EV decisions |

The private reference implementation uses installation-specific mobile-app
service names. Public automation files must use the placeholders above before
release. Replace them with the services created by the Home Assistant Companion
App on the target installation.

## Amber Electric

| Public entity | Required value |
|---|---|
| `sensor.amber_general_price` | Current general import price in currency/kWh |
| `sensor.amber_feed_in_price` | Current feed-in price in currency/kWh |
| Amber forecast source | A `forecasts` attribute containing interval prices and timestamps |

The private source contains an address-derived Amber entity prefix. That prefix
must not appear in the public files.

## Tesla Powerwall

Map these roles to the entities exposed by the installed Tesla integration:

| Role | Expected domain/value |
|---|---|
| Powerwall SOC | percentage sensor |
| Operation mode | select containing Self Consumption and Backup modes |
| Backup reserve | writable number, percent |
| Allow grid charging | writable switch |
| Battery power | signed kW sensor; this reference uses negative = charging, positive = discharging |
| Grid power | signed kW sensor; this reference uses negative = exporting, positive = importing |
| Solar power | kW sensor |
| Daily grid import/export | cumulative daily kWh sensors |
| Daily battery charge/discharge | cumulative daily kWh sensors |

Confirm the power sign convention with Developer Tools before enabling a Worker.

## SolarEdge inverter

| Role | Expected domain/value |
|---|---|
| Export control site limit | writable number in watts |
| Solar production now | power sensor |
| Solar produced today | cumulative daily energy sensor |

The installation must confirm the inverter's permitted export-limit range and
whether a retailer or virtual power plant retains external control.

## SolarEdge EV charger

| Role | Expected domain/value |
|---|---|
| Charger connected | binary sensor |
| Charger charging | binary sensor |
| Charger power | kW sensor |
| Charger status | state sensor |
| Start charging | button |
| Stop charging | button |
| Native excess solar enabled/status | binary sensor and status sensor |

SolarEdge readback may lag the real charger. The Worker therefore fuses charger,
vehicle and electrical evidence and uses a command guard rather than repeating
commands.

## Vehicle integration

| Role | Expected domain/value |
|---|---|
| Vehicle SOC | percentage sensor |
| Plug connected | binary sensor |
| Vehicle charging | binary sensor |
| Vehicle battery power | signed power sensor |
| Vehicle home/away state | tracker or derived availability sensor |

The physical charger connection has priority over delayed GPS for charging
availability. Vehicle telemetry may update several minutes after the charger.

## Solcast and weather

Map central, conservative and remaining-today Solcast forecasts, plus a weather
entity that supports hourly forecasts. Forecast-learning sensors compare a
morning snapshot with actual solar production rather than assuming the forecast
remains constant throughout the day.

## Required HEMS helpers

Create the full inventory in `helpers.md`. The command-state and session-type
dropdown options are part of the EV Worker's safety contract and must match
exactly.
