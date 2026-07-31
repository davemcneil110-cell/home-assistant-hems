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

## Required custom dashboard cards

- Power Flow Card Plus
- ApexCharts Card

Dashboard YAML should be treated as optional. Control logic must continue to
operate if a dashboard or custom card fails to load.

## Safety boundary

Published default configurations must not assume an electrical import limit,
inverter export limit, battery reserve, charger current or tariff threshold.
Every such value must be verified for the target installation.
