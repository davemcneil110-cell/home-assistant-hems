# Contributing

HEMS controls high-power household equipment. Changes should remain small,
state-aware and independently testable.

Before opening a pull request:

1. Do not include Home Assistant backups, `.storage`, recorder databases,
   addresses, device serial numbers, notification service names or tokens.
2. Preserve the Brain/Worker boundary: decision sensors do not call hardware.
3. Preserve manual override and no-repeat command guards.
4. Supply complete replacement YAML when changing a UI automation.
5. Run `python tools/validate_ha_yaml.py` against every changed YAML/Jinja file.
6. Describe the effective-sensor test scenario and any live commissioning that
   was performed.

Hardware-specific changes should be introduced through documented entity
mapping rather than by committing a private installation identifier.
