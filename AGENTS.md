## Environment & Shell Setup

* **WSL Distribution:** Ubuntu
* **Conda Environment:** `sage`
* **Default Shell Launch Command:**
  ```bash
  wsl.exe -d Ubuntu -e bash -c "source ~/miniforge3/etc/profile.d/conda.sh; conda activate sage; <cmd>"
  ```
  Do NOT rely on `--rcfile` or `~/.bashrc` — it early-returns in non-interactive shells, so `conda activate` never runs.

## Running Python / Sage

* The `sage` conda env has plain `python` with Sage installed as a library (`from sage.all import ...`). `sage -python` is not needed.
* Not everything is in `sage.all` — e.g. `chromatic_polynomial` lives in `sage.graphs.chrompoly`.

## Codebase conventions

* **Never import modules like `planar_coloring.py` to reuse their functions** — they execute full analysis pipelines (plotting, `exit()`) at module level, which produces no output and terminates the caller. Copy/duplicate small helpers instead.
* Graph input schema (`input_graphs/*.txt`): line 1 = vertex count n; then n lines of `x y neighbor1 neighbor2 ...` (vertex i's coordinates and adjacency list).

## Debugging tips for this setup

* `wsl.exe -d Ubuntu -e bash -c "..."` mangles `$?`, `$PATH`, etc. — write diagnostics to a file inside WSL and `cat` it, rather than expanding shell variables in the outer command.
