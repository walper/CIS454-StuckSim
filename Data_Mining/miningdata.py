import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials

# tsla_df = yf.download('TSLA', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# tsla_df.head()
# print(tsla_df)
# tsla_df.to_csv(r'C:\Users\gudas\CIS454\TSLA.csv', encoding='utf-8')


# aapl_df = yf.download('AAPL', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# aapl_df.head()
# print(aapl_df)
# aapl_df.to_csv(r'C:\Users\gudas\CIS454\AAPL.csv', encoding='utf-8')


# amc_df = yf.download('AMC', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# amc_df.head()
# print(amc_df)
# amc_df.to_csv(r'C:\Users\gudas\CIS454\AMC.csv', encoding='utf-8')


# amzn_df = yf.download('AMZN', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# amzn_df.head()
# print(amzn_df)
# amzn_df.to_csv(r'C:\Users\gudas\CIS454\AMZN.csv', encoding='utf-8')


# bb_df = yf.download('BB', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# bb_df.head()
# print(bb_df)
# bb_df.to_csv(r'C:\Users\gudas\CIS454\BB.csv', encoding='utf-8')


# cprx_df = yf.download('CPRX', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# cprx_df.head()
# print(cprx_df)
# cprx_df.to_csv(r'C:\Users\gudas\CIS454\CPRX.csv', encoding='utf-8')


# aal_df = yf.download('AAL', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# aal_df.head()
# print(aal_df)
# aal_df.to_csv(r'C:\Users\gudas\CIS454\AAL.csv', encoding='utf-8')

# nvda_df = yf.download('NVDA', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# nvda_df.head()
# print(nvda_df)
# nvda_df.to_csv(r'C:\Users\gudas\CIS454\NVDA.csv', encoding='utf-8')

# plug_df = yf.download('PLUG', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# plug_df.head()
# print(plug_df)
# plug_df.to_csv(r'C:\Users\gudas\CIS454\PLUG.csv', encoding='utf-8')


# gpro_df = yf.download('GPRO', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# gpro_df.head()
# print(gpro_df)
# gpro_df.to_csv(r'C:\Users\gudas\CIS454\GPRO.csv', encoding='utf-8')


# baba_df = yf.download('BABA', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# baba_df.head()
# print(baba_df)
# baba_df.to_csv(r'C:\Users\gudas\CIS454\BABA.csv', encoding='utf-8')


# cll_df = yf.download('CCL', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# cll_df.head()
# print(cll_df)
# cll_df.to_csv(r'C:\Users\gudas\CIS454\CLL.csv', encoding='utf-8')


# acb_df = yf.download('ACB', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# acb_df.head()
# print(acb_df)
# acb_df.to_csv(r'C:\Users\gudas\CIS454\ACB.csv', encoding='utf-8')


# zom_df = yf.download('ZOM', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# zom_df.head()
# print(zom_df)
# zom_df.to_csv(r'C:\Users\gudas\CIS454\ZOM.csv', encoding='utf-8')


# voo_df = yf.download('VOO', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# voo_df.head()
# print(voo_df)
# voo_df.to_csv(r'C:\Users\gudas\CIS454\VOO.csv', encoding='utf-8')


# nok_df = yf.download('NOK', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# nok_df.head()
# print(nok_df)
# nok_df.to_csv(r'C:\Users\gudas\CIS454\nok.csv', encoding='utf-8')


# spy_df = yf.download('SPY', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# spy_df.head()
# print(spy_df)
# spy_df.to_csv(r'C:\Users\gudas\CIS454\SPY.csv', encoding='utf-8')


# dal_df = yf.download('DAL', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# dal_df.head()
# print(dal_df)
# dal_df.to_csv(r'C:\Users\gudas\CIS454\DAL.csv', encoding='utf-8')


# bac_df = yf.download('BAC', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# bac_df.head()
# print(bac_df)
# bac_df.to_csv(r'C:\Users\gudas\CIS454\BAC.csv', encoding='utf-8')


# pltr_df = yf.download('PLTR', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# pltr_df.head()
# print(pltr_df)
# pltr_df.to_csv(r'C:\Users\gudas\CIS454\PLTR.csv', encoding='utf-8')


# gme_df = yf.download('GME', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# gme_df.head()
# print(gme_df)
# gme_df.to_csv(r'C:\Users\gudas\CIS454\GME.csv', encoding='utf-8')


# sbux_df = yf.download('SBUX', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# sbux_df.head()
# print(sbux_df)
# sbux_df.to_csv(r'C:\Users\gudas\CIS454\SBUX.csv', encoding='utf-8')


# amd_df = yf.download('AMD', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# amd_df.head()
# print(amd_df)
# amd_df.to_csv(r'C:\Users\gudas\CIS454\AMD.csv', encoding='utf-8')


# ogi_df = yf.download('OGI', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# ogi_df.head()
# print(ogi_df)
# ogi_df.to_csv(r'C:\Users\gudas\CIS454\OGI.csv', encoding='utf-8')


# tlry_df = yf.download('TLRY', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# tlry_df.head()
# print(tlry_df)
# tlry_df.to_csv(r'C:\Users\gudas\CIS454\TLRY.csv', encoding='utf-8')


# coin_df = yf.download('COIN', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# coin_df.head()
# print(coin_df)
# coin_df.to_csv(r'C:\Users\gudas\CIS454\COIN.csv', encoding='utf-8')


# twtr_df = yf.download('TWTR', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# twtr_df.head()
# print(twtr_df)
# twtr_df.to_csv(r'C:\Users\gudas\CIS454\TWTR.csv', encoding='utf-8')


