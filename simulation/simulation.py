#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

idp = 1
spos_token_supply = 1

curve_coefficient = 0.5  # configurable dynamic param


def process_incoming_DAI_fee(fee):
    global idp, spos_token_supply, curve_coefficient
    invariant = idp / spos_token_supply
    curve_fee = fee * curve_coefficient
    new_idp_for_invariant = idp + fee - curve_fee
    to_mint_tokens = new_idp_for_invariant / invariant - spos_token_supply
    idp += fee
    spos_token_supply += to_mint_tokens


def test():
    global idp, spos_token_supply
    n = 30000  # total payments
    np.random.seed(1234)
    payments = np.random.rand(n) * 20  # random payments up to 20 DAI
    # token prices in DAI after payments
    token_prices = [idp / spos_token_supply]
    pools = [idp]
    tokens = [spos_token_supply]
    for i in range(n):
        process_incoming_DAI_fee(payments[i])
        token_prices.append(idp / spos_token_supply)
        pools.append(idp)
        tokens.append(spos_token_supply)

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
    ax1.plot(token_prices, label="token price in DAI")
    ax1.legend(loc='upper left')
    ax2.plot(pools, label="incentivization DAI pool")
    ax2.legend(loc='upper left')
    ax3.plot(tokens, label="tokens")
    ax3.legend(loc='upper left')
    plt.show()
