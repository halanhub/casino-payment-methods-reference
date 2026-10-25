#!/usr/bin/env python3
"""Validate sourced payment claims in CSV files (Python standard library only)."""

from __future__ import annotations

import argparse
import csv
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

REQUIRED_COLUMNS = [
    "operator_name", "operator_url", "target_country_or_region",
    "payment_method_name", "payment_category", "deposits_supported",
    "withdrawals_supported", "minimum_deposit", "maximum_deposit",
    "minimum_withdrawal", "currency", "operator_fee", "provider_or_bank_fee",
    "currency_conversion_note", "operator_processing_time",
    "provider_or_bank_settlement_time", "eligibility_or_verification_notes",
    "source_url", "source_type", "date_checked_yyyy_mm_dd", "checked_by",
    "confidence", "notes",
]
SUPPORT_VALUES = {"yes", "no", "not stated", "not verified"}
SOURCE_TYPES = {"official_operator", "official_provider", "official_regulator", "other"}
CONFIDENCE_VALUES = {"high", "medium", "low"}
REQUIRED_NONEMPTY = {
    "operator_name", "operator_url", "target_country_or_region",
    "payment_method_name", "payment_category", "deposits_supported",
    "withdrawals_supported", "eligibility_or_verification_notes", "source_url",
    "source_type", "date_checked_yyyy_mm_dd", "checked_by", "confidence", "notes",
}
STALE_AFTER_DAYS = 180


def valid_http_url(value: str) -> bool:
    parsed = urlparse(value.strip())
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def validate_file(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if not path.exists():
        return [f"{path}: file does not exist"], warnings

    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            headers = reader.fieldnames or []
            if headers != REQUIRED_COLUMNS:
                errors.append(
                    f"{path}: headers do not match the required schema/order; "
                    f"expected {len(REQUIRED_COLUMNS)} columns, found {len(headers)}"
                )
                return errors, warnings

            seen: set[tuple[str, str, str]] = set()
            row_count = 0
            today = date.today()

            for line_number, row in enumerate(reader, start=2):
                if not row or all(not (value or "").strip() for value in row.values() if value is not None):
                    continue
                row_count += 1

                if None in row:
                    errors.append(f"{path}:{line_number}: row has extra columns")
                    continue

                for field in REQUIRED_NONEMPTY:
                    if not (row.get(field) or "").strip():
                        errors.append(f"{path}:{line_number}: required field '{field}' is blank")

                for field in ("deposits_supported", "withdrawals_supported"):
                    if (row.get(field) or "").strip().lower() not in SUPPORT_VALUES:
                        errors.append(f"{path}:{line_number}: invalid {field} value")

                if (row.get("source_type") or "").strip() not in SOURCE_TYPES:
                    errors.append(f"{path}:{line_number}: invalid source_type value")
                if (row.get("confidence") or "").strip().lower() not in CONFIDENCE_VALUES:
                    errors.append(f"{path}:{line_number}: invalid confidence value")

                for field in ("operator_url", "source_url"):
                    if not valid_http_url(row.get(field) or ""):
                        errors.append(f"{path}:{line_number}: '{field}' must be an HTTP(S) URL")

                checked = (row.get("date_checked_yyyy_mm_dd") or "").strip()
                try:
                    checked_date = date.fromisoformat(checked)
                    if checked_date.isoformat() != checked:
                        raise ValueError
                    if checked_date > today:
                        errors.append(f"{path}:{line_number}: check date is in the future")
                    elif (today - checked_date).days > STALE_AFTER_DAYS:
                        age = (today - checked_date).days
                        warnings.append(
                            f"{path}:{line_number}: source check is {age} days old "
                            f"(>{STALE_AFTER_DAYS}); re-check before relying on this row"
                        )
                except ValueError:
                    errors.append(
                        f"{path}:{line_number}: date_checked_yyyy_mm_dd must use YYYY-MM-DD"
                    )

                key = (
                    (row.get("operator_name") or "").strip().casefold(),
                    (row.get("target_country_or_region") or "").strip().casefold(),
                    (row.get("payment_method_name") or "").strip().casefold(),
                )
                if key in seen:
                    errors.append(
                        f"{path}:{line_number}: duplicate operator/region/payment-method entry"
                    )
                seen.add(key)

            if row_count == 0:
                errors.append(f"{path}: no data records found")
            elif not errors:
                print(f"PASS {path}: {row_count} records validated")
    except (OSError, csv.Error) as exc:
        errors.append(f"{path}: could not read CSV: {exc}")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "files", nargs="+",
        help="CSV file(s) to validate, e.g. data/verified-payment-claims.csv",
    )
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    for name in args.files:
        file_errors, file_warnings = validate_file(Path(name))
        errors.extend(file_errors)
        warnings.extend(file_warnings)

    for warning in warnings:
        print(f"WARNING {warning}", file=sys.stderr)
    for error in errors:
        print(f"ERROR {error}", file=sys.stderr)
    if errors:
        return 1
    print(f"Validation completed with {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
