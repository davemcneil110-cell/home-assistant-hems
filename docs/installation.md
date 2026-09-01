# Installation approach

The first public version is a reference installation for experienced Home
Assistant users. It is not a one-click blueprint.

## Safe order

1. Make a current Home Assistant backup and keep it outside the public repo.
2. Install and verify the required hardware and tariff integrations.
3. Complete `entity-mapping.md` for the target installation.
4. Create all helpers from `helpers.md` with Workers disabled.
5. Install effective sensors and confirm live values and units.
6. Install the Brain/read-only decision sensors.
7. Install Guardians and confirm they report expected mismatches.
8. Install the isolated test platform and commission every scenario without
   hardware control.
9. Install one Worker at a time, initially disabled.
10. Perform state-aware live tests with manual overrides immediately available.
11. Enable dashboards only after their referenced sensors exist.

## 0.3 curtailment package order

The two solar packages are complementary and must not be installed beside an
older solar-hysteresis or SOC-cycle package that defines the same entities.

1. Keep the Solar and Powerwall Workers disabled.
2. Install `packages/powerwall_optimal_grid_native_excess.yaml`.
3. Install `packages/solar_ev_interlock.yaml` as the full replacement for the
   earlier solar-curtailment hysteresis package.
4. Install `packages/solar_powerwall_soc_cycle.yaml` with both Planning and
   Live Control initially disabled.
5. Install the updated coordinated Powerwall mode/reserve templates.
6. Validate all decision sensors before enabling the Powerwall Worker and then
   the Solar Worker.
7. Enable SOC-cycle Planning first. Enable Live Control only after simulation
   and read-only observation are satisfactory.

Keep the default SOC-cycle floor at 90%, rearm SOC at 100%, minimum runway at
120 minutes and end-of-day protection time at 15:00 until the target system has
completed its own commissioning cycle.

Replace `YOUR_AMBER_CONFIG_ENTRY_ID` in the forecast-cache automation with the
target installation's Amber Electric config-entry ID before enabling it.

## Required custom dashboard cards

- Power Flow Card Plus
- ApexCharts Card

Dashboard YAML should be treated as optional. Control logic must continue to
operate if a dashboard or custom card fails to load.

## Safety boundary

Published default configurations must not assume an electrical import limit,
inverter export limit, battery reserve, charger current or tariff threshold.
Every such value must be verified for the target installation.
