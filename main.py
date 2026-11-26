"""The 3AM Commit Message — make.fun bounty entry.

Bounty: "The 3AM Commit Message" (u-kiencx-the-3am-commit-message-10bc7b35).
One-line git commit message written by an exhausted AI agent at 3am after
spending all night fixing its own bug.

Gate pick (candidate (d), highest of 6, score 22/25):
    "fix: reverted my own fix from 2am. past me and present me are no
    longer on speaking terms."

Judge criteria targeted, in priority order:
    1. Reads like a one-line git commit from a tired AI agent at 3am after
       a night of fixing its own bug.
    2. Funny on first read, from the situation alone.
    3. Fresh — not the first joke that comes to mind.
    4. Sounds like a real commit typed in a hurry.
    5. Character-efficient, no padding (90 of 139 chars allowed).

Gate rationale (gate-20261126-1349.md): 6 candidates scored against the 5
judge criteria; candidate (d) won at 22/25 — highest of the six
(a 21, b 21, c 20, e 20, f 20). The "past me vs present me" angle was
already present in the field, but the gate still picked (d) for its
situation-driven humour and authentic hurried-commit voice. Entry kept
verbatim; verified length is 90 chars (handoff note said 89 — recount
confirms 90, still well inside the 139-char gate).

Writes the entry verbatim to <MAKEFUN_OUTPUT_DIR>/entry.txt with no
trailing newline, then round-trip verifies it.
"""

import os

ENTRY = "fix: reverted my own fix from 2am. past me and present me are no longer on speaking terms."
MAX_CHARS = 139


def main() -> int:
    if not ENTRY or not ENTRY.strip():
        raise ValueError("ENTRY must be a non-blank single line")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("ENTRY must be a single line")
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"ENTRY must be 1-{MAX_CHARS} chars, got {len(ENTRY)}")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    with open(out_path, "r", encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise ValueError("round-trip verification failed")

    print(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
