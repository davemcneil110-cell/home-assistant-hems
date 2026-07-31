# Architecture

```text
Real integrations
       |
       v
Effective sensors  <---- isolated test overrides
       |
       v
HEMS Brain
       |
       +---- desired Powerwall state
       +---- EV permission and target
       +---- desired solar export limit
       +---- financial and forecast decisions
       |
       v
State-aware Workers
       |
       v
Real hardware
```

The Brain expresses intent. Workers own hardware commands. A Worker sends a
command only when actual state differs from desired state, records that command,
waits for acknowledgement, and enters a cooldown or durable fault state rather
than repeating commands.

Effective sensors are the boundary between real data and simulation. Test
scenarios override only those sensors, allowing rare price, solar, EV and
Powerwall conditions to be commissioned without changing integration entities.

## Worker ownership

An EV session is explicitly owned by the EV Worker only after it has claimed an
eligible permission and issued a guarded Start. Native SolarEdge excess-solar
sessions and manual sessions remain outside Worker ownership.

Powerwall coordination is an interlock before EV Start, but ordinary policy
transitions after charging is confirmed do not stop a valid EV session.

## Manual override

Manual override disables new Worker commands and releases Worker ownership
without pressing a hardware Start or Stop button. This prevents automation from
fighting a person or another native controller.
