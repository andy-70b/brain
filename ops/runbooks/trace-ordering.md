# Trace ordering

Use host sequence numbers as the primary order within a session. Wall-clock timestamps support cross-system correlation but can move under clock correction. Transport arrival order is not causal order.

A completion delivered after closure may have been generated before closure. Compare sequence and receipt records before declaring a lifecycle violation. Preserve both arrival and event times when an adapter supplies them.
