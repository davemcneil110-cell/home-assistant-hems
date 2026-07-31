# Security and privacy

Never include any of the following in an issue, pull request, diagnostic bundle
or repository commit:

- Home Assistant backups or `.storage` contents;
- long-lived access tokens, API keys, cookies or webhook URLs;
- `secrets.yaml`;
- recorder databases;
- exact home addresses, coordinates, NMI or meter serial numbers;
- notification targets or device identifiers belonging to a private install;
- vehicle, household, receipt or camera data.

If a secret is committed, remove it from the repository history and revoke or
rotate it immediately. Deleting it only in a later commit is not sufficient.

Hardware-control issues should include redacted entity states and automation
traces. Users should confirm that no service data exposes tokens or personal
identifiers before posting.
