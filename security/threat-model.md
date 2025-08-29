# Trust model

| Boundary | Failure | Control |
|---|---|---|
| Text → host | A completion interpreted as authority | Separate control plane |
| Archive → context | Unreviewed evidence admitted | Explicit admission state |
| Worker → network | Unobserved external effects | No egress in baseline |
| Parameters → runtime | Unverified artifact loaded | Out-of-tree digest review |
| Transcript → operator | Persuasive output mistaken for evidence | Independent trace and observer |

The local package enforces only its own offline replay path. Deployment controls are requirements for the external research environment, not guarantees made by this Python package.