# t_df = yf.download('T', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# t_df.head()
# print(t_df)
# t_df.to_csv(r'C:\Users\gudas\CIS454\T.csv', encoding='utf-8')


# mrna_df = yf.download('MRNA', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# mrna_df.head()
# print(mrna_df)
# mrna_df.to_csv(r'C:\Users\gudas\CIS454\MRNA.csv', encoding='utf-8')


# cgc_df = yf.download('CGC', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# cgc_df.head()
# print(cgc_df)
# cgc_df.to_csv(r'C:\Users\gudas\CIS454\CGC.csv', encoding='utf-8')


# rivn_df = yf.download('RIVN', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# rivn_df.head()
# print(rivn_df)
# rivn_df.to_csv(r'C:\Users\gudas\CIS454\RIVN.csv', encoding='utf-8')


# ko_df = yf.download('KO', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# ko_df.head()
# print(ko_df)
# ko_df.to_csv(r'C:\Users\gudas\CIS454\KO.csv', encoding='utf-8')


# spce_df = yf.download('SPCE', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# spce_df.head()
# print(spce_df)
# spce_df.to_csv(r'C:\Users\gudas\CIS454\SPCE.csv', encoding='utf-8')


# fcel_df = yf.download('FCEL', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# fcel_df.head()
# print(fcel_df)
# fcel_df.to_csv(r'C:\Users\gudas\CIS454\FCEL.csv', encoding='utf-8')


# googl_df = yf.download('GOOGL', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# googl_df.head()
# print(googl_df)
# googl_df.to_csv(r'C:\Users\gudas\CIS454\GOOGL.csv', encoding='utf-8')


# rycey_df = yf.download('RYCEY', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# rycey_df.head()
# print(rycey_df)
# rycey_df.to_csv(r'C:\Users\gudas\CIS454\RYCEY.csv', encoding='utf-8')


# f_df = yf.download('F', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# f_df.head()
# print(f_df)
# f_df.to_csv(r'C:\Users\gudas\CIS454\F.csv', encoding='utf-8')


# nio_df = yf.download('NIO', 
#                       start='2021-01-01', 
#                       end='2021-12-31', 
#                       progress=False)
# nio_df.head()
# print(nio_df)
# nio_df.to_csv(r'C:\Users\gudas\CIS454\NIO.csv', encoding='utf-8')


# pfe_df = yf.download('PFE', 
#                        start='2021-01-01', 
#                        end='2021-12-31', 
#                        progress=False)
# pfe_df.head()
# print(pfe_df)
# pfe_df.to_csv(r'C:\Users\gudas\CIS454\PFE.csv', encoding='utf-8')


# fb_df = yf.download('FB', 
#                        start='2021-01-01', 
#                        end='2021-12-31', 
#                        progress=False)
# fb_df.head()
# print(fb_df)
# fb_df.to_csv(r'C:\Users\gudas\CIS454\FB.csv', encoding='utf-8')


dis_df = yf.download('DIS', 
                       start='2021-01-01', 
                       end='2021-12-31', 
                       progress=False)
dis_df.head()
print(dis_df)
dis_df.to_csv(r'C:\Users\gudas\CIS454\DIS.csv', encoding='utf-8')


hood_df = yf.download('HOOD', 
                       start='2021-01-01', 
                       end='2021-12-31', 
                       progress=False)
hood_df.head()
print(hood_df)
hood_df.to_csv(r'C:\Users\gudas\CIS454\HOOD.csv', encoding='utf-8')


lcid_df = yf.download('LCID', 
                       start='2021-01-01', 
                       end='2021-12-31', 
                       progress=False)
lcid_df.head()
print(lcid_df)
lcid_df.to_csv(r'C:\Users\gudas\CIS454\LCID.csv', encoding='utf-8')


pton_df = yf.download('PTON', 
                       start='2021-01-01', 
                       end='2021-12-31', 
                       progress=False)
pton_df.head()
print(pton_df)
pton_df.to_csv(r'C:\Users\gudas\CIS454\PTON.csv', encoding='utf-8')


rivn_df = yf.download('RIVN', 
                       start='2021-01-01', 
                       end='2021-12-31', 
                       progress=False)
rivn_df.head()
print(rivn_df)
rivn_df.to_csv(r'C:\Users\gudas\CIS454\RIVN.csv', encoding='utf-8')


snap_df = yf.download('SNAP', 
                       start='2021-01-01', 
                       end='2021-12-31', 
                       progress=False)
snap_df.head()
print(snap_df)
snap_df.to_csv(r'C:\Users\gudas\CIS454\SNAP.csv', encoding='utf-8')


sndl_df = yf.download('SNDL', 
                       start='2021-01-01', 
                       end='2021-12-31', 
                       progress=False)
sndl_df.head()
print(sndl_df)
sndl_df.to_csv(r'C:\Users\gudas\CIS454\SNDL.csv', encoding='utf-8')


wish_df = yf.download('WISH', 
                       start='2021-01-01', 
                       end='2021-12-31', 
                       progress=False)
wish_df.head()
print(wish_df)
wish_df.to_csv(r'C:\Users\gudas\CIS454\WISH.csv', encoding='utf-8')


msft_df = yf.download('MSFT', 
                       start='2021-01-01', 
                       end='2021-12-31', 
                       progress=False)
msft_df.head()
print(msft_df)
msft_df.to_csv(r'C:\Users\gudas\CIS454\MSFT.csv', encoding='utf-8')


nflx_df = yf.download('NFLX', 
                       start='2021-01-01', 
                       end='2021-12-31', 
                       progress=False)
nflx_df.head()
print(nflx_df)
nflx_df.to_csv(r'C:\Users\gudas\CIS454\NFLX.csv', encoding='utf-8')














