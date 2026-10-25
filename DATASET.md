# Verified payment claims dataset

**Snapshot date:** 2026-10-25  
**Market scope:** Sweden  
**Approach:** operator-published information only; not a live feed.

This initial dataset includes two official operator sources: Betsson's Swedish payment-method support information and Svenska Spel Casino's official casino page. It captures method-direction claims visible on those pages on the snapshot date. It is intentionally small and is not a ranking or recommendation.

## How to read the data

- Each row is a specific operator/method observation, not a guarantee that a method works for every account.
- `yes` means the cited operator page explicitly lists the method for that direction.
- `no` is used only where the operator explicitly says it is unavailable for that direction.
- `not stated` means the source does not say. It does **not** mean unavailable.
- Empty values mean the source did not provide that value.
- Where an operator gives a general minimum for a group of methods, this is noted; it may not be the method-specific limit for every payment rail or account.
- Some labels are normalized for readability. See row notes for qualifications.

## Source records

1. [Betsson Swedish payment methods in its support centre](https://support.betsson.com/sv.html?category=payment-methods) — lists deposit and withdrawal methods and general minimum amounts in the retrieved page content. Betsson's [Swedish FAQ](https://www.betsson.com/sv/logga-in) separately lists common deposit methods and notes availability can vary by country.
2. [Svenska Spel Casino — payment and withdrawal information](https://spela.svenskaspel.se/casino) — lists Swish, Apple Pay, payment cards, and bank transfer as deposit methods; describes withdrawal options separately. The page does not specify all fees, limits, or processing times.

This dataset was compiled with AI assistance by inspecting official operator pages. The date is the date checked for this initial snapshot, not a promise that the source will remain unchanged. Before relying on or publishing a row, open the source and re-check it. If a claim or method-specific detail cannot be confirmed, mark it as not verified.

## Why some fields are empty

Neither source provides a complete, method-by-method schedule of all fees, maximums, foreign-exchange costs, and end-to-end payout times in the cited page. Those blanks are intentional. Do not fill them by guessing, copying from another operator, or assuming provider-side transfer time equals operator payout time.

## Limitations

This snapshot is informational, not a payment guarantee, recommendation, or financial/legal advice. Payment availability may change and may vary by account, verification status, device, or region. Gambling carries financial risk; follow applicable law and use self-exclusion and support tools if needed.
