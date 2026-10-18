"""Run finite scientific checks and compare them with committed outputs."""

import argparse
import json
import math
from pathlib import Path

import check_potential
import check_process


def equivalent(actual, expected, path="result"):
    if isinstance(actual, dict) and isinstance(expected, dict):
        if actual.keys() != expected.keys():
            raise AssertionError(f"Different fields at {path}")
        for key in actual:
            equivalent(actual[key], expected[key], f"{path}.{key}")
    elif isinstance(actual, list) and isinstance(expected, list):
        if len(actual) != len(expected):
            raise AssertionError(f"Different list lengths at {path}")
        for index, (item, reference) in enumerate(zip(actual, expected)):
            equivalent(item, reference, f"{path}[{index}]")
    elif isinstance(actual, float) or isinstance(expected, float):
        if not (math.isfinite(actual) and math.isfinite(expected)
                and math.isclose(actual, expected, rel_tol=1e-8, abs_tol=1e-10)):
            raise AssertionError(f"Numerical reference mismatch at {path}: {actual} vs {expected}")
    elif actual != expected:
        raise AssertionError(f"Reference mismatch at {path}: {actual!r} vs {expected!r}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", action="store_true",
                        help="Explicitly replace reference outputs after scientific review")
    args = parser.parse_args()
    directory = Path(__file__).resolve().parent / "expected"
    outputs = {"process": check_process.run(), "potential": check_potential.run()}
    for name, result in outputs.items():
        target = directory / f"{name}.json"
        if args.record:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
        else:
            equivalent(result, json.loads(target.read_text()), name)
    rows = outputs["potential"]["checks"]
    print(json.dumps({
        "passed": True,
        "reference_action": "recorded" if args.record else "verified without rewriting",
        "exact_process_checks": outputs["process"],
        "potential_cases": len(rows),
        "oracle_instances_per_case": outputs["potential"]["N"],
        "steps_per_case": outputs["potential"]["steps"],
        "minimum_PSD_eigenvalue": min(row["minimum_PSD_residual_eigenvalue"] for row in rows),
        "maximum_trace_error": max(row["maximum_conditional_trace_error"] for row in rows),
    }, indent=2))


if __name__ == "__main__":
    main()
