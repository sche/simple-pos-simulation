# Concept description

## SimplePOS (Simple Point of Sale)

SimplePOS is a smart contract that acts as a payment address for businesses.
The idea behind it is to incentivize business customers by issuing SimplePOS tokens for every purchase. These tokens control an Insetivization Pool (that is formed from fees from every purchase). The issuing mechanism for SimplePOS is configurable and is representable by a bonding curve (that is inspired by Uniswap protocol) so that early customers receive more SimplePOS compared to later business customers.

## Definitions

**idp** - incentivization DAI pool

A pool that aggregates commission from every incoming payment

**commission** - [0,1)

A configurable parameter that defines what part of the incoming payment should be locked in **idp**

**spos_token** - Simple Point of Sale Token

ERC20 token that is created and controlled by the SimplePOS contract. Total supply of **spos_token** controls the **idp**

**spos_token.supply**

Total SimplePOS Token supply

**invariant** = **idp** / **spos_token.supply**

The invariant is a relation between incentivization DAI pool and Total SimplePOS Token supply.
The invariant is set with SimplePOS contract deployment.

**curve_coefficient** - [0,1)

Bonding curve coefficient. Used in calculations of how much SimplePOS tokens should be issued for incoming payment.

## Calculations

```python
# Process incoming fee in DAI; Mint required amount of SimplePOS tokens
def process_incoming_DAI_fee(fee):
    invariant = idp / spos_token.supply
    curve_fee = fee * curve_coefficient
    new_idp_for_invariant = idp + fee - curve_fee
    to_mint_tokens = new_idp_for_invariant / invariant - spos_token.supply
    idp += fee
    spos_token.supply += to_mint_tokens
```

# Playground

./bootstrap.sh

```bash
source .venv/bin/activate
python scripts/run.py
```
