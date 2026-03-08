# Statement Format Tracker (India)

This tracker is used to keep current notes about account statement formats for:

- HDFC Bank
- ICICI Bank
- SBI (State Bank of India)
- Motilal Oswal (Scriptbox)
- Zerodha

> Last updated: 2026-03-08

## How to use this file

1. Download a **fresh sample statement** from each provider portal at least once per month.
2. Compare against the latest parser/ops assumptions used internally.
3. Update this file with any format differences.
4. Mark changed fields as `CHANGED` and include the effective date.

---

## HDFC Bank

### Common statement channels
- NetBanking account statement (PDF)
- NetBanking account statement (Excel/CSV)
- e-mail generated account statement

### Baseline format checkpoints
- Header includes account holder name, account number (masked/full), IFSC, branch details.
- Date/value-date columns are separate in transaction table.
- Narration column often includes UPI/VPA/UTR references.
- Debit, credit, and running balance columns are present.
- Footer may include system-generated disclaimer and page numbering.

### Verification notes
- Current status: `PENDING MONTHLY VERIFICATION`
- Last verified sample: `NOT ATTACHED`

---

## ICICI Bank

### Common statement channels
- Internet Banking detailed account statement (PDF)
- CSV export from transaction history
- e-Statement email attachment

### Baseline format checkpoints
- Account details panel appears before transaction grid.
- Transaction grid usually includes txn date, value date, particulars, cheque no., debit/credit, balance.
- Narration patterns include IMPS/NEFT/UPI indicators.
- Closing balance appears at statement end.

### Verification notes
- Current status: `PENDING MONTHLY VERIFICATION`
- Last verified sample: `NOT ATTACHED`

---

## SBI

### Common statement channels
- Online SBI account statement (PDF)
- Online SBI account statement (CSV/Excel)

### Baseline format checkpoints
- Header includes customer name and account number.
- Table usually includes txn date, value date, description/reference, debit, credit, and balance.
- Running balance direction and CR/DR markings should be validated.
- Summary/footer includes generated timestamp and statement period.

### Verification notes
- Current status: `PENDING MONTHLY VERIFICATION`
- Last verified sample: `NOT ATTACHED`

---

## Motilal Oswal (Scriptbox)

### Common statement/report channels
- Portfolio holding statements
- Capital gain statements
- Transaction summaries

### Baseline format checkpoints
- Investor/client metadata appears in report header.
- Instrument-wise rows include ISIN/scheme/security identifiers.
- Buy/sell dates, quantity, price, and realized/unrealized values are present where applicable.
- Charges/tax columns (if any) are represented separately.

### Verification notes
- Current status: `PENDING MONTHLY VERIFICATION`
- Last verified sample: `NOT ATTACHED`

---

## Zerodha

### Common statement/report channels
- Console reports (P&L, tax P&L, tradebook)
- Ledger statement exports
- Contract notes

### Baseline format checkpoints
- Client ID/PAN/account metadata present in header areas.
- Time/date precision and exchange segment columns should be validated.
- Charges and taxes are typically split into multiple columns/sections.
- Summary values should reconcile with line-item totals.

### Verification notes
- Current status: `PENDING MONTHLY VERIFICATION`
- Last verified sample: `NOT ATTACHED`

---

## Change log template

Use this when a format shift is detected:

```text
Provider: <HDFC|ICICI|SBI|Motilal Oswal|Zerodha>
Detected on: YYYY-MM-DD
Effective date (if known): YYYY-MM-DD
Changed section: <header|transaction table|footer|narration|charges>
Old format:
New format:
Impact on processing:
Action taken:
Owner:
```
