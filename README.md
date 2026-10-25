# Casino Payment Methods: A Practical Verification Toolkit

This open reference helps writers, researchers, and consumers evaluate claims about payment methods listed by online services. It is designed to make comparisons more careful and transparent—not to claim that a particular casino accepts a payment method.

**Important scope note:** the included taxonomy is a general starting point, not a live or independently verified list of casino payment options. Operator-specific availability, fees, limits, currencies, verification rules, and payout times must be checked against current primary sources.

## What you can use it for

- Distinguish a payment category from a specific provider or payment service.
- Check deposits and withdrawals separately rather than assuming that a method supports both.
- Record the source, country or region, and date behind each claim.
- Compare the operator's stated processing time with any additional provider or bank settlement time.
- Flag missing information instead of guessing or treating “not stated” as “not supported.”

## Repository contents

- [Payment-method taxonomy](data/payment-methods.csv) — general categories and cautions in spreadsheet-friendly format.
- [JSON taxonomy](data/payment-methods.json) — the same reference in a structured format.
- [Practical verification guide](GUIDE.md) — a checklist for assessing payment claims.
- [Data collection template](data/payment-claims-template.csv) — a blank structure for recording sourced, operator-specific claims.
- [Source and verification policy](SOURCES.md) — how to document and maintain claims.

## Quick verification checklist

Before publishing a claim about a payment method, record:

1. **Where it applies:** operator, country/region, currency, and relevant account conditions.
2. **What it supports:** deposits, withdrawals, or both, based on the operator's own information.
3. **The actual costs:** stated fees and possible currency conversion or network costs.
4. **The actual timing:** separate operator review from payment-provider or bank processing where possible.
5. **The evidence:** a direct official source URL and the date you checked it.

If a point cannot be verified, mark it as “not stated” or “not verified”—do not fill the gap with assumptions.

## Swedish-market context

Anyone researching gambling services aimed at people in Sweden should check the applicable rules and the operator's licence status using official information. The Swedish Gambling Authority publishes information about [online casinos](https://www.spelinspektionen.se/spelare/spelform/onlinekasino/) and [Spelpaus](https://www.spelinspektionen.se/lagar-regler/spelansvar-och-konsumentskydd/spelpaus.se). Do not assume that a foreign website is covered by Swedish safeguards just because it accepts Swedish customers or Swedish payment methods.

For an explanation of the payment-reference methodology, see [GUIDE.md](GUIDE.md).

## Maintainer disclosure

The maintainer also operates the following Swedish-language casino comparison websites: [MGA Casino utan svensk licens](https://mga-casino-utan-svensk-licens.se/) and [MrCasinosOnline](https://mrcasinosonline.com/). They are commercial websites operated separately from this reference project; their inclusion is a disclosure of the maintainer's interests, not an independent endorsement or a claim that either site has verified every item in this dataset.

## Contributing

Corrections and improvements are welcome. Please include the official source, relevant country or region, and date checked for factual claims. Do not add unsupported casino availability, prices, fees, or withdrawal-time claims.

## Limitations

This project is informational and does not provide financial or legal advice. It does not recommend that anyone gamble, and it does not guarantee that a payment method is safe, available, reversible, fee-free, or suitable for a specific person. Check current terms directly with the operator, payment provider, and relevant official authorities.

Gambling involves financial risk. Follow applicable law and seek support if gambling is causing harm.
