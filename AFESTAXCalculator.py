#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 12:28:25 2025

@author: Bronze
"""

import streamlit as st

def calculate_total_with_taxes(contract_sum):
    GETFundNHILtax = 0.05
    COVID_levytax = 0.01
    VATtax = 0.15

    GETFund_NHIL = contract_sum * GETFundNHILtax
    subtotal_1 = contract_sum + GETFund_NHIL
    COVID_levy = contract_sum * COVID_levytax
    subtotal_2 = subtotal_1 + COVID_levy
    VAT = subtotal_2 * VATtax
    grand_total = subtotal_2 + VAT

    return GETFund_NHIL,subtotal_1, COVID_levy,subtotal_2, VAT, grand_total

st.title(" AFES Ghana Tax Calculator")

contract_sum = st.number_input("Enter Contract Sum (GHS)", min_value=0.0, step=100.0)

if st.button("Calculate"):
    getfund_nhil, subtotal_1, covid_levy, subtotal_2, vat, total = calculate_total_with_taxes(contract_sum)
    
    st.write(f"**NHIL/GETFund (5%)**: GHS {getfund_nhil:,.2f}")
    st.write(f"SUBTOTAL(1): GHS {subtotal_1:,.2f}")
    st.write(f"**COVID Levy (1%)**: GHS {covid_levy:,.2f}")
    st.write(f"SUBTOTAL(2): GHS {subtotal_2:,.2f}")
    st.write(f"**VAT (15%)**: GHS {vat:,.2f}")
    st.success(f"**Grand Total: GHS {total:,.2f}**")
