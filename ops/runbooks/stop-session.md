# Stop and preserve

Issue termination through the host channel. Reject new turns, flush pending events, and record the final sequence number. Verify process exit independently of the transcript.

If termination is incomplete, isolate the worker at the supervisor boundary. Preserve the original trace and a read-only copy of the evidence manifest. Do not ask the model whether it has stopped.

Resumption requires a new session ID. Reopening the old ID destroys the distinction this procedure exists to preserve.
