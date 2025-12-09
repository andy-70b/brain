# Operator quickstart

Use Python 3.11 or newer. Run commands from the repository root. The package has no runtime dependencies.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m andy replay --prompt "Identify yourself." --json
python -m andy inventory
python -m unittest discover -s tests -v
```

On Windows, activate with `.venv\Scripts\Activate.ps1`. To avoid installation entirely, set `PYTHONPATH=src` (PowerShell: `$env:PYTHONPATH = "src"`) before the module commands.

Expected replay source: `replay`, record ID: `c001`. Unknown prompts return `replay-miss`. No network credentials are required.
