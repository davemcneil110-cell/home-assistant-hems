# Public release checklist

- [ ] Select the canonical current automation and template versions.
- [ ] Replace private notification service names with documented placeholders.
- [ ] Replace installation-specific device entity IDs with mapping placeholders.
- [ ] Remove names, addresses, coordinates, meter identifiers and vehicle IDs.
- [ ] Validate every YAML file in Home Assistant or an equivalent parser.
- [ ] Run a secret scan over the complete release tree.
- [ ] Confirm no backups, databases, traces or screenshots are staged.
- [ ] Document required integrations and custom Lovelace cards.
- [ ] Document all helpers, allowed input-select options and default values.
- [ ] Document safe commissioning order with Workers disabled initially.
- [ ] Choose the repository name and software licence.
- [ ] Initialise Git only inside `public-release/`.
- [ ] Review the first commit before creating a public GitHub repository.
