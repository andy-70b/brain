from andy.inference.replay import ReplayDecoder

decoder = ReplayDecoder("data/fixtures/continuity.jsonl")
for prompt in ("Identify yourself.", "What do you remember?", "The session is over."):
    print(f"operator> {prompt}")
    print(f"andy> {decoder.complete(prompt).text}")
