# Practical guide to verifying casino payment methods

This guide is intended for researchers and readers comparing payment claims. It is not a list of currently supported methods at any particular casino. The goal is to show what must be checked before a payment-method claim can be called reliable.

## 1. Identify what the name refers to

A payment label might refer to a card network, bank transfer, e-wallet, payment gateway, bank-connect service, prepaid voucher, mobile carrier billing, or cryptocurrency network. These are not interchangeable. Where possible, identify both the user-facing service and the underlying payment type.

Do not assume that two services with similar names have the same coverage, fees, or payout rules.

## 2. Treat deposits and withdrawals as separate claims

An operator may list a payment method for deposits without offering withdrawals through that method. For every operator-specific entry, check separately:

- Can the method be used to deposit?
- Can it be used to withdraw?
- Are withdrawals required to use the same method or a different route?
- Are there minimums, maximums, or account-specific restrictions?
- Does the operator require the payment account to be in the player's own name?

If an official source does not answer a question, record “not stated.” Do not turn missing information into a positive or negative claim.

## 3. Separate the types of costs

When the source provides the information, distinguish among:

- Fees charged by the operator.
- Fees charged by the payment provider, bank, card issuer, or network.
- Currency conversion or exchange-rate costs.
- Network fees associated with digital assets.
- Any other costs stated in the applicable terms.

A statement that an operator charges no fee does not necessarily establish that every bank or payment provider involved charges no fee. Avoid using “free” unless the scope is clearly defined and verified.

## 4. Separate processing stages

“Instant” can be ambiguous. A payment may be authorised quickly while an account review, fraud check, operator approval, bank transfer, or payout settlement takes longer.

When timing information is published, preserve the source's wording and identify which stage it describes. Do not convert a provider estimate into a guaranteed end-to-end withdrawal time. If the sources do not explain the stages, say so.

## 5. Understand method-specific questions

These are prompts for verification, not universal claims about every provider.

| Payment category | Questions worth checking |
|---|---|
| Bank transfer | Which banks and countries are supported? What reference details are required? Are incoming and outgoing transfers treated differently? |
| Credit/debit card | Which card networks and issuing countries are accepted? Could the issuer block gambling-related transactions? What currency and cardholder-name rules apply? |
| E-wallet | Does the wallet provider permit the intended transaction? Are account verification, wallet currency, or withdrawal rules relevant? |
| Prepaid voucher | Is it deposit-only? If so, what withdrawal method is available under the operator's rules? |
| Mobile/carrier payment | Is the service available with the user's country and carrier? Are charges added to a mobile bill? |
| Open-banking or bank-connect service | Which banks and countries participate? What account permissions and authentication steps are requested? |
| Instant bank payment | What does “instant” describe: authorisation, transfer initiation, settlement, or the operator's processing? |
| Cryptocurrency | Which asset and exact network are required? Are addresses and networks compatible? What fees, volatility, irreversibility, and legal considerations apply? |

## 6. Check the operator and relevant rules

For Sweden-related research, consult the Swedish Gambling Authority's official information about [online casinos](https://www.spelinspektionen.se/spelare/spelform/onlinekasino/) and [Spelpaus](https://www.spelinspektionen.se/lagar-regler/spelansvar-och-konsumentskydd/spelpaus.se). Verify licence-related claims directly from official sources rather than inferring status from a website's design, language, payment methods, or marketing.

Spelpaus is the Swedish national self-exclusion register for gambling covered by the Swedish licensing framework. Do not assume a self-exclusion tool covers every overseas site. Anyone concerned about gambling harms should consult official support information and avoid gambling rather than trying to work around an exclusion.

This guide is general information, not legal advice. Applicable rules can vary by the person's location and the operator's circumstances.

## 7. Use primary sources and keep a record

Use sources in this order where available:

1. The operator's own cashier, payment, withdrawal, and terms pages for operator-specific claims.
2. The payment provider's official documentation for provider-specific restrictions and processes.
3. A regulator or government source for legal and licensing information.

For every claim, keep the URL and date checked. Prefer a specific page that directly supports the claim over a homepage or search snippet. If official pages conflict, document the conflict and avoid presenting the claim as settled until it is resolved.

Recommended record fields are provided in [the CSV template](data/payment-claims-template.csv).

## 8. A compact publication standard

A payment comparison is ready to publish when a reader can answer:

- Which operator and country does this information apply to?
- What exactly was verified?
- Does the claim refer to deposits, withdrawals, or both?
- What fees, limits, timing, and eligibility details are known—and what remains unknown?
- Which primary source supports the claim, and when was it checked?
- Are any commercial relationships disclosed clearly?

If these answers are missing, treat the entry as incomplete instead of filling it with generic copy.
