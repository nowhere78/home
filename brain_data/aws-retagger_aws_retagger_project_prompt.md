# Prompt: Generate a Local Python Project for AWS Retagging (with short CLI flags)

> **Objective**  
> Create a production‑ready Python CLI tool that scans AWS resources across multiple named profiles for a specific tag key/value and retags them to a new key/value. Use the **Resource Groups Tagging API** for discovery and updates. Provide both a **pure-venv workflow** and optional **Makefile** convenience targets.  
>
> **Repo & Bootstrap**  
> - Initialize a new Git repo using GitHub CLI (document the commands in README):  
>   ```bash
>   export REPO=aws-retagger
>   mkdir "$REPO" && cd "$REPO"
>   git init -b main
>   gh repo create "$REPO" --public --source=. --remote=origin --push
>   ```
> - Add a `.gitignore` suitable for Python/venv/IDE artifacts.  
>
> **Environment & Tooling**  
> - Default to **Python venv**: `python -m venv .venv` with setup steps in README for macOS/Linux/Windows.  
> - Add optional **Makefile** targets (`venv`, `install`, `format`, `lint`, `run`).  
> - Configure **Black** and **Ruff** via `pyproject.toml` (Black line-length 100; Ruff with common rules).  
> - Pin runtime deps in `requirements.txt` (`boto3`, `botocore`) and dev deps installed via Makefile or README steps.  
>
> **Project Layout (src layout)**  
> ```
> aws-retagger/
> ├─ src/
> │  └─ retagger/
> │     ├─ __init__.py
> │     ├─ cli.py
> │     └─ core.py
> ├─ pyproject.toml
> ├─ requirements.txt
> ├─ Makefile          # optional; keep project usable without it
> ├─ README.md
> └─ .gitignore
> ```
>
> **Runtime & Style**  
> - Python **3.11+** with type hints.  
> - Clean logging via `logging` (timestamped, single StreamHandler).  
> - Lint- and format-clean (Ruff + Black).  
>
> **CLI**  
> - Package entrypoint as a console script named **`retagger`** (`[project.scripts] retagger = "retagger.cli:main"`).  
> - Use `argparse` and provide **short flags for every argument**:  
>   - `-ok, --old-key` (required) — existing tag key to match  
>   - `-ov, --old-value` (required) — existing tag value to match  
>   - `-nk, --new-key` (required) — new tag key to apply  
>   - `-nv, --new-value` (required) — new tag value to apply  
>   - `-ko, --keep-old` (flag) — keep the old tag after applying the new one  
>   - `-r,  --regions` — comma‑separated regions (default: discover per profile)  
>   - `-p,  --profiles` — comma‑separated profiles (default: all local profiles)  
>   - `-s,  --services` — comma‑separated `ResourceTypeFilters` (e.g., `ec2:instance,s3:bucket`)  
>   - `-d,  --dry-run` (flag) — plan only; don’t call tagging APIs  
>   - `-m,  --max-pages` (int, default 1000) — safety cap for pagination  
>   - `-l,  --log-level` (`DEBUG|INFO|WARNING|ERROR`, default `INFO`)  
>
> **Behavior & AWS Logic**  
> - For each chosen or discovered **AWS named profile**, build a `boto3.Session(profile_name=...)`.  
> - Discover supported regions per profile (EC2 `describe_regions` with `OptInStatus` in `None|opt-in-not-required|opted-in`).  
> - Use **Resource Groups Tagging API** (`resourcegroupstaggingapi`) to find and retag resources:  
>   - **Discovery:** `get_resources(TagFilters=[{"Key": old_key, "Values": [old_value]}], ResourceTypeFilters=[...])` with pagination.  
>   - **Tagging:** `tag_resources(ResourceARNList=[...], Tags={new_key: new_value})` in batches of ≤20 ARNs.  
>   - **Untag (optional):** if `--keep-old` is not set and the key/value changed, call `untag_resources(ResourceARNList=[...], TagKeys=[old_key])`.  
> - Respect `--dry-run`: log the intended changes without API calls.  
> - Log per profile/region: scanned, matched, tagged, untagged, errors.  
> - Handle retries with `botocore.config.Config(retries={"max_attempts": 10, "mode": "standard"})`.  
> - Gracefully continue on unsupported resources or partial failures; never crash the whole run.  
>
> **Code Structure**  
> - `core.py`:  
>   - `RetagRunner` class encapsulating config (old/new key/value, filters, max_pages, logger).  
>   - Helpers: `available_profiles()`, `available_regions(session)`, `find_resources(session, region)`, `build_plan(arns)`, `apply_plan(session, region, plan, dry_run)`, `run_profile(profile, regions, dry_run)`.  
>   - Lightweight `@dataclass RetagPlan` with `arns`, `will_tag`, `will_untag`.  
> - `cli.py`:  
>   - `parse_args()` with the **short flags** listed above.  
>   - `setup_logger()` to configure formatting and levels.  
>   - `main()` to wire args → `RetagRunner` and loop profiles.  
>
> **Files to Generate (content requirements)**  
> 1) `pyproject.toml`  
>    - Build-system (setuptools), `project.scripts` entry, Black & Ruff config (line-length 100, target `py311`, Ruff rules: `E,F,I,UP,B`; ignore `E501`).  
> 2) `requirements.txt` with `boto3>=1.34`, `botocore>=1.34`.  
> 3) `Makefile` (optional, but include) with targets:  
>    - `venv`: create venv and upgrade pip  
>    - `install`: install runtime + dev tools (Black, Ruff)  
>    - `format`: Black + Ruff fix  
>    - `lint`: Ruff check + Black check  
>    - `run`: `python -m retagger $(ARGS)`  
> 4) `README.md` (must include):  
>    - **Why/what** the tool does.  
>    - **Setup**: pure‑venv steps for macOS/Linux/Windows; optional Makefile route.  
>    - **Examples using short flags**:  
>      ```bash
>      # Dry run across all local profiles, auto-discover regions
>      retagger -ok Owner -ov Legacy -nk Owner -nv Platform -d
>
>      # Specific profiles & regions
>      retagger -ok CostCenter -ov 1234 -nk CostCenter -nv 5678 >        -p dev,prod -r eu-west-1,eu-north-1
>
>      # Filter by resource types (ResourceTypeFilters)
>      retagger -ok Environment -ov Test -nk Environment -nv Prod >        -s ec2:instance,s3:bucket -d
>      ```
>    - Notes and limitations of the **Resource Groups Tagging API** (service coverage, batch size ≤20, eventual consistency, org/SSO caveats).  
>    - Exit codes and logging levels.  
> 5) `src/retagger/core.py` and `src/retagger/cli.py` implementing everything above, with robust error handling and docstrings.  
> 6) `.gitignore` covering `.venv/`, `__pycache__/`, `*.pyc`, build artifacts, `.env`, editor folders.  
>
> **Acceptance Criteria**  
> - `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt && pip install -e .` works on a clean machine.  
> - `retagger -ok K -ov V -nk K2 -nv V2 -d` runs and prints a clear plan without calling AWS.  
> - Real runs tag and (optionally) untag with correct batching and pagination.  
> - `ruff .` and `black --check .` pass with no errors.  
> - Optional: `make venv && make install && make run ARGS="..."` also works.  
>
> **Quality Notes**  
> - Use precise, contextual logging (profile, region, counts).  
> - Don’t swallow exceptions; log and continue where reasonable.  
> - Keep functions testable and side‑effect‑light.  
> - Include type annotations and docstrings for public functions/classes.  
>
> **References (for implementation)**  
> - Boto3 `resourcegroupstaggingapi` operations: `get_resources`, `tag_resources`, `untag_resources`.  
> - EC2 `describe_regions` for region discovery.  
> - Botocore retry configuration.
