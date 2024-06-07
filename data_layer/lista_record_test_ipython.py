from decimal import Decimal
from data_layer.record_smf import Record_smf
from datetime import datetime
import pandas as pd

lista_smf = []

_rec_smf = Record_smf()
_rec_tran = 'Y1TR'
_rec_smf.START = datetime(2023,5,29,20,33,45,234568)
_rec_smf.STOP = datetime(2023,5,29,20,33,45,235568)
_delta = _rec_smf.STOP - _rec_smf.START
_microsecs = Decimal(_delta.microseconds) / Decimal(1000000)
_secs = Decimal(_delta.seconds) + Decimal(_microsecs)
_rec_smf.ELAPSED = _secs
_rec_smf.TRANNUM = '65676'
_rec_smf.PGMNAME = 'Y1ORCUT0'
_rec_smf.OAPPLID = 'Y2A4670B'
_rec_smf.USRCPUT = _secs
lista_smf.append(_rec_smf)

_rec_smf_02 = Record_smf()
_rec_smf_02.TRAN = 'Y2TM'
_rec_smf_02.START = datetime(2023,5,29,20,33,45,234568)
_rec_smf_02.STOP = datetime(2023,5,29,20,33,45,235568)
_delta = _rec_smf_02.STOP - _rec_smf_02.START
_microsecs = Decimal(_delta.microseconds) / Decimal(1000000)
_secs = Decimal(_delta.seconds) + Decimal(_microsecs)
_rec_smf.ELAPSED = _secs
_rec_smf_02.TRANNUM = '65676'
_rec_smf_02.PGMNAME = 'Y1ORCUT0'
_rec_smf_02.OAPPLID = 'Y2A4670B'
_rec_smf_02.USRCPUT = _secs
lista_smf.append(_rec_smf_02)

_rec_smf_03 = Record_smf()
_rec_smf_03.TRAN = 'Y3MT'
_rec_smf_03.START = datetime(2023,5,29,20,33,45,224568)
_rec_smf_03.STOP = datetime(2023,5,29,20,33,45,235668)
_delta = _rec_smf_03.STOP - _rec_smf_03.START
_microsecs = Decimal(_delta.microseconds) / Decimal(1000000)
_secs = Decimal(_delta.seconds) + Decimal(_microsecs)
_rec_smf.ELAPSED = _secs
_rec_smf_03.TRANNUM = '65676'
_rec_smf_03.PGMNAME = 'Y1ORCUT0'
_rec_smf_03.OAPPLID = 'Y2A4670B'
_rec_smf_03.USRCPUT = _secs
lista_smf.append(_rec_smf_03)

_rec_smf_04 = Record_smf()
_rec_smf_04.TRAN = 'Y6$§'
_rec_smf_04.START = datetime(2023,5,29,20,33,45,234568)
_rec_smf_04.STOP = datetime(2023,5,29,20,33,45,245568)
_delta = _rec_smf_04.STOP - _rec_smf_04.START
_microsecs = Decimal(_delta.microseconds) / Decimal(1000000)
_secs = Decimal(_delta.seconds) + Decimal(_microsecs)
_rec_smf.ELAPSED = _secs
_rec_smf_04.TRANNUM = '65676'
_rec_smf_04.PGMNAME = 'Y1ORCUT0'
_rec_smf_04.OAPPLID = 'Y2A4670B'
_rec_smf_04.USRCPUT = _secs
lista_smf.append(_rec_smf_04)

lista_smf_dict = [x.__dict__ for x in lista_smf]

df = pd.DataFrame.from_dict(lista_smf_dict)

df = df[['TRAN', 'START', 'STOP', 'ELAPSED', 'TRANNUM', 'PGMNAME', 'OAPPLID', 'USRCPUT']]

df[['ELAPSED', 'USRCPUT']] = df[['ELAPSED', 'USRCPUT']].astype(float)