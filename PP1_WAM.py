#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:50:48 2024

@author: williammuckler
"""
#interface start
import streamlit as st


st.title("Financial Ratio Calculator")
st.divider()
 
tab1, tab2, tab3 = st.tabs(['Liquidity','Profitability','Market Prospect'])

with tab1:
    st.header('Liquidity Ratios') 
    st.write("Liquidity ratios measure how well a company can pay short-term debt obligations.")
    st.write("Check all ratios you would like to solve.")
    current_ratio=st.checkbox("Current Ratio",key='cr')
    quick_ratio = st.checkbox("Quick Ratio",key='qr')
    days_sales_outstanding = st.checkbox("Days Sales Outstanding")
    
    
    #funtions: Liquidity Ratios
    def liquid_ratio(ca,cl,inv,ar,rev):
        cr=ca/cl
        qr=(ca-inv)/cl
        dso=ar/(rev/365)
        return cr,qr,dso
    
    
    #inputs, value=1 to eliminate a divide by 0 error
    st.write('**Inputs**')
    ca=st.number_input("Enter the Current Assets of your Company.", value=1)
    cl=st.number_input("Enter the Current Liabilities of your Company.",value =1)
    inv=st.number_input("Enter the inventory of your Company.",value=1)
    ar=st.number_input("Enter the Accounts Receivable of your Company.",value=1)
    rev=st.number_input("Enter the revenue of your Company.",value=1)
    
    cr,qr,dso = liquid_ratio(ca,cl,inv,ar,rev)
    st.write("")
    c_name = st.text_input("Enter the name of your company.")
    st.write("")
    st.divider()
    st.write('**Results**')
    st.divider()
    if current_ratio:
        st.write("Current Ratio = CA/CL")
        st.write(f'The **current ratio** of your company is **{cr}**.')
        analysis_cr = st.checkbox("Analysis of Current Ratio")
        if analysis_cr:
            st.write("A healthy current ratio falls between 1.2 and 2. Below this range, the business may not have enough liquid assets to cover short term liabilities. Above this range, the company may not be using assets efficiently.")
        st.divider()
    if quick_ratio:
        st.write("Quick Ratio = (CA-Inv)/CL")
        st.write(f'The **Quick Ratio** of your company is **{qr}**.')
        analysis_qr= st.checkbox("Analysis of Quick Ratio")
        if analysis_qr:
            st.write("A healthy quick ratio falls between 1 and 2. Below this range, the business may not have enough liquid assets to cover short term liabilities. Above this range, the company may not be using assets efficiently. ")
        st.divider()
    if days_sales_outstanding:
        st.session_state['ca']=False
        st.write("Days Sales Outstanding=AR/(REV/365)")
        st.write(f'The **Days Sales Outstanding** of your company is **{dso}** days.')
        analysis_dso= st.checkbox("Analysis of Days Sales Outstanding")
        if analysis_dso:
            st.write("A healthy number for days sales outstanding is 45. Above this number, a business may be taking too long to collect payment from sales.")
        st.divider()
        
    
    write_tf_liq=st.button("Write to File")
    if write_tf_liq:
        with open('file.csv','w') as f:
            print(f'Company:{c_name},Current Ratio= {cr}, Quick Ratio = {qr}, Days Sales Outstanding= {dso}',file=f)
    st.divider()
            
          
          
          
    st.write("""
              **KEY:**  
              CA=Current Assets  
              CL=Current Liabilities    
              Inv=Inventory  
              AR=Accounts Receivable  
              REV=Revenue
              """)
     
              
     
with tab2:
    st.header('Profitability Ratios')
    st.write("Profitability Ratios measure a business's ability to generate earnings relative to assets, operations, or equity.")
    st.write("Check all ratios you would like to solve.")
    gross_margin=st.checkbox("Gross Margin")
    return_on_assets = st.checkbox("Return on Assets")
    return_on_equity = st.checkbox("Return on Equity")
    
    #funcitons: profitability ratios
    def profit_ratio(p,rev1,ta,se):
        gm=p/rev1
        roa=p/ta
        roe=p/se
        return gm,roa,roe
    
    st.write('**Inputs**')
    p= st.number_input("Enter the Gross Profit of your company.", value=1)
    rev1 = st.number_input("Enter the total revenue of your company.",value=1) 
    ta=st.number_input("Enter the total assets of your company.",value=1)
    se=st.number_input("Enter the total shareholder equity of your company.",value=1)
    
    st.write("")
    c_name_prof = st.text_input("Enter the name of your company")
    st.write("")
    
    gm,roa,roe = profit_ratio(p,rev,ta,se)
    
    st.divider()
    st.write('**Results**')
    st.divider()
    
    if gross_margin:
        st.write("Gross Margin=P/REV")
        st.write(f'The **Profit Margin** of your company is **{gm}** or **{gm*100}%**.')
        analysis_gm = st.checkbox('Analysis of Gross Margin')
        if analysis_gm:
            st.write('Gross margin varies by industry. Generally, a margin greater than 10% is considered good.')
        st.divider()
        
    if return_on_assets:
        st.write('Return on Assets=P/TA')
        st.write(f"The **Return on Assets** of your comapny is **{roa}** or **{roa*100}%**.")
        analysis_roa=st.checkbox("Analysis of Return on Assets")
        if analysis_roa:
            st.write("A generally healthy return on assets is above 10%. Firms should be compared to firms within their industry.")
        st.divider()
        
    if return_on_equity:
        st.write("Return on Equity=P/SE")
        st.write(f'The **Return on Equity** of your company is **{roe}** or **{roe*100}%**.')
        analysis_roe = st.checkbox("Analysis of Return on Equity")
        if analysis_roe:
            st.write("A return on equity between 15%-20% is considered good. This shows the ability of management to generatge revenue through equity.")
        st.divider()
            
    
    write_tf_prof=st.button("Write to File!")
    if write_tf_prof:
        with open('file.csv','w') as f:
            print(f'compamy:{c_name_prof},Gross margin = {gm}, ROA={roa}, ROE={roe}',file=f)
        
                    



    st.divider()
    st.write("""
                **KEY:**  
               P=Total Profit  
               REV=Revenue  
               TA=Total Assets  
               SE=Shareholder Equity
               """)
              
with tab3:
    st.header('Market Prospect Ratios')
    st.write("Market Prospect Ratios allow analysts to predict future earnings and performance.")
    price_to_earnings = st.checkbox('Earnings per Share, Price to Earnings')
    dividend_yield=st.checkbox("Dividend per Share, Dividend Yield")
    dividend_payout = st.checkbox("Dividend Payout Ratio")
    
    def mp_ratio(rev,psd,waso,sp,d,os):
        eps=(rev-psd)/waso
        pe=sp/eps
        dps=d/os
        dy=dps/sp
        dp=dps/eps
        return eps,pe,dps,dy,dp
    
    st.write('**Inputs**')
    rev=st.number_input(' Enter the revenue of your company.',value=2)
    psd = st.number_input("Enter the amount of preferred share dividents paid, if any.",value=1)
    waso=st.number_input("Enter the weighted average of shares outstanding.",value=1)
    sp=st.number_input("Enter the share price of the company.",value=1)
    d=st.number_input("Enter the amount of dividends paid.",value=1)
    os=st.number_input("Enter the number of shares outstanding.",value=1)
    
    st.write("")
    c_name_mp = st.text_input("Enter the name of your company!")
    st.write("")
    
    eps,pe,dps,dy,dp=mp_ratio(rev,psd,waso,sp,d,os)
    
    
    st.divider()
    st.write('**Results**')
    st.divider()
    
    if price_to_earnings:
        st.write("""
                 Earnings per Share = (Rev-PSD)/WASO  
                 Price to Earnings = SP/EPS
                 """)
        st.write(f'The **Earnings per Share** of your company is {eps}.')
        eps_analysis = st.checkbox("Analysis of Earnings per Share")
        if eps_analysis:
            st.write("The higher the EPS, the more profitable the company. Generally, you want EPS to be increasing by quarter.")
        st.write(f'The **Price to Earnings** of your company is {pe}.')
        pe_analysis=st.checkbox("Analysis of Price to Earnings")
        if pe_analysis:
            st.write("A good P/E ratio is around 20 to 25. The lower the number, the better the investment.")
     
        st.divider()
    
    if dividend_yield:
        st.write("""
                 Dividends per Share= D/OS  
                 Dividend Yield = DPS/SP
                 """)

        st.write(f"The **Dividends per Share** for your company is {dps}")
        dps_analysis=st.checkbox("Analysis of Dividends per Share")
        if dps_analysis:
            st.write("This tells us the amount of dividend per individual share. For investors, a higher number is generally better.")
        st.write(f'The **Dividend Yield** of your company is {dy} or {dy*100}%.')
        dy_analysis=st.checkbox("Analysis of Dividend Yeild")
        if dy_analysis:
            st.write("2%-6% are considered good. Although each investment has different standards.")
        st.divider()
        
    if dividend_payout:
        st.write("Dividend Payout=DPS/EPS")
        st.write(f'The **Dividend Payout** of your company is **{dp}** or **{dp*100}%**.')
        dp_analysis = st.checkbox("Analysis of Dividend Payout")
        if dp_analysis:
            st.write("A healthy dividend payout ratio is between 30% and 50%. Above this may be unsubstantial.")
        st.divider()
    
    
    
    
    
    
    write_tf_mp=st.button("Write to File.")
    if write_tf_mp:
        with open('file.csv','w') as f:
            print(f'compamy:{c_name_mp}, EPS={eps}, P/E={pe}, DPS={dps},DY={dy},DP={dp}',file=f)
    st.divider()
    
    
    st.write("""
             **KEY:**  
             Rev=Revenue  
             PSD=Preferred Share Dividends  
             WASO=Weighted Average Shares Outstanding  
             SP=Share Price  
             EPS=Earnings per Share  
             D=Dividends Paid  
             OS=Outstanding Shares  
             DPS=Dividends per Share  
             """)
    

              
        
                 
    
    