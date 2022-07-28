# Library

!pip install numpy 
import numpy as np

!pip install pandas 
import pandas as pd

!pip install math 
import math as mat

# Definição dos dados
tipo_v={"CAR":{"num":0,"cap_V":25000 ,"tim_V":6 } ,"BIT":{"num":1,"cap_V":42000,"tim_V":8},"TRU":{"num":2,"cap_V":15000,"tim_V":3}}

filial={0: {"Acro":"BAU"   ,"cidade":"BAURU"                 , "UF":"SP"       ,	"Tipo":"Normal"   ,	"cap_R" : 150000    ,"cap_E": 	200000 },
        1:  {"Acro":"BHZ"   ,"cidade":"BELO HORIZONTE"        , "UF":"MG"       ,	"Tipo":"XD"	      ,	"cap_R" : 650000    ,"cap_E":  1175000 },
        2:  {"Acro":"BSB"   ,"cidade":"BRASÍLIA"              ,	"UF":"DF"       ,	"Tipo":"Normal"	  ,	"cap_R" : 400000    ,"cap_E":   575000 },
        3:  {"Acro":"CPQ"   ,"cidade":"CAMPINAS"              ,	"UF":"SP"	    ,	"Tipo":"XD"	      ,	"cap_R" :2900000    ,"cap_E":  3025000 },
        4:  {"Acro":"CWB"   ,"cidade":"CURITIBA"              ,	"UF":"PR"	    ,	"Tipo":'Normal'	  ,	"cap_R" :1200000    ,"cap_E":  1250000 },
        5:  {"Acro":"FEC"   ,"cidade":"FEIRA DE SANTANA"      ,	"UF":"BA"       ,	"Tipo":"XD"       ,	"cap_R" :2000000    ,"cap_E":  2225000 },
        6:  {"Acro":"FLN"   ,"cidade":'FLORIANOPOLIS'         ,	"UF":"SC"       ,	"Tipo":"Normal"	  ,	"cap_R" : 325000 	,"cap_E":   300000 },
        7:  {"Acro":"FOR"   ,"cidade":"FORTALEZA"	          ,	"UF":"CE"       ,	"Tipo":'Normal'   ,	"cap_R" :1125000 	,"cap_E":  2050000 },
        8:  {"Acro":"NAT"   ,"cidade":'NATAL'                 ,	"UF":'RN'       ,	"Tipo":"Normal"	  ,	"cap_R" : 100000 	,"cap_E":   300000 },
        9: {"Acro":"SPC"   ,"cidade":"SAO PAULO"	          ,	"UF":"SP"	    ,	"Tipo":"XD"	      ,	"cap_R" :3275000 	,"cap_E":  5825000 },
        10: {"Acro":"POA"   ,"cidade":'PORTO ALEGRE'          ,	"UF":"RS"	    ,	"Tipo":'Normal'   ,	"cap_R" : 925000    ,"cap_E":  1450000 },
        11: {"Acro":"SJP"   ,"cidade":"SAO JOSE DO RIO PRETO" ,	"UF":"SP"       ,	"Tipo":'Normal'	  ,	"cap_R" : 275000 	,"cap_E":   175000 },
        12: {"Acro":"SSZ"   ,"cidade":"SANTOS"	              ,	"UF":"SP"	    ,	"Tipo":"Normal"	  ,	"cap_R" :  25000 	,"cap_E":    25000 }
        }
    
# dados de demanda
destinos={ "BAU":{1:    {"des":"BHZ","Dem": 923 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 7   } ,
                    2:      {"des":"BSB","Dem": 84  ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 7   } ,
                    3:      {"des":"CPQ","Dem": 310 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 4   } ,
                    4:      {"des":"CWB","Dem": 451 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 7   } ,
                    5:      {"des":"FEC","Dem": 93  ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 12  } ,
                    6:      {"des":"FLN","Dem": 12  ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 8   } ,
                    7:      {"des":"FOR","Dem": 38  ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 13  } ,
                    8:      {"des":"NAT","Dem": 313 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 13  } ,
                    9:      {"des":"SPC","Dem": 6   ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15  } ,
                    10:      {"des":"POA","Dem": 60  ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 8   } ,
                    11:     {"des":"SJP","Dem": 51  ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 6   } ,
                    12:     {"des":"SSZ","Dem": 86  ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 6   } ,
                    0:     {"des": None}
                     },
               
         "BHZ":{0:      {"des":"BAU","Dem": 95 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 9 },
                    2:      {"des":"BSB","Dem": 287 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 6 },
                    3:      {"des":"CPQ","Dem": 81 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 8 },
                    4:      {"des":"CWB","Dem": 634 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 10 },
                    5:      {"des":"FEC","Dem": 1291,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 8 },
                    6:      {"des":"FLN","Dem": 29 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 10 },
                    7:      {"des":"FOR","Dem": 1557,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 13 },
                    8:      {"des":"NAT","Dem": 1318,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 13 },
                    9:      {"des":"SPC","Dem": 118 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    10:      {"des":"POA","Dem": 360 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 10 },
                    11:     {"des":"SJP","Dem": 142 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 10 },
                    12:     {"des":"SSZ","Dem": 43 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 8 },
                    1:      {"des": None}

                    },
          "BSB":{0:	{"des":"BAU","Dem": 9 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 11 },
                    1:  	{"des":"BHZ","Dem": 11 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 9 },
                    3:  	{"des":"CPQ","Dem": 35 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 8 },
                    4:  	{"des":"CWB","Dem": 13 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 9 },
                    5:  	{"des":"FEC","Dem": 411 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 14 },
                    6:  	{"des":"FLN","Dem": 68 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 14 },
                    7:  	{"des":"FOR","Dem": 323 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 16 },
                    8:  	{"des":"NAT","Dem": 283 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    9:  	{"des":"SPC","Dem": 124 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    10:  	{"des":"POA","Dem": 10 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 14 },
                    11: 	{"des":"SJP","Dem": 25 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 9 },
                    12:	    {"des":"SSZ","Dem": 0 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 10 },
                    2:      {"des": None}
                    },
        "CPQ":{0:	{"des":"BAU","Dem": 1454,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 6 },
                    1:	{"des":"BHZ","Dem": 3634,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 6 },
                    2:	{"des":"BSB","Dem": 1000,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 6 },
                    4:	{"des":"CWB","Dem": 5057,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 6 },
                    5:	{"des":"FEC","Dem": 793 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 11 },
                    6:	{"des":"FLN","Dem": 965 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 7 },
                    7:	{"des":"FOR","Dem": 7414,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 11 },
                    8:	{"des":"NAT","Dem": 1855,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 11 },
                    9:	{"des":"SPC","Dem": 8 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    10:	{"des":"POA","Dem": 4703,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 7 },
                    11:	{"des":"SJP","Dem": 3817,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 6 },
                    12:	{"des":"SSZ","Dem": 451 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 6 },
                    3:  {"des": None}
                   },
        "CWB":{0:	{"des":"BAU","Dem": 141 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 8 },
                    1:	{"des":"BHZ","Dem": 156 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 7 },
                    2:	{"des":"BSB","Dem": 471 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 8 },
                    3:	{"des":"CPQ","Dem": 551 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 6 },
                    5:	{"des":"FEC","Dem": 510 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    6:	{"des":"FLN","Dem": 15 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 8 },
                    7:	{"des":"FOR","Dem": 1359,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 14 },
                    8:	{"des":"NAT","Dem": 673 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    9:	{"des":"SPC","Dem": 26 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    10:	{"des":"POA","Dem": 37 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 4 },
                    11:	{"des":"SJP","Dem": 125 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 8 },
                    12:	{"des":"SSZ","Dem": 68 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 8 },
                    4:  {"des": None}
                    },
        "FEC":{0:	{"des":"BAU","Dem": 2 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 10 },
                    1:	{"des":"BHZ","Dem": 150 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 12 },
                    2:	{"des":"BSB","Dem": 549 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 12 },
                    3:	{"des":"CPQ","Dem": 54 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 11 },
                    4:	{"des":"CWB","Dem": 29 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 17 },
                    6:	{"des":"FLN","Dem": 23 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 16 },
                    7:	{"des":"FOR","Dem": 2010,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 9 },
                    8:	{"des":"NAT","Dem": 789 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 13 },
                    9:	{"des":"SPC","Dem": 27 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    10:	{"des":"POA","Dem": 11 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 13 },
                    11:	{"des":"SJP","Dem": 16 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 14 },
                    12:	{"des":"SSZ","Dem": 103 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 12 },
                    5:  {"des": None}
                   },
        "FLN":{0:	{"des":"BAU","Dem": 154 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 7 },
                    1:	{"des":"BHZ","Dem": 710 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 7 },
                    2:	{"des":"BSB","Dem": 1032,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 7 },
                    3:	{"des":"CPQ","Dem": 215 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 5 },
                    4:	{"des":"CWB","Dem": 515 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 6 },
                    5:	{"des":"FEC","Dem": 236 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    7:	{"des":"FOR","Dem": 1753,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 12 },
                    8:	{"des":"NAT","Dem": 538 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 14 },
                    9:	{"des":"SPC","Dem": 443 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    10:	{"des":"POA","Dem": 200 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 5 },
                    11:	{"des":"SJP","Dem": 183 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 7 },
                    12:	{"des":"SSZ","Dem": 48 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 6 },
                    6:  {"des": None}
                   },
        "FOR":{0:	{"des":"BAU","Dem": 614 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 12 },
                    1:	{"des":"BHZ","Dem": 1292,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 12 },
                    2:	{"des":"BSB","Dem": 206 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 13 },
                    3:	{"des":"CPQ","Dem": 528 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 11 },
                    4:	{"des":"CWB","Dem": 793 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 13 },
                    5:	{"des":"FEC","Dem": 164 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 11 },
                    6:	{"des":"FLN","Dem": 238 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 14 },
                    8:	{"des":"NAT","Dem": 11 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 8 },
                    9:	{"des":"SPC","Dem":32155 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    10:	{"des":"POA","Dem": 856 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 16 },
                    11:	{"des":"SJP","Dem": 516 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 13 },
                    12:	{"des":"SSZ","Dem": 137 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 12 },
                    
                    7:  {"des": None}
                   },
        "NAT":{0:	{"des":"BAU","Dem": 4 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 16 },
                    1:	{"des":"BHZ","Dem": 796 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 14 },
                    2:	{"des":"BSB","Dem": 62 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 9 },
                    3:	{"des":"CPQ","Dem": 31 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 10 },
                    4:	{"des":"CWB","Dem": 195 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 8 },
                    5:	{"des":"FEC","Dem": 188 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 11 },
                    6:	{"des":"FLN","Dem": 39 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    7:	{"des":"FOR","Dem": 661 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 11 },
                    9:	{"des":"SPC","Dem": 40 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    10:	{"des":"POA","Dem": 50 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 11 },
                    11:	{"des":"SJP","Dem": 0 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 17 },
                    12:	{"des":"SSZ","Dem": 43 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 17 },
                    8:  {"des": None}
                   },
        "SPC":{0:	{"des":"BAU","Dem": 392 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    1:	{"des":"BHZ","Dem": 2599,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    2:	{"des":"BSB","Dem": 4657,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    3:	{"des":"CPQ","Dem": 1845,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    4:	{"des":"CWB","Dem": 5911,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    5:	{"des":"FEC","Dem": 1645,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    6:	{"des":"FLN","Dem": 1883,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    7:	{"des":"FOR","Dem":12875 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    8:	{"des":"NAT","Dem": 5212,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    10:	{"des":"POA","Dem": 5955,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    11:	{"des":"SJP","Dem": 532 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    12:	{"des":"SSZ","Dem": 667 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    9:  {"des": None}
                   },
        "POA":{0:	{"des":"BAU","Dem": 251 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 8 },
                    1:	{"des":"BHZ","Dem": 785 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 7 },
                    2:	{"des":"BSB","Dem": 728 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 10 },
                    3:	{"des":"CPQ","Dem": 706 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 6 },
                    4:	{"des":"CWB","Dem": 392 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 6 },
                    5:	{"des":"FEC","Dem": 79 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 14 },
                    6:	{"des":"FLN","Dem": 234 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 5 },
                    7:	{"des":"FOR","Dem": 526 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 14 },
                    8:	{"des":"NAT","Dem": 404 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    9:	{"des":"SPC","Dem": 98 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    11:	{"des":"SJP","Dem": 130 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 7 },
                    12:	{"des":"SSZ","Dem": 112 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 6 },
                    10:  {"des": None}
                   },
        "SJP":{0:	{"des":"BAU","Dem": 189 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 10 },
                    1:	{"des":"BHZ","Dem": 338 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 12 },
                    2:	{"des":"BSB","Dem": 657 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 10 },
                    3:	{"des":"CPQ","Dem": 52 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 8 },
                    4:	{"des":"CWB","Dem": 443 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 8 },
                    5:	{"des":"FEC","Dem": 846 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 17 },
                    6:	{"des":"FLN","Dem": 212 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 10 },
                    7:	{"des":"FOR","Dem": 349 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 10 },
                    8:	{"des":"NAT","Dem": 218 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 16 },
                    9:	{"des":"SPC","Dem": 40 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    10:	{"des":"POA","Dem": 540 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 10 },
                    12:	{"des":"SSZ","Dem": 53 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 10 },
                    11:  {"des": None}
                   },
        "SSZ":{0:	{"des":"BAU","Dem": 32 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 7 },
                    1:	{"des":"BHZ","Dem": 8 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 7 },
                    2:	{"des":"BSB","Dem": 12 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 6 },
                    3:	{"des":"CPQ","Dem": 49 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 5 },
                    4:	{"des":"CWB","Dem": 34 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 5 },
                    5:	{"des":"FEC","Dem": 3 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 14 },
                    6:	{"des":"FLN","Dem": 6 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 8 },
                    7:	{"des":"FOR","Dem": 32 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 10 },
                    8:	{"des":"NAT","Dem": 0 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 10 },
                    9:	{"des":"SPC","Dem": 5 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 15 },
                    10:	{"des":"POA","Dem": 380 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 8 },
                    11:	{"des":"SJP","Dem": 55 ,"H_Col": 10 ,"H_Ent": 18 ,"Prazo": 6 },
                   12:  {"des": None}
                   }
}

Demanda={"Ori":{"BAU":{"destino":destinos["BAU"]},
                "BHZ":{"destino":destinos["BHZ"]},
                "BSB":{"destino":destinos["BSB"]},
                "CPQ":{"destino":destinos["CPQ"]},
                "CWB":{"destino":destinos["CWB"]},
                "FEC":{"destino":destinos["FEC"]},
                "FLN":{"destino":destinos["FLN"]},
                "FOR":{"destino":destinos["FOR"]},
                "NAT":{"destino":destinos["NAT"]},
                "SPC":{"destino":destinos["SPC"]},
                "POA":{"destino":destinos["POA"]},
                "SJP":{"destino":destinos["SJP"]},
                "SSZ":{"destino":destinos["SSZ"]}
                },
                
         }


# dados de custo

Costos={"Ori":{"BAU":{"destino":{	1	:{"des":{	"BHZ"	:{	0	:{"Tipo_V":	"CAR"	,"C_Car":	 2542.83 	,"C_Vaz":	 2034.26 	,"T_Trans":	20	},
                					                            2	:{"Tipo_V":	"TRU"	,"C_Car":	 1779.98 	,"C_Vaz":	 1423.98 	,"T_Trans":	14	}
                                                            }
                                                }
                                        },
                                    3	:{"des":{	"CPQ"	:{	0	:{"Tipo_V":	"CAR"	,"C_Car":	 893.42 	,"C_Vaz":	 714.74 	,"T_Trans":	5	},
                                                                2	:{"Tipo_V":	"TRU"	,"C_Car":	 625.39 	,"C_Vaz":	 500.32 	,"T_Trans":	4	} 
                                                            }
                                                }
                                        },
                                    11	:{"des":{	"SJP"	:{	0	:{"Tipo_V":	"CAR"	,"C_Car":	 770.44 	,"C_Vaz":	 616.35 	,"T_Trans":	4	},
                                                                2	:{"Tipo_V":	"TRU"	,"C_Car":	 539.31 	,"C_Vaz":	 431.45 	,"T_Trans":	3	} 
                                                            }
                                                }
                                        },
                                    10:  {"des": None},
                                    0:  {"des": None},
                                    2:  {"des": None},
                                    4:  {"des": None},
                                    5:  {"des": None},
                                    6:  {"des": None},
                                    7:  {"des": None},
                                    8:  {"des": None},
                                    9:  {"des": None},
                                    12:  {"des": None}
                                 
                                },
                        },

                "BHZ":{"destino":{	2	:{"des":{	"BSB"	:{	0	:{"Tipo_V":	"CAR"	,"C_Car":	 2376.88 	,"C_Vaz":	 2001.92 	,"T_Trans":	21	},
                                                                2	:{"Tipo_V":	"TRU"	,"C_Car":	 1663.82 	,"C_Vaz":	 1401.34 	,"T_Trans":	15	} 
                                                            }
                                                }
                                        },
                                    3	:{"des":{	"CPQ"	:{	1	:{"Tipo_V":	"BIT"	,"C_Car":	 3413.23 	,"C_Vaz":	 2804.80 	,"T_Trans":	14	},
                                                                0	:{"Tipo_V":	"CAR"	,"C_Car":	 1896.24 	,"C_Vaz":	 1558.22 	,"T_Trans":	12	},
                                                                2	:{"Tipo_V":	"TRU"	,"C_Car":	 1327.37 	,"C_Vaz":	 1090.75 	,"T_Trans":	8	} 
                                                            }
                                                }
                                        },
                                    4	:{"des":{	"CWB"	:{	0	:{"Tipo_V":	"CAR"	,"C_Car":	 2816.22 	,"C_Vaz":	 2252.98 	,"T_Trans":	27	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 1971.35 	,"C_Vaz":	 1577.09 	,"T_Trans":	19	} 
                                                            }
                                                }
                                        },
                                    5	:{"des":{	"FEC"	:{	1	:{"Tipo_V":"BIT"	,"C_Car":	 8137.87 	,"C_Vaz":	 6510.29 	,"T_Trans":	42	},
                                                                0	:{"Tipo_V":	"CAR"	,"C_Car":	 4521.04 	,"C_Vaz":	 3616.83 	,"T_Trans":	35	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 3164.73 	,"C_Vaz":	 2531.78 	,"T_Trans":	25	} 
                                                            }
                                                }
                                        },
                                    6	:{"des":{	"FLN"	:{	0	:{"Tipo_V":	"CAR"	,"C_Car":	 4593.84 	,"C_Vaz":	 3889.35 	,"T_Trans":	34	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 3215.69 	,"C_Vaz":	 2722.55 	,"T_Trans":	24	} 
                                                            }
                                                }
                                        },
                                    7	:{"des":{	"FOR"	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 8330.29 	,"C_Vaz":	 7039.64 	,"T_Trans":	82	},
                                                                2	:{"Tipo_V":	"TRU"	,"C_Car":	 5831.20 	,"C_Vaz":	 4927.75 	,"T_Trans":	57	} 
                                                            }
                                                }
                                        },
                                    8	:{"des":{	"NAT"	:{	0	:{"Tipo_V":	"CAR"	,"C_Car":	 8066.80 	,"C_Vaz":	 6453.44 	,"T_Trans":	82	},
                                                                2	:{"Tipo_V":	"TRU"	,"C_Car":	 5646.76 	,"C_Vaz":	 4517.41 	,"T_Trans":	57	} 
                                                            }
                                                }
                                        },
                                    10	:{"des":{	"POA"	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 5824.24 	,"C_Vaz":	 4659.39 	,"T_Trans":	51	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 4076.97 	,"C_Vaz":	 3261.57 	,"T_Trans":	36	} 
                                                            }
                                                }
                                        },
                                    11	:{"des":{	"SJP"	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 2445.16 	,"C_Vaz":	 1956.13 	,"T_Trans":	20	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 1711.61 	,"C_Vaz":	 1369.29 	,"T_Trans":	14	} 
                                                            }
                                                }
                                        },
                                    9	:{"des":{	"SPC"	:{	1	:{"Tipo_V":	'BIT'	,"C_Car":	 2827.44 	,"C_Vaz":	 2544.70 	,"T_Trans":	13	},
                                                                0	:{"Tipo_V":	'CAR'	,"C_Car":	 1570.80 	,"C_Vaz":	 1413.72 	,"T_Trans":	11	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 1099.56 	,"C_Vaz":	 989.60 	,"T_Trans":	8	} 
                                                            }
                                                }
                                        },
                                    0:  {"des": None},
                                    1:  {"des": None},
                                    12:  {"des": None}
                                },
                        },

                'BSB':{"destino":{	1	:{"des":{	'BHZ'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 2442.53 	,"C_Vaz":	 1954.02 	,"T_Trans":	21	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 1709.77 	,"C_Vaz":	 1367.81 	,"T_Trans":	15	} 
                                                            }
                                                }
                                        },
                                    3	:{"des":{	'CPQ'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 2785.65 	,"C_Vaz":	 2313.70 	,"T_Trans":	10	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 1949.96 	,"C_Vaz":	 1619.59 	,"T_Trans":	7	} 
                                                            }
                                                }
                                        },
                                    4	:{"des":{	'CWB'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 4650.11 	,"C_Vaz":	 3720.09 	,"T_Trans":	45	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 3255.08 	,"C_Vaz":	 2604.06 	,"T_Trans":	32	} 
                                                            }
                                                }
                                        },
                                    5	:{"des":{	'FEC'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 4625.32 	,"C_Vaz":	 3899.25 	,"T_Trans":	36	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 3237.72 	,"C_Vaz":	 2729.48 	,"T_Trans":	25	} 
                                                            }
                                                }
                                        },
                                    6	:{"des":{	'FLN'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 5727.81 	,"C_Vaz":	 4582.25 	,"T_Trans":	51	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 4009.47 	,"C_Vaz":	 3207.58 	,"T_Trans":	36	} 
                                                            }
                                                }
                                        },
                                    7	:{"des":{	'FOR'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 7266.81 	,"C_Vaz":	 513.45 	,"T_Trans":	77	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 5086.77 	,"C_Vaz":	 4069.42 	,"T_Trans":	54	} 
                                                            }
                                                }
                                        },
                                    8	:{"des":{	'NAT'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 8061.14 	,"C_Vaz":	 6788.60 	,"T_Trans":	83	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 5642.80 	,"C_Vaz":	 4752.02 	,"T_Trans":	58	} 
                                                            }
                                                }
                                        },
                                    10	:{"des":{	'POA'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 6923.40 	,"C_Vaz":	 5538.72 	,"T_Trans":	76	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 4846.38 	,"C_Vaz":	 3877.10 	,"T_Trans":	53	} 
                                                            }
                                                }
                                        },
                                    11	:{"des":{	'SJP'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 2410.07 	,"C_Vaz":	 1995.66 	,"T_Trans":	21	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 1687.05 	,"C_Vaz":	 1396.96 	,"T_Trans":	15	} 
                                                            }
                                                }
                                        },
                                    0	:{"des":{	'BAU'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 2926.64 	,"C_Vaz":	 2522.33 	,"T_Trans":	25	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 2048.65 	,"C_Vaz":	 1765.63 	,"T_Trans":	18	} 
                                                            }
                                                }
                                        },
                                    9	:{"des":{	'SPC'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 3552.03 	,"C_Vaz":	 2841.63 	,"T_Trans":	27	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 2486.42 	,"C_Vaz":	 1989.14 	,"T_Trans":	19	} 
                                                            }
                                                }
                                        },
                                    12:  {"des": None},
                                    2:  {"des": None}
                                },
                        },

                'CPQ':{"destino":{	1	:{"des":{	'BHZ'	:{	1	:{"Tipo_V":	'BIT'	,"C_Car":	 3397.12 	,"C_Vaz":	 2717.69 	,"T_Trans":	14	},
                                                                0	:{"Tipo_V":	'CAR'	,"C_Car":	 1887.29 	,"C_Vaz":	 1509.83 	,"T_Trans":	12	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 1321.10 	,"C_Vaz":	 1056.88 	,"T_Trans":	8	} 
                                                            }
                                                }
                                        },
                                    2	:{"des":{	'BSB'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 2888.14 	,"C_Vaz":	 2310.51 	,"T_Trans":	18	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 2021.70 	,"C_Vaz":	 1617.36 	,"T_Trans":	13	} 
                                                            }
                                                }
                                        },
                                    4	:{"des":{	'CWB'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 1875.47 	,"C_Vaz":	 1500.37 	,"T_Trans":	10	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 1312.83 	,"C_Vaz":	 1050.26 	,"T_Trans":	7	} 
                                                            }
                                                }
                                         },
                                   5	:{"des":{	'FEC'	:{	1	:{"Tipo_V":	'BIT'	,"C_Car":	 13325.56 	,"C_Vaz":	 10660.45 	,"T_Trans":	77	},
                                                                0	:{"Tipo_V":	'CAR'	,"C_Car":	 7403.09 	,"C_Vaz":	 5922.47 	,"T_Trans":	64	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 5182.16 	,"C_Vaz":	 4145.73 	,"T_Trans":	45	} 
                                                            }
                                                }
                                         },
                                   6	:{"des":{	'FLN'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 2839.43 	,"C_Vaz":	 2271.54 	,"T_Trans":	22	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 1987.60 	,"C_Vaz":	 1590.08 	,"T_Trans":	15	} 
                                                             }
                                                }
                                        },
                                    7	:{"des":{	'FOR'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 11593.43 	,"C_Vaz":	 9274.74 	,"T_Trans":	111	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 8115.40 	,"C_Vaz":	 6492.32 	,"T_Trans":	78	} 
                                                            }
                                                }
                                        },
                                    8	:{"des":{	'NAT'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 11504.27 	,"C_Vaz":	 9203.41 	,"T_Trans":	102	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 8052.99 	,"C_Vaz":	 6442.39 	,"T_Trans":	71	} 
                                                            }
                                                }
                                        },
                                    10	:{"des":{	'POA'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 4631.95 	,"C_Vaz":	 3705.56 	,"T_Trans":	33	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 3242.37 	,"C_Vaz":	 2593.89 	,"T_Trans":	23	} 
                                                            }
                                                }
                                        },
                                    11	:{"des":{	'SJP'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 1193.64 	,"C_Vaz":	 954.91 	,"T_Trans":	7	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 835.55 	,"C_Vaz":	 668.44 	,"T_Trans":	5	} 
                                                            }
                                                }
                                        },
                                    12	:{"des":{	'SSZ'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 650.30 	,"C_Vaz":	 520.23 	,"T_Trans":	3	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 455.21 	,"C_Vaz":	 364.16 	,"T_Trans":	2	} 
                                                            }
                                                }
                                        },
                                    0	:{"des":{	'BAU'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 904.28 	,"C_Vaz":	 723.43 	,"T_Trans":	5	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 633.00 	,"C_Vaz":	 506.40 	,"T_Trans":	4	} 
                                                             }
                                                }
                                        },
                                   9	:{"des":{	'SPC'	:{	1	:{"Tipo_V":	'BIT'	,"C_Car":	 740.16 	,"C_Vaz":	 604.80 	,"T_Trans":	2	},
                                                                0	:{"Tipo_V":	'CAR'	,"C_Car":	 411.20 	,"C_Vaz":	 336.00 	,"T_Trans":	2	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 287.84 	,"C_Vaz":	 235.20 	,"T_Trans":	1	} 
                                                            }
                                                }
                                        },
                                    3:  {"des": None}
                                },
                        },

                'CWB':{"destino":{	1	:{"des":{	'BHZ'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 3247.41 	,"C_Vaz":	 2597.93 	,"T_Trans":	27	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 2273.19 	,"C_Vaz":	 1818.55 	,"T_Trans":	19	} 
                                                            }
                                                }
                                        },
                                    2	:{"des":{	'BSB'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 4770.41 	,"C_Vaz":	 4019.18 	,"T_Trans":	46	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 3339.29 	,"C_Vaz":	 2813.43 	,"T_Trans":	32	} 
                                                            }
                                                }
                                        },
                                    3	:{"des":{	'CPQ'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 1867.63 	,"C_Vaz":	 1494.10 	,"T_Trans":	10	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 1307.34 	,"C_Vaz":	 1045.87 	,"T_Trans":	7	} 
                                                            }
                                                }
                                        },

                                    5	:{"des":{	'FEC'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 6746.42 	,"C_Vaz":	 5397.14 	,"T_Trans":	80	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 4722.49 	,"C_Vaz":	 3778.00 	,"T_Trans":	56	} 
                                                            }
                                                }
                                        },
                                    6	:{"des":{	'FLN'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 1081.51 	,"C_Vaz":	 865.22 	,"T_Trans":	6	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 757.06 	,"C_Vaz":	 605.65 	,"T_Trans":	4	} 
                                                            }
                                                }
                                        },
                                    7	:{"des":{	'FOR'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 12076.08 	,"C_Vaz":	 9660.87 	,"T_Trans":	123	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 8453.26 	,"C_Vaz":	 6762.61 	,"T_Trans":	86	} 
                                                            }
                                                }
                                        },
                                    8	:{"des":{	'NAT'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 11491.25 	,"C_Vaz":	 9193.00 	,"T_Trans":	119	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 8043.88 	,"C_Vaz":	 6435.10 	,"T_Trans":	83	} 
                                                            }
                                                }
                                        },
                                    10	:{"des":{	'POA'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 2326.46 	,"C_Vaz":	 1960.89 	,"T_Trans":	21	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 1628.52 	,"C_Vaz":	 1372.62 	,"T_Trans":	15	} 
                                                            }
                                                }
                                        },
                                    11	:{"des":{	'SJP'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 3063.69 	,"C_Vaz":	 2450.95 	,"T_Trans":	23	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 2144.58 	,"C_Vaz":	 1715.67 	,"T_Trans":	16	} 
                                                            }
                                                }
                                        },
                                    12	:{"des":{	'SSZ'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 1569.82 	,"C_Vaz":	 1255.86 	,"T_Trans":	9	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 1098.87 	,"C_Vaz":	 879.10 	,"T_Trans":	6	} 
                                                            }
                                                }
                                        },
                                    0	:{"des":{	'BAU'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 2050.90 	,"C_Vaz":	 1640.72 	,"T_Trans":	11	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 1435.63 	,"C_Vaz":	 1148.50 	,"T_Trans":	8	} 
                                                            }
                                                }
                                        },
                                    9	:{"des":{	'SPC'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 1503.00 	,"C_Vaz":	 1202.40 	,"T_Trans":	9	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 1052.10 	,"C_Vaz":	 841.68 	,"T_Trans":	6	} 
                                                            }
                                                }
                                        },
                                    4:  {"des": None}                                  
                                },
                        },

                'FEC':{"destino":{	1	:{"des":{	'BHZ'	:{	1	:{"Tipo_V":	'BIT'	,"C_Car":	 8148.15 	,"C_Vaz":	 6518.50 	,"T_Trans":	42	},
                                                                0	:{"Tipo_V":	'CAR'	,"C_Car":	 4526.75 	,"C_Vaz":	 3621.39 	,"T_Trans":	35	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 3168.73 	,"C_Vaz":	 2534.97 	,"T_Trans":	25	} 
                                                            }
                                                }
                                        },
                                    2	:{"des":{	'BSB'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 4788.45 	,"C_Vaz":	 3830.76 	,"T_Trans":	37	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 3351.92 	,"C_Vaz":	 2681.53 	,"T_Trans":	26	} 
                                                            }
                                                }
                                        },
                                    3	:{"des":{	'CPQ'	:{	1	:{"Tipo_V":	'BIT'	,"C_Car":	 13275.38 	,"C_Vaz":	 10620.31 	,"T_Trans":	77	},
                                                                0	:{"Tipo_V":	'CAR'	,"C_Car":	 7375.21 	,"C_Vaz":	 5900.17 	,"T_Trans":	64	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 5162.65 	,"C_Vaz":	 4130.12 	,"T_Trans":	45	} 
                                                            }
                                                }
                                        },
                                    4	:{"des":{	'CWB'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 7969.82 	,"C_Vaz":	 6375.86 	,"T_Trans":	81	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 5578.87 	,"C_Vaz":	 4463.10 	,"T_Trans":	57	} 
                                                            }
                                                }
                                        },
                                    6	:{"des":{	'FLN'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 8839.49 	,"C_Vaz":	 7071.59 	,"T_Trans":	94	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 6187.64 	,"C_Vaz":	 4950.11 	,"T_Trans":	66	} 
                                                            }
                                                }
                                        },
                                    7	:{"des":{	'FOR'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 3688.84 	,"C_Vaz":	 2951.07 	,"T_Trans":	29	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 2582.19 	,"C_Vaz":	 2065.75 	,"T_Trans":	20	} 
                                                            }
                                                }
                                        },
                                    8	:{"des":{	'NAT'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 3530.95 	,"C_Vaz":	 2824.76 	,"T_Trans":	28	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 2471.67 	,"C_Vaz":	 1977.33 	,"T_Trans":	20	} 
                                                            }
                                                }
                                        },
                                    10	:{"des":{	'POA'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 10242.73 	,"C_Vaz":	 8194.19 	,"T_Trans":	112	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 7169.91 	,"C_Vaz":	 5735.93 	,"T_Trans":	78	} 
                                                            }
                                                }
                                        },
                                    11	:{"des":{	'SJP'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 5502.42 	,"C_Vaz":	 4586.67 	,"T_Trans":	60	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 3851.69 	,"C_Vaz":	 3210.67 	,"T_Trans":	42	} 
                                                            }
                                                }
                                        },
                                    0	:{"des":{	'BAU'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 7314.33 	,"C_Vaz":	 5851.46 	,"T_Trans":	60	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 5120.03 	,"C_Vaz":	 4096.02 	,"T_Trans":	42	} 
                                                            }
                                                }
                                        },
                                    9	:{"des":{	'SPC'	:{	2	:{"Tipo_V":	'TRU'	,"C_Car":	 4450.18 	,"C_Vaz":	 3655.52 	,"T_Trans":	44	},
                                                                1	:{"Tipo_V":	'BIT'	,"C_Car":	 11443.32 	,"C_Vaz":	 9399.91 	,"T_Trans":	76	},
                                                                0	:{"Tipo_V":	'CAR'	,"C_Car":	 6357.40 	,"C_Vaz":	 5222.17 	,"T_Trans":	63	} 
                                                            }
                                                }
                                        },
                                    5:  {"des": None},
                                    12:  {"des": None}
                                    
                                },
                        },
               'FLN':{"destino":{	1	:{"des":{	'BHZ'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 4597.64 	,"C_Vaz":	 3892.39 	,"T_Trans":	34	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 3218.35 	,"C_Vaz":	 2724.67 	,"T_Trans":	24	} 
                                                            }
                                                }
                                        },
                                    2	:{"des":{	'BSB'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 5886.90 	,"C_Vaz":	 4709.52 	,"T_Trans":	51	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 4120.83 	,"C_Vaz":	 3296.66 	,"T_Trans":	36	} 
                                                            }
                                                }
                                        },
                                    3	:{"des":{	'CPQ'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 2839.43 	,"C_Vaz":	 2271.54 	,"T_Trans":	22	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 1987.60 	,"C_Vaz":	 1590.08 	,"T_Trans":	15	} 
                                                            }
                                                }
                                        },
                                    4	:{"des":{	'CWB'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 1023.44 	,"C_Vaz":	 818.75 	,"T_Trans":	6	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 716.41 	,"C_Vaz":	 573.13 	,"T_Trans":	4	} 
                                                            }
                                                }
                                        },
                                    5	:{"des":{	'FEC'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 8828.07 	,"C_Vaz":	 7446.92 	,"T_Trans":	94	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 6179.65 	,"C_Vaz":	 5212.84 	,"T_Trans":	66	} 
                                                            }
                                                }
                                        },
                                    7	:{"des":{	'FOR'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 12955.33 	,"C_Vaz":	 10364.27 	,"T_Trans":	136	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 9068.73 	,"C_Vaz":	 7254.99 	,"T_Trans":	95	} 
                                                            }
                                                }
                                        },
                                    8	:{"des":{	'NAT'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 12441.78 	,"C_Vaz":	 9953.42 	,"T_Trans":	133	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 8709.25 	,"C_Vaz":	 6967.39 	,"T_Trans":	93	} 
                                                            }
                                                }
                                        },
                                    10	:{"des":{	'POA'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 1580.68 	,"C_Vaz":	 1264.54 	,"T_Trans":	9	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 1106.48 	,"C_Vaz":	 885.18 	,"T_Trans":	6	} 
                                                            }
                                                }
                                        },
                                    9	:{"des":{	'SPC'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 2432.07 	,"C_Vaz":	 2012.23 	,"T_Trans":	21	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 1702.45 	,"C_Vaz":	 1408.56 	,"T_Trans":	15	} 
                                                            }
                                                }
                                        },
                                    6:  {"des": None},
                                    11:  {"des": None},
                                    12:  {"des": None},
                                    0:  {"des": None}
                                },
                        },
              'FOR':{"destino":{	1	:{"des":{	'BHZ'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 8369.89 	,"C_Vaz":	 6502.94 	,"T_Trans":	81	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 5858.92 	,"C_Vaz":	 4552.06 	,"T_Trans":	57	} 
                                                            }
                                                }
                                        },
                                    2	:{"des":{	'BSB'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 7475.39 	,"C_Vaz":	 5980.31 	,"T_Trans":	78	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 5232.77 	,"C_Vaz":	 4186.22 	,"T_Trans":	55	} 
                                                            }
                                                }
                                        },
                                    3	:{"des":{	'CPQ'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 10427.02 	,"C_Vaz":	 8100.30 	,"T_Trans":	113	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 7298.91 	,"C_Vaz":	 5670.21 	,"T_Trans":	79	} 
                                                            }
                                                }
                                        },
                                    4	:{"des":{	'CWB'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 11898.12 	,"C_Vaz":	 9518.49 	,"T_Trans":	132	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 8328.68 	,"C_Vaz":	 6662.94 	,"T_Trans":	92	} 
                                                            }
                                                }
                                        },
                                    5	:{"des":{	'FEC'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 3578.56 	,"C_Vaz":	 2862.85 	,"T_Trans":	28	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 2504.99 	,"C_Vaz":	 2004.00 	,"T_Trans":	20	} 
                                                            }
                                                }
                                        },
                                    6	:{"des":{	'FLN'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 12753.68 	,"C_Vaz":	 10202.95 	,"T_Trans":	138	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 8927.58 	,"C_Vaz":	 7142.07 	,"T_Trans":	97	} 
                                                            }
                                                }
                                        },
                                    8	:{"des":{	'NAT'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 1726.69 	,"C_Vaz":	 1381.35 	,"T_Trans":	10	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 1208.68 	,"C_Vaz":	 966.95 	,"T_Trans":	7	} 
                                                            }
                                                }
                                        },
                                    10	:{"des":{	'POA'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 14228.45 	,"C_Vaz":	 11977.70 	,"T_Trans":	155	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 9959.92 	,"C_Vaz":	 8384.39 	,"T_Trans":	109	} 
                                                            }
                                                }
                                        },
                                    11	:{"des":{	'SJP'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 11169.17 	,"C_Vaz":	 8935.33 	,"T_Trans":	101	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 7818.42 	,"C_Vaz":	 6254.73 	,"T_Trans":	71	} 
                                                            }
                                                }
                                        },
                                    12	:{"des":{	'SSZ'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 11587.49 	,"C_Vaz":	 9270.00 	,"T_Trans":	111	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 8111.24 	,"C_Vaz":	 6489.00 	,"T_Trans":	78	} 
                                                            }
                                                }
                                        },
                                    0	:{"des":{	'BAU'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 11910.73 	,"C_Vaz":	 9528.60 	,"T_Trans":	113	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 8337.51 	,"C_Vaz":	 6670.02 	,"T_Trans":	79	} 
                                                            }
                                                }
                                        },
                                    9	:{"des":{	'SPC'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 9870.25 	,"C_Vaz":	 7800.83 	,"T_Trans":	93	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 6909.18 	,"C_Vaz":	 5460.58 	,"T_Trans":	65	} 
                                                            }
                                                }
                                        },
                                    7:  {"des": None}
                                },
                        },
                'NAT':{"destino":{	1	:{"des":{	'BHZ'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 8137.59 	,"C_Vaz":	 6316.29 	,"T_Trans":	82	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 5696.31 	,"C_Vaz":	 4421.40 	,"T_Trans":	57	} 
                                                            }
                                                }
                                        },
                                    2	:{"des":{	'BSB'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 8184.15 	,"C_Vaz":	 6547.32 	,"T_Trans":	83	},
                                                                2  	:{"Tipo_V":	'TRU'	,"C_Car":	 5728.91 	,"C_Vaz":	 4583.12 	,"T_Trans":	58	} 
                                                            }
                                                }
                                        },
                                    3	:{"des":{	'CPQ'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 12360.07 	,"C_Vaz":	 9393.66 	,"T_Trans":	102	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 8652.05 	,"C_Vaz":	 6575.56 	,"T_Trans":	71	} 
                                                            }
                                                }
                                        },
                                    4	:{"des":{	'CWB'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 11219.35 	,"C_Vaz":	 8975.48 	,"T_Trans":	119	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 7853.55 	,"C_Vaz":	 6282.84 	,"T_Trans":	83	} 
                                                            }
                                                }
                                        },
                                    5	:{"des":{	'FEC'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 3527.63 	,"C_Vaz":	 2972.17 	,"T_Trans":	28	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 2469.34 	,"C_Vaz":	 2080.52 	,"T_Trans":	20	} 
                                                            }
                                                }
                                        },
                                    6	:{"des":{	'FLN'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 12140.32 	,"C_Vaz":	 1022473 	,"T_Trans":	133	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 8498.22 	,"C_Vaz":	 7157.31 	,"T_Trans":	93	} 
                                                            }
                                                }
                                        },
                                    7	:{"des":{	'FOR'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 1738.10 	,"C_Vaz":	 1465.79 	,"T_Trans":	10	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 1216.67 	,"C_Vaz":	 1026.05 	,"T_Trans":	7	} 
                                                            }
                                                }
                                        },
                                    10	:{"des":{	'POA'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 13549.67 	,"C_Vaz":	 10839.74 	,"T_Trans":	142	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 9484.77 	,"C_Vaz":	 7587.82 	,"T_Trans":	99	} 
                                                            }
                                                }
                                        },
                                    11	:{"des":{	'SJP'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 8271.01 	,"C_Vaz":	 7168.37 	,"T_Trans":	100	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 5789.71 	,"C_Vaz":	 5017.86 	,"T_Trans":	70	} 
                                                            }
                                                }
                                        },
                                    9	:{"des":{	'SPC'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 9949.99 	,"C_Vaz":	 7840.38 	,"T_Trans":	102	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 6964.99 	,"C_Vaz":	 5488.27 	,"T_Trans":	71	} 
                                                             }
                                                }
                                        },
                                    8:  {"des": None},
                                    0:  {"des": None},
                                    12:  {"des": None}
                                },
                        },
                'POA':{"destino":{	2	:{"des":{	'BSB'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 7105.84 	,"C_Vaz":	 5684.67 	,"T_Trans":	76	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 4974.09 	,"C_Vaz":	 3979.27 	,"T_Trans":	53	} 
                                                            }
                                                }
                                        },
                                    3	:{"des":{	'CPQ'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 4641.46 	,"C_Vaz":	 3713.17 	,"T_Trans":	33	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 3249.02 	,"C_Vaz":	 2599.22 	,"T_Trans":	23	} 
                                                            }
                                                }
                                        },
                                    4	:{"des":{	'CWB'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 2339.12 	,"C_Vaz":	 1971.02 	,"T_Trans":	21	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 1637.38 	,"C_Vaz":	 1379.71 	,"T_Trans":	15	} 
                                                            }
                                                }
                                        },
                                    5	:{"des":{	'FEC'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 9038.83 	,"C_Vaz":	 7231.07 	,"T_Trans":	112	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 6327.18 	,"C_Vaz":	 5061.75 	,"T_Trans":	78	} 
                                                            }
                                                }
                                        },
                                    6	:{"des":{	'FLN'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 1409.88 	,"C_Vaz":	 1188.76 	,"T_Trans":	9	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 986.92 	,"C_Vaz":	 832.13 	,"T_Trans":	6	} 
                                                            }
                                                }
                                        },
                                    7	:{"des":{	'FOR'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 12612.74 	,"C_Vaz":	 10090.19 	,"T_Trans":	153	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 8828.92 	,"C_Vaz":	 7063.13 	,"T_Trans":	107	} 
                                                            }
                                                }
                                        },
                                    8	:{"des":{	'NAT'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 13887.02 	,"C_Vaz":	 11109.62 	,"T_Trans":	142	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 9720.91 	,"C_Vaz":	 7776.73 	,"T_Trans":	99	} 
                                                            }
                                                }
                                        },
                                    9	:{"des":{	'SPC'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 3908.08 	,"C_Vaz":	 3235.02 	,"T_Trans":	32	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 2735.66 	,"C_Vaz":	 2264.51 	,"T_Trans":	22	} 
                                                             }
                                                }
                                        },
                                    0:  {"des": None},
                                    12:  {"des": None},
                                    10:  {"des": None},
                                    11:  {"des": None},
                                    1:  {"des": None}
                                },
                        },
                'SJP':{"destino":{	1	:{"des":{	'BHZ'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 2559.36 	,"C_Vaz":	 2047.50 	,"T_Trans":	20	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 1791.55 	,"C_Vaz":	 1433.25 	,"T_Trans":	14	} 
                                                            }
                                                }
                                        },
                                    2	:{"des":{	'BSB'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 2686.05 	,"C_Vaz":	 2148.84 	,"T_Trans":	21	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 1880.24 	,"C_Vaz":	 1504.19 	,"T_Trans":	15	} 
                                                            }
                                                }
                                        },
                                    3	:{"des":{	'CPQ'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 1197.26 	,"C_Vaz":	 957.81 	,"T_Trans":	7	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 838.08 	,"C_Vaz":	 670.47 	,"T_Trans":	5	} 
                                                            }
                                                }
                                        },
                                    4	:{"des":{	'CWB'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 2593.46 	,"C_Vaz":	 2074.77 	,"T_Trans":	20	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 1815.42 	,"C_Vaz":	 1452.34 	,"T_Trans":	14	} 
                                                            }
                                                }
                                        },
                                    5	:{"des":{	'FEC'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 6902.29 	,"C_Vaz":	 5521.84 	,"T_Trans":	61	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 4831.60 	,"C_Vaz":	 3865.29 	,"T_Trans":	43	} 
                                                            }
                                                }
                                        },
                                    0	:{"des":{	'BAU'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 770.44 	,"C_Vaz":	 616.35 	,"T_Trans":	4	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 539.31 	,"C_Vaz":	 431.45 	,"T_Trans":	3	} 
                                                            }
                                                }
                                        },
                                  11:  {"des": None},
                                    12:  {"des": None},
                                    6:  {"des": None},
                                    7:  {"des": None},
                                    8:  {"des": None},
                                    9:  {"des": None},
                                    10:  {"des": None}
                                },
                        },
                'SPC':{"destino":{	1	:{"des":{	'BHZ'	:{	1	:{"Tipo_V":	'BIT'	,"C_Car":	 3460.34 	,"C_Vaz":	 2866.90 	,"T_Trans":	13	},
                                                                0	:{"Tipo_V":	'CAR'	,"C_Car":	 1922.41 	,"C_Vaz":	 592.72 	,"T_Trans":	11	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 1345.69 	,"C_Vaz":	 1114.90 	,"T_Trans":	8	} 
                                                            }
                                                }
                                        },
                                    2	:{"des":{	'BSB'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 3459.29 	,"C_Vaz":	 2862.34 	,"T_Trans":	27	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 2421.50 	,"C_Vaz":	 2003.64 	,"T_Trans":	19	} 
                                                            }
                                                }
                                        },
                                    3	:{"des":{	'CPQ'	:{	1	:{"Tipo_V":	'BIT'	,"C_Car":	 729.20 	,"C_Vaz":	 612.11 	,"T_Trans":	2	},
                                                                0	:{"Tipo_V":	'CAR'	,"C_Car":	 405.11 	,"C_Vaz":	 340.06 	,"T_Trans":	2	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 283.58 	,"C_Vaz":	 238.04 	,"T_Trans":	1	} 
                                                            }
                                                }
                                        },
                                    4	:{"des":{	'CWB'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 1441.46 	,"C_Vaz":	 1215.94 	,"T_Trans":	9	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 1009.02 	,"C_Vaz":	 851.16 	,"T_Trans":	6	} 
                                                            }
                                                }
                                        },
                                    5	:{"des":{	'FEC'	:{	1	:{"Tipo_V":	'BIT'	,"C_Car":	 11965.39 	,"C_Vaz":	 9572.31 	,"T_Trans":	76	},
                                                                0	:{"Tipo_V":	'CAR'	,"C_Car":	 6647.44 	,"C_Vaz":	 5317.95 	,"T_Trans":	63	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 4653.21 	,"C_Vaz":	 3722.57 	,"T_Trans":	44	} 
                                                            }
                                                }
                                        },
                                    6	:{"des":{	'FLN'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 2402.47 	,"C_Vaz":	 1988.36 	,"T_Trans":	21	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 1681.73 	,"C_Vaz":	 1391.85 	,"T_Trans":	15	} 
                                                            }
                                                }
                                        },
                                    7	:{"des":{	'FOR'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 10613.02 	,"C_Vaz":	 8490.42 	,"T_Trans":	102	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 7429.11 	,"C_Vaz":	 5943.29 	,"T_Trans":	71	} 
                                                            }
                                                }
                                        },
                                    8	:{"des":{	'NAT'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 10442.43 	,"C_Vaz":	 8645.70 	,"T_Trans":	102	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 7309.70 	,"C_Vaz":	 6051.99 	,"T_Trans":	71	} 
                                                            }
                                                }
                                        },
                                    10	:{"des":{	'POA'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 3858.30 	,"C_Vaz":	 3193.23 	,"T_Trans":	32	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 2700.81 	,"C_Vaz":	 2235.26 	,"T_Trans":	22	} 
                                                            }
                                                }
                                        },
                                    11	:{"des":{	'SJP'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 1475.82 	,"C_Vaz":	 1220.69 	,"T_Trans":	9	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 1033.07 	,"C_Vaz":	 854.48 	,"T_Trans":	6	} 
                                                            }
                                                }
                                        },
                                    12	:{"des":{	'SSZ'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 289.37 	,"C_Vaz":	 231.50 	,"T_Trans":	1	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 202.56 	,"C_Vaz":	 162.05 	,"T_Trans":	1	} 
                                                            }
                                                }
                                        },
                                    0	:{"des":{	'BAU'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 215.35 	,"C_Vaz":	 972.28 	,"T_Trans":	6	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 850.75 	,"C_Vaz":	 680.60 	,"T_Trans":	4	} 
                                                            }
                                                }
                                        },
                                    9:  {"des": None}
                                },
                        },
                'SSZ':{"destino":{	3	:{"des":{	'CPQ'	:{	0	:{"Tipo_V":	'CAR'	,"C_Car":	 694.03 	,"C_Vaz":	 555.23 	,"T_Trans":	3	},
                                                                2	:{"Tipo_V":	'TRU'	,"C_Car":	 485.82 	,"C_Vaz":	 388.66 	,"T_Trans":	2	} 
                                                            }
                                                }
                                        },
                                  0:  {"des": None},
                                  10:  {"des": None},
                                  11:  {"des": None},
                                    1:  {"des": None},
                                    2:  {"des": None},
                                    4:  {"des": None},
                                    5:  {"des": None},
                                    6:  {"des": None},
                                    7:  {"des": None},
                                    8:  {"des": None},
                                    9:  {"des": None},
                                    12:  {"des": None}
                                },
                        }
            }       
}

## bloque de funciones##
def nivel_dem(dem_A): #extração de nivel de demanda
    k=[]
    dema=dem_A
    p=0
    while type(dema[0])is list: #rota de ida
        p+=1
        dema=dema[0]
    p1=0
    while type(dema[1])is list:#rota de volta
        p1+=1
        dema=dema[0]
    p1
    k=[p,p1]
    return k
def val_rota(i,j,n=0):# validacion existencia rutas ida y/o vuelta
    control=False
    if n==0:# solo valida ida
        if Costos["Ori"][filial[i]["Acro"]]["destino"]!=None:
            if Costos["Ori"][filial[i]["Acro"]]["destino"][j]["des"]!=None:
                control=True
    elif n==1:# solo valida vuelta
        if Costos["Ori"][filial[i]["Acro"]]["destino"]!=None:
            if Costos["Ori"][filial[j]["Acro"]]["destino"][i]["des"]!=None:
                control=True
    elif n==2:# ambas
        if Costos["Ori"][filial[i]["Acro"]]["destino"]!=None:
            if Costos["Ori"][filial[i]["Acro"]]["destino"][j]["des"]!=None:
                if Costos["Ori"][filial[i]["Acro"]]["destino"]!=None:
                    if Costos["Ori"][filial[j]["Acro"]]["destino"][i]["des"]!=None:
                        control=True
    return control

def val_rota_dem(i,j,n=0):# validacion existencia rutas de demanda ida y/o vuelta
    control=False
    if n==0:# solo valida ida
        if Demanda["Ori"][filial[i]["Acro"]]["destino"]!=None:
            if Demanda["Ori"][filial[i]["Acro"]]["destino"][j]["des"]!=None:
                    control=True
    elif n==1:# solo valida vuelta
        if Demanda["Ori"][filial[j]["Acro"]]["destino"]!=None:
            if Demanda["Ori"][filial[j]["Acro"]]["destino"][i]["des"]!=None:
                control=True
    elif n==2:# ambas
        if Demanda["Ori"][filial[i]["Acro"]]["destino"]!=None:
            if Demanda["Ori"][filial[i]["Acro"]]["destino"][j]["des"]!=None:
                if Demanda["Ori"][filial[j]["Acro"]]["destino"]!=None:
                    if Demanda["Ori"][filial[j]["Acro"]]["destino"][i]["des"]!=None:
                        control=True
    return control

def repite_ruta_salida(Rutas):
    respuesta=[]
    for i in list(range(len(Rutas))):
        for j in list(range(len(Rutas))):
            if Rutas[i][1]==Rutas[j][1]:
                auxi=True
            else:
                auxi=False

            respuesta.append(auxi)
    return respuesta

def costo(i,j,k=None,k1="C_Car"):
    control=False #costo ida 
    control1=False#costo volta
    if (k!=None and k1=="C_Car"): # costo de ida para veiculo k, cargado
        control=Costos["Ori"][filial[i]["Acro"]]["destino"][j]["des"][filial[j]["Acro"]][tipo_v[k]["num"]][k1]
    elif(k!=None and k1=="C_Vaz"):# costo de ida para veiculo k, descargado
        control=Costos["Ori"][filial[i]["Acro"]]["destino"][j]["des"][filial[j]["Acro"]][tipo_v[k]["num"]][k1]    
    elif (k==None and (k1=="C_Car"or k1=="C_Vaz")):# costos de ida 
        control=Costos["Ori"][filial[i]["Acro"]]["destino"][j]["des"][filial[j]["Acro"]]

    return control

def Tempo(i,j,k=None,k1="T_Trans",k2=None):
    control=False #costo ida 
    if (k2!=None and k==0 and k1=="T_Trans"): # costo de ida para veiculo k
        control=Costos["Ori"][filial[i]["Acro"]]["destino"][j]["des"][filial[j]["Acro"]][tipo_v[k2]["num"]][k1]
    elif(k2!=None and k==1 and k1=="T_Trans"):# costo de volta para veiculo k
        control=Costos["Ori"][filial[j]["Acro"]]["destino"][i]["des"][filial[i]["Acro"]][tipo_v[k2]["num"]][k1]    
    elif (k2!=None and k==2 and (k1=="T_Trans")):# costos de ida 
        control=Costos["Ori"][filial[i]["Acro"]]["destino"][j]["des"][filial[j]["Acro"]][tipo_v[k2]["num"]][k1]+Costos["Ori"][filial[j]["Acro"]]["destino"][i]["des"][filial[i]["Acro"]][tipo_v[k2]["num"]][k1]
    
    return control

def Demandas(i,j,n=0):# validacion existencia rutas de demanda ida y/o vuelta
    control=0
    if n==0:# solo valida ida
        if Demanda["Ori"][filial[i]["Acro"]]["destino"]!=None:
            if Demanda["Ori"][filial[i]["Acro"]]["destino"][j]["des"]!=None:
                    control=Demanda["Ori"][filial[i]["Acro"]]["destino"][j]["Dem"]
    elif n==1:# solo valida vuelta
        if Demanda["Ori"][filial[j]["Acro"]]["destino"]!=None:
            if Demanda["Ori"][filial[j]["Acro"]]["destino"][i]["des"]!=None:
                control=Demanda["Ori"][filial[j]["Acro"]]["destino"][i]["Dem"]
    elif n==2:# ambas
        if Demanda["Ori"][filial[i]["Acro"]]["destino"]!=None:
            if Demanda["Ori"][filial[i]["Acro"]]["destino"][j]["des"]!=None:
                if Demanda["Ori"][filial[j]["Acro"]]["destino"]!=None:
                    if Demanda["Ori"][filial[j]["Acro"]]["destino"][i]["des"]!=None:
                        control=[Demanda["Ori"][filial[i]["Acro"]]["destino"][j]["Dem"],Demanda["Ori"][filial[j]["Acro"]]["destino"][i]["Dem"]]
    return control

def Prazo(i,j,n=0):# prazo da demanda ida y/o vuelta
    control=False
    if n==0:# solo valida ida
        if Demanda["Ori"][filial[i]["Acro"]]["destino"]!=None:
            if Demanda["Ori"][filial[i]["Acro"]]["destino"][j]["des"]!=None:
                    control=Demanda["Ori"][filial[i]["Acro"]]["destino"][j]["Prazo"]
    elif n==1:# solo valida vuelta
        if Demanda["Ori"][filial[j]["Acro"]]["destino"]!=None:
            if Demanda["Ori"][filial[j]["Acro"]]["destino"][i]["des"]!=None:
                control=Demanda["Ori"][filial[j]["Acro"]]["destino"][i]["Prazo"]
    elif n==2:# ambas
        if Demanda["Ori"][filial[i]["Acro"]]["destino"]!=None:
            if Demanda["Ori"][filial[i]["Acro"]]["destino"][j]["des"]!=None:
                if Demanda["Ori"][filial[j]["Acro"]]["destino"]!=None:
                    if Demanda["Ori"][filial[j]["Acro"]]["destino"][i]["des"]!=None:
                        control=[Demanda["Ori"][filial[i]["Acro"]]["destino"][j]["Prazo"],Demanda["Ori"][filial[j]["Acro"]]["destino"][i]["Prazo"]]
    return control

# criar rotas direitas
rota= [] # vetor de rotas
t_rota=[]# vetor de tipo de veiculo usado por rota
COSTO_R=[]# vetor de costo por rota
tempo=[]# vetor de tempo por rota
t_custo=[]# vetor de tipo de costo por rota
dem=[]# vetor de demandas por rota
for i in list(range(len(filial))):
    for j in list(range(len(filial))):
        if i!=j:# remover rotas sem movimiento
            if val_rota(i,j,2): # validação existencia rotas ida e vuelta
                if i>j:# rotas unicas
                    
                    costo_r=mat.inf
                    
                    for k in list(tipo_v.keys()):
                        if tipo_v[k]["num"]in Costos["Ori"][filial[i]["Acro"]]["destino"][j]["des"][filial[j]["Acro"]]:# validacion existencia rutas ida para el tipo de veiculo 
                           # demanda menor á capacidade del veiculo 
                            if not val_rota_dem(i,j,n=0):# se não há demanda de ida
                                if not (val_rota_dem(j,i,n=0)):# se não há demanda de volta
                                    
                                    c11=costo(i,j,k,k1="C_Vaz")
                                    c21=costo(j,i,k,k1="C_Vaz")  
                                    C1=c11+c21
                                    costo_r=min(C1,costo_r)
                                    if min(C1,costo_r)==C1:
                                        tip_rota=k
                                        tip_costo=["C_Vaz","C_Vaz"] 
                                        dem_r=[[0,0,0],[0,0,0]]   
                                elif Demanda["Ori"][filial[j]["Acro"]]["destino"][i]["Dem"]<=tipo_v[k]["cap_V"]:# si hay demanda de volta
                                    
                                    c11=costo(i,j,k,k1="C_Vaz") 
                                    c21=costo(j,i,k,k1="C_Car")
                                    
                                    C1=c11+c21
                                    costo_r=min(C1,costo_r)
                                    if min(C1,costo_r)==C1:
                                        tip_rota=k    
                                        tip_costo=["C_Vaz","C_Car"]
                                        dem_r=[[0,0,0],[Demandas(i,j,1),Demandas(i,j,1),0]]
                            elif Demanda["Ori"][filial[i]["Acro"]]["destino"][j]["Dem"]<=tipo_v[k]["cap_V"]:# si hay demanda de ida
                                if (not val_rota_dem(j,i,n=0) ):# si no hay demanda de volta
                                    
                                    c11=costo(i,j,k,k1="C_Car")
                                    c21=costo(j,i,k,k1="C_Vaz")  
                                    
                                    C1=c11+c21
                                    costo_r=min(C1,costo_r)
                                    if min(C1,costo_r)==C1:
                                        tip_rota=k    
                                        tip_costo=["C_Car","C_Vaz"]
                                        dem_r=[[Demandas(i,j,0),Demandas(i,j,0),0],[0,0,0]]
                                elif Demanda["Ori"][filial[j]["Acro"]]["destino"][i]["Dem"]<=tipo_v[k]["cap_V"]:# si hay demanda de volta
                                    
                                    c11=costo(i,j,k,k1="C_Car")
                                    c21=costo(j,i,k,k1="C_Car")  
                                    
                                    C1=c11+c21
                                    costo_r=min(C1,costo_r)
                                    if min(C1,costo_r)==C1:
                                        tip_rota=k  
                                        tip_costo=["C_Car","C_Car"]
                                        dem_r=[[Demandas(i,j,0),Demandas(i,j,0),0],[Demandas(i,j,1),Demandas(i,j,1),0]]
                    if k=='TRU' and costo_r!=mat.inf:
                        COSTO_R.append(costo_r)
                        t_rota.append(tip_rota)
                        rota.append([i,j])
                        tempo.append(Tempo(i,j,2,"T_Trans",tip_rota)+4*tipo_v[tip_rota]["tim_V"])
                        t_custo.append(tip_costo)
                        dem.append(dem_r)

# criar rotas de demanda não satisfeitas com dois nós
k1=None
dem_r=[]# vetor de demandas por rota
for i in list(range(len(filial))):
    for j in list(range(len(filial))):
        if i!=j:# remove rotas sem movimiento
            if val_rota_dem(i,j):# validação existencia rotas de demanda ida  
               for p in list(range(len(rota))):
                    if(len(rota[p])==2):

                        if rota[p]!=[i,j]:
                            if rota[p]!=[j,i]:
                                    k1=None
                                    for n in list(range(len(filial))):
                                        
                                        if (n!=i ) and (val_rota(i,n)==1):# validação existencia rotas ida 
                                            if (n!=j ) and (val_rota(n,j)==1):# validação existencia rotas ida   
                                                
                                                costo_r=mat.inf
                                                for k in list(tipo_v.keys()):
                                                    if tipo_v[k]["num"]in Costos["Ori"][filial[i]["Acro"]]["destino"][n]["des"][filial[n]["Acro"]]and tipo_v[k]["num"]in Costos["Ori"][filial[n]["Acro"]]["destino"][j]["des"][filial[j]["Acro"]]:
                                                        dem_r=[Demandas(i,n)+Demandas(i,j),Demandas(n,j)+Demandas(i,j)]
                                                    # demanda inferior a capacidade
                                                        if dem_r[0]<=tipo_v[k]["cap_V"] and dem_r[1]<=tipo_v[k]["cap_V"]:# si hay demanda de volta
                                                                c11=costo(i,n,k,k1="C_Car")
                                                                c21=costo(n,j,k,k1="C_Car") 
                                                                C1=c11+c21
                                                                costo_r=min(C1,costo_r)
                                                                if (k1!=i ) and (k1!=j ) and  min(C1,costo_r)==C1:
                                                                    tip_rota=k  
                                                                    tip_costo=["C_Car","C_Car"]
                                                                    k1=n 
                                                                    Dem_r=[[Demandas(i,n)+Demandas(i,j),Demandas(i,n),Demandas(i,j)],[Demandas(n,j)+Demandas(i,j),Demandas(n,j),Demandas(i,j)]]

                            else:
                                break
                        else:
                            break
                    
                                            
               if k1!=None and k1!=j and k1!=i and costo_r!= mat.inf :         
                    rota.append([i,k1,j])
                    COSTO_R.append(costo_r)
                    t_rota.append(tip_rota)
                    tempo.append(Tempo(i,k1,0,"T_Trans",tip_rota)+Tempo(k1,j,0,"T_Trans",tip_rota)+4*tipo_v[tip_rota]["tim_V"])
                    t_custo.append(tip_costo)
                    dem.append(Dem_r)

# estudo de demandas satisfeitas
deman=[]
demand=[]
for i in list(range(len(filial))):
    for j in list(range(len(filial))):
        if i!=j:# elimina rutas sin movimiento
            if val_rota_dem(i,j):# validacion existencia rutas de demanda ida
                deman.append([i,j,Demandas(i,j)])
                k=None
                for p in list(range(len(rota))):
                    if len(rota[p])==2:
                        if(rota[p]==[i,j] or rota[p]==[j,i]):# por ciclo ida y vuelta
                            demand.append('satis')
                            k=1
                            break
                    elif len(rota[p])==3:
                        if([rota[p][0],rota[p][1]]==[i,j] or [rota[p][1],rota[p][2]]==[i,j]or [rota[p][0],rota[p][2]]==[i,j]):# por ida
                            demand.append('satis')
                            k=1
                            break
                    if(p==len(rota)-1 and k==None):
                            demand.append('No satis')
# extraindo demandas não satisfeitas
for i,k in enumerate(demand):
    if k =='No satis':
        print(demand[i])
        print(deman[i])
        N_SAT=[demand[i][0],demand[i][1]]

# rotas de vuelta
# encontrar volta uniendo rotas de 3 nó
Rutas=[]#vetor que tem os indices das rotas a unir
Costo=[]#vetor que tem os costos das rotas unidas
Tipo=[]#vetor que tem os tipos das rotas unidas
tempoA=[]#vetor que tem os tempos das rotas unidas
tip_costo=[]#vetor que tem os tipos de custo das rotas por arco
dem_r=[] #vetor que tem os tipos demandas das rotas por arco
for i in list(range(len(rota))):
    if len(rota[i])==3:# seleccionar rota com 3 nó de ida
        costo1=mat.inf
        for j in list(range(len(rota))):
            j1=j-1
            if i!=j and len(rota[j])==3 and rota[i][0]== rota [j][2] and rota[j][0]== rota [i][2]:# seleccionar rota com 3 nó de volta
                aux=COSTO_R[i]+COSTO_R[j]
                
                if aux==min(aux,costo1) and t_rota[i]==t_rota[j]:# escoger el minimo
                    ruta= [i,j]
                    costo1=aux
                    j1+=1

                    if(j1>j ): # validacion de existencias de mais de um nó de volta
                        Rutas[len(Rutas)-1]=ruta
                        Costo[len(Rutas)-1]=costo1 
                        Tipo[len(Rutas)-1]=t_rota[i]
                        tempoA[len(Rutas)-1]=tempo[i]+tempo[j]
                        tip_costo[len(Rutas)-1]=t_custo[i]+t_custo[j]
                        dem_r[len(Rutas)-1]=[dem[i],dem[j]]
                    else:      
                        Rutas.append(ruta)
                        Costo.append(costo1)
                        Tipo.append(t_rota[i])
                        tempoA.append(tempo[i]+tempo[j])
                        tip_costo.append(t_custo[i]+t_custo[j])
                        dem_r.append([dem[i],dem[j]])
     

# Crear elemento en forma de lista para rotas unidas
aux=[]# auxiliar
ruta_con=[] # auxiliar de rota

for i in list(range(len(Rutas))):
    conju=[]
    if Rutas[i]!=None:
        for k in list(range(len(rota[Rutas[i][0]]))):
            aux=rota[Rutas[i][0]][k]
            conju.append(aux)
            if k==len(rota[Rutas[i][0]])-1:# unir rota de volta
                for k1 in list(range(len(rota[Rutas[i][1]])-1)):
                    aux=rota[Rutas[i][1]][k1+1]
                    conju.append(aux)
        ruta_con.append(conju)   
        
# remoção de rotas: 

for i in list(range(len(Rutas))):#sustitucion de unidas e eliminacion de la volta
    if Rutas[i]!=None:
        rota[Rutas[i][0]]=ruta_con[i]
        COSTO_R[Rutas[i][0]]=Costo[i]
        t_rota[Rutas[i][0]]=Tipo[i]
        tempo[Rutas[i][0]]=tempoA[i]
        t_custo[Rutas[i][0]]=tip_costo[i]
        dem[Rutas[i][0]]=dem_r[i]

        rota[Rutas[i][1]]=mat.inf
        COSTO_R[Rutas[i][1]]=mat.inf
        t_rota[Rutas[i][1]]=mat.inf
        tempo[Rutas[i][1]]=mat.inf
        t_custo[Rutas[i][1]]=mat.inf
        dem[Rutas[i][1]]=mat.inf

while mat.inf in COSTO_R :# eliminacionde rutas sobrantes
    rota.remove(mat.inf)
    t_rota.remove(mat.inf)
    COSTO_R.remove(mat.inf)
    tempo.remove(mat.inf)
    t_custo.remove(mat.inf)
    dem.remove(mat.inf)

# rutas de vuelta
# encontrar ida uniendo rotas direitas 
# caso ida directa( sin paradas) con retorno de 3 nó
Rutas=[]#vector que tem os indices das rotas a unir junto con la ruta
Costo=[]#vector que tem os costos das rotas unidas
Tipo=[]#vector que tem os tipos das rotas unidas
tempoA=[]#vector que tem os tempos das rotas unidas
tipo_costo=[]#vector que tem os tipos de costo por arco das rotas unidas
Dem_r=[]#vector que tem as demandas das rotas unidas
for i in list(range(len(rota))):
    if len(rota[i])==3:
        ruta=None# auxiliar de ruta
        costo1=mat.inf# auxiliar de costo
        tip_rota=None# auxiliar de tipo
        temp=None# auxiliar de tempo
        tip_costo=None      
        dem_r=None        
        if val_rota(rota[i][2],rota[i][0]): # validacion existencia rutas ida 

            for k in ['CAR',"TRU","BIT"]:

                
                if tipo_v[k]["num"]in costo(rota[i][2],rota[i][0]):# validacion existencia rutas ida para el tipo de veiculo 

                    # demanda inferior a capacidad
                    if not([rota[i][2],rota[i][0]] is N_SAT):# si no hay demanda de volta
                        c11=costo(rota[i][2],rota[i][0],k,k1="C_Vaz")
                        C1=c11
                        
                        if k==t_rota[i]:
                            ruta=[i,rota[i][2],rota[i][0]]# indice, rota
                            costo1=min(C1,costo1)
                            
                            if min(C1,costo1)==C1:
                                tip_rota=k 
                                tip_costo=["C_Vaz"]
                                temp=Tempo(rota[i][2],rota[i][0],0,"T_Trans",k)
                                dem_r=[0,0,0]
                    
                    elif[rota[i][2],rota[i][0]] is N_SAT and Demanda["Ori"][filial[rota[i][2]]["Acro"]]["destino"][rota[i][0]]["Dem"]<=tipo_v[k]["cap_V"]:# si hay demanda de ida                                             
                        c11=costo(rota[i][2],rota[i][0],k,k1="C_Car")
                        C1=c11 
                            
                        if k==t_rota[i]:
                            ruta=[i,rota[i][2],rota[i][0]]
                            costo1=min(C1,costo1)
                            if min(C1,costo1)==C1:
                                tip_rota=k 
                                tip_costo=["C_Car"]
                                temp=Tempo(rota[i][2],rota[i][0],0,"T_Trans",k)+2*tipo_v[tip_rota]["tim_V"]
                                dem_r=[Demandas(rota[i][2],rota[i][0]),Demandas(rota[i][2],rota[i][0]),0]
                    
                else:
                    continue 
            if k=="BIT" and costo1!=mat.inf:
                Rutas.append(ruta)
                Costo.append(costo1)
                Tipo.append(tip_rota)
                tempoA.append(temp+2*tipo_v[tip_rota]["tim_V"])
                tipo_costo.append(tip_costo)
                Dem_r.append(dem_r)

# Crear elemento en forma de lista para rotas unidas
aux=[]# auxiliar
ruta_con=[] # auxiliar de rota
for i in list(range(len(Rutas))):
    conju=[]
    if Rutas[i]!=None:
        for k in list(range(len(rota[Rutas[i][0]]))):        
            aux=rota[Rutas[i][0]][k]
            conju.append(aux)
            if k==len(rota[Rutas[i][0]])-1:# unir rota de volta
                for k1 in list(range(len(Rutas[i])-2)):
                    aux=Rutas[i][k1+2]
                    conju.append(aux)


        ruta_con.append(conju)   
        
# eliminacion de rutas: 
for i in list(range(len(Rutas))):#sustitucion de unidas e eliminacion de la volta
        if Rutas[i]!=None:       
            rota[Rutas[i][0]]=ruta_con[i]
            COSTO_R[Rutas[i][0]]=Costo[i]+COSTO_R[Rutas[i][0]]
            t_rota[Rutas[i][0]]=Tipo[i]
            tempo[Rutas[i][0]]=tempoA[i]+tempo[Rutas[i][0]]
            t_custo[Rutas[i][0]]=(tipo_costo[i][0])
            dem[Rutas[i][0]]=[dem[Rutas[i][0]],Dem_r[i]]

# validacion rutas faltantes
k=0
for i in list(range(len(rota))):
    if len(rota[i])==3:
        print(rota[i])
        k+=1
k

# crear rutas de demanda no satisfechas con 3 nodos
#retorno de 3 nós
Rutas=[]#vector que tem as rotas a unir
Costo=[]#vector que tem os costos das rotas unidas
Tipo=[]#vector que tem os tipos das rotas unidas
tempoA=[]#vector que tem os tempos das rotas unidas
tipo_costo=[]#vector que tem os tipos de costo por arco das rotas unidas
Dem_r=[]#vector que tem as demandas das rotas unidas
for i in list(range(len(rota))) :
    if len(rota[i])==3:
        costo_r=mat.inf
        k1=None
        for n in list(range(len(filial))):
            
            if n!=rota[i][0]and n!=rota[i][2]:# elimina rutas sin movimiento       
                for k in list(tipo_v.keys()):
                    if(val_rota(rota[i][2],n)):# validacion existencia rutas ida   
                        if (val_rota(n,rota[i][0])):# validacion existencia rutas ida 
                            
                            if (tipo_v[k]["num"]in costo(rota[i][2],n)) and (tipo_v[k]["num"]in costo(n,rota[i][0])) and k==t_rota[i]:
                                # demanda inferior a capacidad
                                if not([rota[i][2],n] is N_SAT) :# si no hay demanda de ida
                                    if not([n,rota[i][0]] is N_SAT):# si no hay demanda de ida
                                            c11=costo(rota[i][2],n,k,k1="C_Vaz")
                                            c21=costo(n,rota[i][0],k,k1="C_Vaz")   
                                            C1=c11+c21
                                            costo_r=min(C1,costo_r)
                                            if(k1!=n )and min(C1,costo_r)==C1:
                                                tip_rota=k
                                                tip_costo=["C_Vaz","C_Vaz"]
                                                k1=n 
                                                dem_r=[[0,0,0],[0,0,0]]
                                                tempa=Tempo(rota[i][2],k1,0,"T_Trans",tip_rota)+Tempo(k1,rota[i][0],0,"T_Trans",tip_rota)
                                    elif  ([n,rota[i][0]] is N_SAT)and Demanda["Ori"][filial[n]["Acro"]]["destino"][rota[i][0]]["Dem"]<=tipo_v[k]["cap_V"]:# si hay demanda de volta
                                        c11=costo(rota[i][2],n,k,k1="C_Vaz")
                                        c21=costo(n,rota[i][0],k,k1="C_Car")   
                                        C1=c11+c21                                                         
                                        costo_r=min(C1,costo_r)
                                        if (k1!=n ) and min(C1,costo_r)==C1:
                                            tip_rota=k
                                            tip_costo=["C_Vaz","C_Car"]
                                            k1=n
                                            dem_r=[[0,0,0],[Demandas(n,rota[i][0]),Demandas(n,rota[i][0]),0]]
                                            tempa=Tempo(rota[i][2],k1,0,"T_Trans",tip_rota)+Tempo(k1,rota[i][0],0,"T_Trans",tip_rota)+2*tipo_v[tip_rota]["tim_V"]
                                elif ([rota[i][2],n] is N_SAT) and Demanda["Ori"][filial[rota[i][2]]["Acro"]]["destino"][n]["Dem"]<=tipo_v[k]["cap_V"]:# si hay demanda de volta
                                    if not([n,rota[i][0]] is N_SAT):# si no hay demanda de volta
                                        c11=costo(rota[i][2],n,k,k1="C_Car")
                                        c21=costo(n,rota[i][0],k,k1="C_Vaz")   
                                        C1=c11+c21
                                        costo_r=min(C1,costo_r)
                                        if (k1!=n )and min(C1,costo_r)==C1:
                                            tip_rota=k
                                            tip_costo=["C_Car","C_Vaz"]
                                            k1=n
                                            dem_r=[[Demandas(rota[i][2],n),Demandas(rota[i][2],n),0],[0,0,0]]
                                            tempa=Tempo(rota[i][2],k1,0,"T_Trans",tip_rota)+Tempo(k1,rota[i][0],0,"T_Trans",tip_rota)+2*tipo_v[tip_rota]["tim_V"]
                                    elif ([n,rota[i][0]] is N_SAT) and Demanda["Ori"][filial[n]["Acro"]]["destino"][rota[i][0]]["Dem"]<=tipo_v[k]["cap_V"]:# si hay demanda de volta
                                        c11=costo(rota[i][2],n,k,k1="C_Car")
                                        c21=costo(n,rota[i][0],k,k1="C_Car")   
                                        C1=c11+c21                                                          
                                        costo_r=min(C1,costo_r)
                                        if (k1!=n)and min(C1,costo_r)==C1:
                                            tip_rota=k
                                            tip_costo=["C_Car","C_Car"]
                                            k1=n
                                            dem_r=[[Demandas(rota[i][2],n),Demandas(rota[i][2],n),0],[Demandas(n,rota[i][0]),Demandas(n,rota[i][0]),0]]
                                            tempa=Tempo(rota[i][2],k1,0,"T_Trans",tip_rota)+Tempo(k1,rota[i][0],0,"T_Trans",tip_rota)+4*tipo_v[tip_rota]["tim_V"]            
                        else:
                            break                       
                    else:
                        break
            
        if (k1!= None) and (k1!=rota[i][0] and k1!=rota[i][2]):
            Rutas.append([i,rota[i][2],k1,rota[i][0]])
            Costo.append(costo_r)
            Tipo.append(tip_rota)
            tempoA.append(tempa)
            tipo_costo.append(tip_costo)
            Dem_r.append(dem_r)
    else:
        continue
    
# Crear elemento en forma de lista para rotas unidas
aux=[]# auxiliar
ruta_con=[] # auxiliar de rota
for i in list(range(len(Rutas))):
    conju=[]
    for k in list(range(len(rota[Rutas[i][0]]))):
            aux=rota[Rutas[i][0]][k]
            
            conju.append(aux)
            if k==len(rota[Rutas[i][0]])-1:# unir rota de volta  
                for k1 in list(range(len(Rutas[i])-2)):
                    aux=Rutas[i][k1+2]
                    conju.append(aux)
    ruta_con.append(conju) 
 
        
# eliminacion de rutas: 
for i in list(range(len(Rutas))):#sustitucion de unidas e eliminacion de la volta      
            rota[Rutas[i][0]]=ruta_con[i]
            COSTO_R[Rutas[i][0]]=Costo[i]+COSTO_R[Rutas[i][0]]
            t_rota[Rutas[i][0]]=Tipo[i]
            tempo[Rutas[i][0]]=tempoA[i]+tempo[Rutas[i][0]]
            t_custo[Rutas[i][0]]=tipo_costo[i]+t_custo[Rutas[i][0]]
            dem[Rutas[i][0]]=[dem[Rutas[i][0]],Dem_r[i]]

# validacion rutas faltantes
k=0
for i in list(range(len(rota))):
    if len(rota[i])==3:
        print(rota[i])
        k+=1
k


# crear rutas de demanda no satisfechas con 3 nodos
Rutas=[]#vector que tem as rotas a unir
Costo=[]#vector que tem os costos das rotas unidas
Tipo=[]#vector que tem os tipos das rotas unidas
tempoA=[]#vector que tem os tempos das rotas unidas
tipo_costo=[]#vector que tem os tipos de costo por arco das rotas unidas
Dem_r=[]#vector que tem as demandas das rotas unidas
for i in list(range(len(rota))):
    if len(rota[i])==3:

        costo_r=mat.inf
        k1=None
        k2=None
        for n in list(range(len(filial))):
            for j in list(range(len(filial))):
                if n!=j and n!=rota[i][0]and n!=rota[i][2]and j!=rota[i][0]and j!=rota[i][2]:# elimina rutas sin movimiento       

                    for k in list(tipo_v.keys()):
                        if(val_rota(rota[i][2],n)):# validacion existencia rutas ida 
                            if (val_rota(n,j)):# validacion existencia rutas ida   
                                if (val_rota(j,rota[i][0])):# validacion existencia rutas ida                      
                                          
                                    if (tipo_v[k]["num"]in costo(rota[i][2],n))and (tipo_v[k]["num"]in costo(n,j))and( tipo_v[k]["num"]in costo(j,rota[i][0])) and k==t_rota[i]:
                                        # demanda inferior a capacidad
                                        if  not([rota[i][2],n] is N_SAT) :# si no hay demanda de ida
                                            
                                            if  not([n,j] is N_SAT):# si no hay demanda de ida
                                                if  not([j,rota[i][0]] is N_SAT):# si no hay demanda de ida
                                                    c11=costo(rota[i][2],n,k,k1="C_Vaz")
                                                    c21=costo(n,j,k,k1="C_Vaz")
                                                    c31=costo(j,rota[i][0],k,k1="C_Vaz")   
                                                    C1=c11+c21+c31
                                                    costo_r=min(C1,costo_r)
                                                    if(k1!=i ) and (k1!=j )and(k2!=i ) and (k2!=j )  and min(C1,costo_r)==C1:
                                                        tip_rota=k
                                                        tip_costo=["C_Vaz","C_Vaz","C_Vaz"]
                                                        k1=n
                                                        k2=j  
                                                        dem_r=[[0,0,0],[0,0,0],[0,0,0]]
                                                        temp=Tempo(rota[i][2],k1,0,"T_Trans",tip_rota)+Tempo(k1,k2,0,"T_Trans",tip_rota)+Tempo(k2,rota[i][0],0,"T_Trans",tip_rota)
                                                        
                                                elif ([j,rota[i][0]] is N_SAT)and Demanda["Ori"][filial[j]["Acro"]]["destino"][rota[i][0]]["Dem"]<=tipo_v[k]["cap_V"]:# si hay demanda de volta
                                                    c11=costo(rota[i][2],n,k,k1="C_Vaz")
                                                    c21=costo(n,j,k,k1="C_Vaz")
                                                    c31=costo(j,rota[i][0],k,k1="C_Car")   
                                                    C1=c11+c21+c31                                                          
                                                    costo_r=min(C1,costo_r)
                                                    if (k1!=i ) and (k1!=j )and(k2!=i ) and (k2!=j )  and min(C1,costo_r)==C1:
                                                        tip_rota=k
                                                        tip_costo=["C_Vaz","C_Vaz","C_Car"]
                                                        k1=n
                                                        k2=j
                                                        dem_r=[[0,0,0],[0,0,0],[Demandas(j,rota[i][0]),Demandas(j,rota[i][0]),0]]
                                                        temp=Tempo(rota[i][2],k1,0,"T_Trans",tip_rota)+Tempo(k1,k2,0,"T_Trans",tip_rota)+Tempo(k2,rota[i][0],0,"T_Trans",tip_rota)+2*tipo_v[tip_rota]["tim_V"]           
  
                                            elif  ([n,j] is N_SAT)and Demanda["Ori"][filial[n]["Acro"]]["destino"][j]["Dem"]<=tipo_v[k]["cap_V"]:# si hay demanda de ida
                                                if  not([j,rota[i][0]] is N_SAT):# si no hay demanda de volta
                                                    c11=costo(rota[i][2],n,k,k1="C_Vaz")
                                                    c21=costo(n,j,k,k1="C_Car")
                                                    c31=costo(j,rota[i][0],k,k1="C_Vaz")   
                                                    C1=c11+c21+c31
                                                    costo_r=min(C1,costo_r)
                                                    if (k1!=i ) and (k1!=j )and(k2!=i ) and (k2!=j )  and min(C1,costo_r)==C1:
                                                        tip_rota=k
                                                        tip_costo=["C_Vaz","C_Car","C_Vaz"]
                                                        k1=n
                                                        k2=j 
                                                        dem_r=[[0,0,0],[Demandas(n,j),Demandas(n,j),0],[0,0,0]]
                                                        temp=Tempo(rota[i][2],k1,0,"T_Trans",tip_rota)+Tempo(k1,k2,0,"T_Trans",tip_rota)+Tempo(k2,rota[i][0],0,"T_Trans",tip_rota)+2*tipo_v[tip_rota]["tim_V"]
                                                elif ([j,rota[i][0]] is N_SAT) and Demanda["Ori"][filial[j]["Acro"]]["destino"][rota[i][0]]["Dem"]<=tipo_v[k]["cap_V"]:# si hay demanda de volta
                                                    c11=costo(rota[i][2],n,k,k1="C_Vaz")
                                                    c21=costo(n,j,k,k1="C_Car")
                                                    c31=costo(j,rota[i][0],k,k1="C_Car")   
                                                    C1=c11+c21+c31                                                          
                                                    costo_r=min(C1,costo_r)
                                                    if (k1!=i ) and (k1!=j )and(k2!=i ) and (k2!=j )  and min(C1,costo_r)==C1:
                                                        tip_rota=k
                                                        tip_costo=["C_Vaz","C_Car","C_Car"]
                                                        k1=n
                                                        k2=j  
                                                        dem_r=[[0,0,0],[Demandas(n,j),Demandas(n,j),0],[Demandas(j,rota[i][0]),Demandas(j,rota[i][0]),0]]
                                                        temp=Tempo(rota[i][2],k1,0,"T_Trans",tip_rota)+Tempo(k1,k2,0,"T_Trans",tip_rota)+Tempo(k2,rota[i][0],0,"T_Trans",tip_rota)+4*tipo_v[tip_rota]["tim_V"]
                                        elif ([rota[i][2],n] is N_SAT)and Demanda["Ori"][filial[rota[i][2]]["Acro"]]["destino"][n]["Dem"]<=tipo_v[k]["cap_V"]:# si hay demanda de volta
                                            if  not([n,j] is N_SAT):# si no hay demanda de volta
                                                if  not([j,rota[i][0]] is N_SAT):# si no hay demanda de volta
                                                    c11=costo(rota[i][2],n,k,k1="C_Car")
                                                    c21=costo(n,j,k,k1="C_Vaz")
                                                    c31=costo(j,rota[i][0],k,k1="C_Vaz")   
                                                    C1=c11+c21+c31
                                                    costo_r=min(C1,costo_r)
                                                    if (k1!=i ) and (k1!=j )and(k2!=i ) and (k2!=j )  and min(C1,costo_r)==C1:
                                                        tip_rota=k
                                                        tip_costo=["C_Car","C_Vaz","C_Vaz"]
                                                        k1=n
                                                        k2=j
                                                        dem_r=[[Demandas(rota[i][2],n),Demandas(rota[i][2],n),0],[0,0,0],[0,0,0]]
                                                        temp=Tempo(rota[i][2],k1,0,"T_Trans",tip_rota)+Tempo(k1,k2,0,"T_Trans",tip_rota)+Tempo(k2,rota[i][0],0,"T_Trans",tip_rota)+2*tipo_v[tip_rota]["tim_V"]
                                                elif ([j,rota[i][0]] is N_SAT) and Demanda["Ori"][filial[j]["Acro"]]["destino"][rota[i][0]]["Dem"]<=tipo_v[k]["cap_V"]:# si hay demanda de volta
                                                    c11=costo(rota[i][2],n,k,k1="C_Car")
                                                    c21=costo(n,j,k,k1="C_Vaz")
                                                    c31=costo(j,rota[i][0],k,k1="C_Car")   
                                                    C1=c11+c21+c31                                                          
                                                    costo_r=min(C1,costo_r)
                                                    if (k1!=i ) and (k1!=j )and(k2!=i ) and (k2!=j )  and min(C1,costo_r)==C1:
                                                        tip_rota=k
                                                        tip_costo=["C_Car","C_Vaz","C_Car"]
                                                        k1=n
                                                        k2=j
                                                        dem_r=[[Demandas(rota[i][2],n),Demandas(rota[i][2],n),0],[0,0,0],[Demandas(j,rota[i][0]),Demandas(j,rota[i][0]),0]]
                                                        temp=Tempo(rota[i][2],k1,0,"T_Trans",tip_rota)+Tempo(k1,k2,0,"T_Trans",tip_rota)+Tempo(k2,rota[i][0],0,"T_Trans",tip_rota)+4*tipo_v[tip_rota]["tim_V"]
                                            elif ([n,j] is N_SAT)and Demanda["Ori"][filial[n]["Acro"]]["destino"][j]["Dem"]<=tipo_v[k]["cap_V"]:# si hay demanda de ida
                                                if  not([j,rota[i][0]] is N_SAT):# si no hay demanda de volta
                                                    c11=costo(rota[i][2],n,k,k1="C_Car")
                                                    c21=costo(n,j,k,k1="C_Car")
                                                    c31=costo(j,rota[i][0],k,k1="C_Vaz")   
                                                    C1=c11+c21+c31
                                                    costo_r=min(C1,costo_r)
                                                    if (k1!=i ) and (k1!=j )and(k2!=i ) and (k2!=j )  and min(C1,costo_r)==C1:
                                                        tip_rota=k
                                                        tip_costo=["C_Car","C_Car","C_Vaz"]
                                                        k1=n
                                                        k2=j
                                                        dem_r=[[Demandas(rota[i][2],n),Demandas(rota[i][2],n),0],[Demandas(n,j),Demandas(n,j),0],[0,0,0]]
                                                        temp=Tempo(rota[i][2],k1,0,"T_Trans",tip_rota)+Tempo(k1,k2,0,"T_Trans",tip_rota)+Tempo(k2,rota[i][0],0,"T_Trans",tip_rota)+4*tipo_v[tip_rota]["tim_V"]
                                                elif ([j,rota[i][0]] is N_SAT) and  Demanda["Ori"][filial[j]["Acro"]]["destino"][rota[i][0]]["Dem"]<=tipo_v[k]["cap_V"]:# si hay demanda de volta
                                                    c11=costo(rota[i][2],n,k,k1="C_Car")
                                                    c21=costo(n,j,k,k1="C_Car")
                                                    c31=costo(j,rota[i][0],k,k1="C_Car")   
                                                    C1=c11+c21+c31                                                          
                                                    costo_r=min(C1,costo_r)
                                                    if (k1!=i ) and (k1!=j )and(k2!=i ) and (k2!=j )  and min(C1,costo_r)==C1:
                                                        tip_rota=k
                                                        tip_costo=["C_Car","C_Car","C_Car"]
                                                        k1=n
                                                        k2=j
                                                        dem_r=[[Demandas(rota[i][2],n),Demandas(rota[i][2],n),0],[Demandas(n,j),Demandas(n,j),0][Demandas(j,rota[i][0]),Demandas(j,rota[i][0]),0]]
                                                        temp=Tempo(rota[i][2],k1,0,"T_Trans",tip_rota)+Tempo(k1,k2,0,"T_Trans",tip_rota)+Tempo(k2,rota[i][0],0,"T_Trans",tip_rota)+6*tipo_v[tip_rota]["tim_V"]
                                    else:
                                        break
        if (k1!= None and k2!= None) and (k1!=rota[i][0] and k1!=rota[i][2])and (k2!=rota[i][0] and k2!=rota[i][2]):
            Rutas.append([i,rota[i][2],k1,k2,rota[i][0]])
            Costo.append(costo_r)
            Tipo.append(tip_rota)
            tempoA.append(temp)
            tipo_costo.append(tip_costo)
            Dem_r.append(dem_r)
    else:
        continue
        
                    
# Crear elemento en forma de lista para rotas unidas
aux=[]# auxiliar
ruta_con=[] # auxiliar de rota
for i in list(range(len(Rutas))):
    conju=[]
    for k in list(range(len(rota[Rutas[i][0]]))):
            aux=rota[Rutas[i][0]][k]
            
            conju.append(aux)
            if k==len(rota[Rutas[i][0]])-1:# unir rota de volta  
                for k1 in list(range(len(Rutas[i]))):
                    aux=Rutas[i][k1+2]
                    conju.append(aux)
    ruta_con.append(conju) 
 
        
# eliminacion de rutas: 
for i in list(range(len(Rutas))):#sustitucion de unidas e eliminacion de la volta      
            rota[Rutas[i][0]]=ruta_con[i]
            COSTO_R[Rutas[i][0]]=Costo[i]+COSTO_R[Rutas[i][0]]
            t_rota[Rutas[i][0]]=Tipo[i]
            tempo[Rutas[i][0]]=tempoA[i]+tempo[Rutas[i][0]]
            t_custo[Rutas[i][0]]=tipo_costo[i]+t_custo[Rutas[i][0]]
            dem[Rutas[i][0]]=[dem[Rutas[i][0]],Dem_r[i]]

# validacion rutas faltantes
k=0
for i in list(range(len(rota))):
    if len(rota[i])==3:
        print(rota[i])
        k+=1

print(k)

## Re escrever rota de 2 nó como [i-j-i]
# Crear elemento en forma de lista para rotas unidas
aux=[]# auxiliar
ruta_con=[] # auxiliar de rota
for i in list(range(len(rota))):
    conju=[]
    if len(rota[i])==2:   
        for k in list(range(len(rota[i]))):
            aux=rota[i][k]
            
            conju.append(aux)
            if k==len(rota[i])-1:# unir rota de volta  
               aux=rota[i][0]
               conju.append(aux)
        ruta_con.append(conju) 
 
        
# substituição de rutas: 
for i in list(range(len(rota))):#sustitucion de unidas e eliminacion de la volta      
    if len(rota[i])==2:            
        rota[i]=ruta_con[i]

# todas as rotas
for i in list(range(len(rota))):
        print(rota[i])
        

# valor objetivo


FO=sum(COSTO_R)
FO

#CALCULO DOS GANHOS POR ROTA E ORDENAÇÃO
savings=[]# vetor de ganhos
for m in range(len(rota)):
  for n in range(len(rota)):
    if n!=m and n>m and rota[m][0]==rota[n][0] and t_rota[m]==t_rota[n]:
       if val_rota(rota[m][len(rota[m])-2],rota[n][1],0): # validacion existencia rutas ida 
            if costo(rota[m][len(rota[m])-2],rota[n][1],k=t_rota[m],k1="C_Car")!= False:
                cmI=costo(rota[n][0],rota[n][1],k=t_rota[m],k1=t_custo[n][0])

                cmV=costo(rota[m][len(rota[m])-2],rota[m][len(rota[m])-1],k=t_rota[m],k1=t_custo[m][len(t_custo[m])-1])

                cmU=costo(rota[m][len(rota[m])-2],rota[n][1],k=t_rota[m],k1=t_custo[m][len(t_custo[m])-1])

                s=cmI+cmV-cmU
                if abs(s)==s:
                    savings.append([s,[m,n]])
 
       if val_rota(rota[n][len(rota[n])-2],rota[m][1],0): # validacion existencia rutas ida
            if costo(rota[n][len(rota[n])-2],rota[m][1],k=t_rota[m],k1="C_Car")!= False:
                cmI=costo(rota[m][0],rota[m][1],k=t_rota[m],k1=t_custo[m][0])

                cmV=costo(rota[n][len(rota[n])-2],rota[n][len(rota[n])-1],k=t_rota[m],k1=t_custo[n][len(t_custo[n])-1])

                cmU=costo(rota[n][len(rota[n])-2],rota[m][1],k=t_rota[m],k1=t_custo[n][len(t_custo[n])-1])

                s=cmI+cmV-cmU
                
                if abs(s)==s:
                    savings.append([s,[n,m]])
 
print(savings) 


savings=sorted(savings,reverse=True)
print(len(savings))

# factibilidades
tempoA=[]# vetor de tempo da rota unida
factivel=[]# vetor de factivilidade
aux14=0
disponible=[]# vetor de recursos sobrantes da rota unida
for i in range(len(savings)):
    control=None
    
    if savings[i][0]>0:
        # TEMPO TOTAL ROTA UNIDA
        time=tempo[savings[i][1][0]]+tempo[savings[i][1][1]]
        +Tempo(rota[savings[i][1][0]][len(rota[savings[i][1][0]])-2],rota[savings[i][1][1]][1],0,"T_Trans",t_rota[savings[i][1][1]])        
        -Tempo(rota[savings[i][1][1]][0],rota[savings[i][1][1]][1],0,"T_Trans",t_rota[savings[i][1][1]])
        -Tempo(rota[savings[i][1][0]][len(rota[savings[i][1][0]])-2],rota[savings[i][1][0]][len(rota[savings[i][1][0]])-1],0,"T_Trans",t_rota[savings[i][1][0]])
        -2*tipo_v[t_rota[savings[i][1][1]]]["tim_V"]
        
        # vetor de tempo:
        tempoA.append(time)
        aux14+=1

        # TEMPO TOTAL ROTA A    
        time_A=tempo[savings[i][1][0]]
        +Tempo(rota[savings[i][1][0]][len(rota[savings[i][1][0]])-2],rota[savings[i][1][1]][1],0,"T_Trans",t_rota[savings[i][1][1]])        
        -Tempo(rota[savings[i][1][1]][0],rota[savings[i][1][1]][1],0,"T_Trans",t_rota[savings[i][1][1]])
        -1*tipo_v[t_rota[savings[i][1][1]]]["tim_V"]
        
        ## Restrição 14 dias para voltar o carro
        if time<=14*24:
            # print('satisfeito 14 dias')
            dias='factivel'
        else:
            dias="não factivel"
            control="não factivel"
            factivel.append([control, savings[i]])
            continue

        # demandas das rotas A e B
        dem_A=dem[savings[i][1][0]]
        dem_B=dem[savings[i][1][1]]
        
        demanda_U=[]# vector de demandas unidas
 
        # seleção de demanda rota A
        for j in range(len(dem_A)):
            if len(dem_A)==2 and type(dem_A[j])==list:
                k=nivel_dem(dem_A[j])# k = nivel de la demanda
                if k==[1,0]:
                    for p in range(len(dem_A[j])):
                        if len(dem_A[j][p])==3 and type(dem_A[j][p][0])==int:    
                            d1=dem_A[j][p][1]
                            d1a=dem_A[j][p][2]
                            if j>0:
                                p1=1
                            else:
                                p1=0
                            aux1=rota[savings[i][1][0]][j+p+p1]
                            aux2=rota[savings[i][1][0]][j+p+p1+1]
                            if (p==0):
                                aux3=rota[savings[i][1][0]][j+p1+2]
                            if d1!=0:
                                demanda_U.append(["A",[d1,[aux1,aux2]],'d'])
                            if d1a!=0 and p==0:
                                demanda_U.append(["A",[d1a,[aux1,aux3]],'a'])
                if k==[2,0]:
                    for p in range(len(dem_A[j])):
                        if p==1:
                            if len(dem_A[j][p])==3 and type(dem_A[j][p][0])==int:    
                                d1=dem_A[j][p][1]
                                d1a=dem_A[j][p][2]
                                if j>0:
                                    p1=1
                                else:
                                    p1=0
                                aux1=rota[savings[i][1][0]][j+p+p1]
                                aux2=rota[savings[i][1][0]][j+p+p1+1]
                                if (p==0):
                                    aux3=rota[savings[i][1][0]][j+p1+2]
                                if d1!=0:
                                    demanda_U.append(["A",[d1,[aux1,aux2]],'d'])
                                if d1a!=0 and p==0:
                                    demanda_U.append(["A",[d1a,[aux1,aux3]],'a'])
                        if p==0:
                            for q in range(len(dem_A[j])):
                                if len(dem_A[j][p][q])==3 and type(dem_A[j][p][q][0])==int:    
                                    d1=dem_A[j][p][q][1]
                                    d1a=dem_A[j][p][q][2]
                                    if j>0:
                                        p1=1
                                    else:
                                        p1=0
                                    aux1=rota[savings[i][1][0]][j+p+p1+q]
                                    aux2=rota[savings[i][1][0]][j+p+p1+q+1]
                                    if (q==0):
                                        aux3=rota[savings[i][1][0]][j+p1+q+2]
                                    if d1!=0:
                                        demanda_U.append(["A",[d1,[aux1,aux2]],'d'])
                                    if d1a!=0 and p==0:
                                        demanda_U.append(["A",[d1a,[aux1,aux3]],'a'])
            if len(dem_A[j])==3 and type(dem_A[j][0])==int:    
                d1=dem_A[j][1]
                d1a=dem_A[j][2]
                aux1=rota[savings[i][1][0]][j]
                aux2=rota[savings[i][1][0]][j+1]
                if j==0:
                    aux3=rota[savings[i][1][0]][j+2]
                if d1!=0:
                    demanda_U.append(["A",[d1,[aux1,aux2]],'d'])
                if d1a!=0:
                    demanda_U.append(["A",[d1a,[aux1,aux3]],'a'])
 
        # seleção de demanda rota B
        for j in range(len(dem_B)):
            if len(dem_B)==2 and type(dem_B[j])==list:
                k=nivel_dem(dem_B[j])# k = nivel de la demanda
                # print(k)
                if k==[1,0]:
                    for p in range(len(dem_B[j])):
                        if len(dem_B[j][p])==3 and type(dem_B[j][p][0])==int:    
                            d1=dem_B[j][p][1]
                            d1a=dem_B[j][p][2]
                            if j>0:
                                p1=1
                            else:
                                p1=0
                            aux1=rota[savings[i][1][1]][j+p+p1]
                            aux2=rota[savings[i][1][1]][j+p+p1+1]
                            if (p==0):
                                aux3=rota[savings[i][1][1]][j+p1+2]
                            if d1!=0:
                                demanda_U.append(["B",[d1,[aux1,aux2]],'d'])
                            if d1a!=0 and p==0:
                                demanda_U.append(["B",[d1a,[aux1,aux3]],'a'])
                if k==[2,0]:
                    for p in range(len(dem_B[j])):
                        if p==1:
                            if len(dem_B[j][p])==3 and type(dem_B[j][p][0])==int:    
                                d1=dem_B[j][p][1]
                                d1a=dem_B[j][p][2]
                                if j>0:
                                    p1=1
                                else:
                                    p1=0
                                aux1=rota[savings[i][1][1]][j+p+p1]
                                aux2=rota[savings[i][1][1]][j+p+p1+1]
                                if (p==0):
                                    aux3=rota[savings[i][1][1]][j+p1+2]
                                if d1!=0:
                                    demanda_U.append(["B",[d1,[aux1,aux2]],'d'])
                                if d1a!=0 and p==0:
                                    demanda_U.append(["B",[d1a,[aux1,aux3]],'a'])
                        if p==0:
                            for q in range(len(dem_B[j])):
                                if len(dem_B[j][p][q])==3 and type(dem_B[j][p][q][0])==int:    
                                    d1=dem_B[j][p][q][1]
                                    d1a=dem_B[j][p][q][2]
                                    if j>0:
                                        p1=1
                                    else:
                                        p1=0
                                    aux1=rota[savings[i][1][1]][j+p+p1+q]
                                    aux2=rota[savings[i][1][1]][j+p+p1+q+1]
                                    if (q==0):
                                        aux3=rota[savings[i][1][1]][j+p1+q+2]
                                    if d1!=0:
                                        demanda_U.append(["B",[d1,[aux1,aux2]],'d'])
                                    if d1a!=0 and p==0:
                                        demanda_U.append(["B",[d1a,[aux1,aux3]],'a'])
            if len(dem_B[j])==3 and type(dem_B[j][0])==int:    
                d1=dem_B[j][1]
                d1a=dem_B[j][2]
                aux1=rota[savings[i][1][1]][j]
                aux2=rota[savings[i][1][1]][j+1]
                if j==0:
                    aux3=rota[savings[i][1][1]][j+2]
                if d1!=0:
                    demanda_U.append(["B",[d1,[aux1,aux2]],'d'])
                if d1a!=0:
                    demanda_U.append(["B",[d1a,[aux1,aux3]],'a'])
                    
        
        ## restrição prazos das demandas
        for j in range(len(demanda_U)):
            if demanda_U[j][0]=="A"and demanda_U[j][2]=='d':
                if Tempo(demanda_U[j][1][1][0],demanda_U[j][1][1][1],0,"T_Trans",t_rota[savings[i][1][0]])<= Prazo(demanda_U[j][1][1][0],demanda_U[j][1][1][1],0)*24:
                    # print('prazo demanda %d satisfeito',demanda_U[j][1][0])
                    demanda_aux='satisfeita'
                else:
                    demanda_aux='não satisfeita'
                    control="não factivel"
                    break
            elif demanda_U[j][0]=="A"and demanda_U[j][2]=='a':
                for q in range(len(rota[savings[i][1][0]])-1):
                    if demanda_U[j][1][1][0]==rota[savings[i][1][0]][q]:
                        timeB=Tempo(demanda_U[j][1][1][0],rota[savings[i][1][0]][q+1],0,"T_Trans",t_rota[savings[i][1][0]])
                        +Tempo(rota[savings[i][1][0]][q+1],demanda_U[j][1][1][1],0,"T_Trans",t_rota[savings[i][1][0]])
                        if timeB<= Prazo(demanda_U[j][1][1][0],demanda_U[j][1][1][1],0)*24:
                            # print('prazo demanda %d satisfeito',demanda_U[j][1][0])
                            demanda_aux='satisfeita'
                        else:
                            demanda_aux='não satisfeita'
                            control="não factivel"
                            break
            if demanda_U[j][0]=="B"and demanda_U[j][2]=='d':
                if demanda_U[j][1][1][1]==rota[savings[i][1][1]][1]:
                    time_D=time_A+1*tipo_v[t_rota[savings[i][1][1]]]["tim_V"]
                else:
                    k=1
                    time_D=time_A+1*tipo_v[t_rota[savings[i][1][1]]]["tim_V"]
                    while [rota[savings[i][1][1]][k],rota[savings[i][1][1]][k+1]]!=demanda_U[j][1][1]:
                        time_D+=Tempo(rota[savings[i][1][1]][k],rota[savings[i][1][1]][k+1],0,"T_Trans",t_rota[savings[i][1][0]])+2*tipo_v[t_rota[savings[i][1][1]]]["tim_V"]
                        k+=1
                    time_D+=Tempo(demanda_U[j][1][1][0],demanda_U[j][1][1][1],0,"T_Trans",t_rota[savings[i][1][0]])+2*tipo_v[t_rota[savings[i][1][1]]]["tim_V"]
                if time_D<= Prazo(demanda_U[j][1][1][0],demanda_U[j][1][1][1],0)*24:
                    # print('prazo demanda %d satisfeito',demanda_U[j][1][0])
                    demanda_aux='satisfeita'
                else:
                    demanda_aux='não satisfeita'
                    control="não factivel"
                    break
            elif demanda_U[j][0]=="B"and demanda_U[j][2]=='a':
                for q in range(len(rota[savings[i][1][1]])-1):
                    if demanda_U[j][1][1][0]==rota[savings[i][1][1]][q]and q!=0:
                        timeB=Tempo(demanda_U[j][1][1][0],rota[savings[i][1][1]][q+1],0,"T_Trans",t_rota[savings[i][1][0]])
                        +Tempo(rota[savings[i][1][1]][q+1],demanda_U[j][1][1][1],0,"T_Trans",t_rota[savings[i][1][0]])
                        +3*tipo_v[t_rota[savings[i][1][1]]]["tim_V"]
                        if demanda_U[j][1][1][1]==rota[savings[i][1][1]][2]:
                            time_D=time_A+timeB+1*tipo_v[t_rota[savings[i][1][1]]]["tim_V"]
                        else:
                            k=1
                            time_D=time_A+timeB+1*tipo_v[t_rota[savings[i][1][1]]]["tim_V"]
                            while rota[savings[i][1][1]][k+1]!=demanda_U[j][1][1][0]:
                                time_D+=Tempo(rota[savings[i][1][1]][k],rota[savings[i][1][1]][k+1],0,"T_Trans",t_rota[savings[i][1][0]])+2*tipo_v[t_rota[savings[i][1][1]]]["tim_V"]
                                k+=1
                            time_D+=Tempo(rota[savings[i][1][1]][k],demanda_U[j][1][1][0],0,"T_Trans",t_rota[savings[i][1][0]])+2*tipo_v[t_rota[savings[i][1][1]]]["tim_V"]
                        if time_D<= Prazo(demanda_U[j][1][1][0],demanda_U[j][1][1][1],0)*24:
                            # print('prazo demanda %d satisfeito',demanda_U[j][1][0])
                            demanda_aux='satisfeita'
                        else:
                            demanda_aux='não satisfeita'
                            control="não factivel"
                            break
                    
                    if demanda_U[j][1][1][0]==rota[savings[i][1][1]][q]and q==0:
                        timeB=Tempo(rota[savings[i][1][1]][q+1],demanda_U[j][1][1][1],0,"T_Trans",t_rota[savings[i][1][0]])
                        if demanda_U[j][1][1][1]==rota[savings[i][1][1]][2]:
                            time_D=time_A+timeB+3*tipo_v[t_rota[savings[i][1][1]]]["tim_V"]
                        if time_D<= Prazo(demanda_U[j][1][1][0],demanda_U[j][1][1][1],0)*24:
                            # print('prazo demanda %d satisfeito',demanda_U[j][1][0])
                            demanda_aux='satisfeita'
                        else:
                            demanda_aux='não satisfeita'
                            control="não factivel"
                            break
            if demanda_aux=="satisfeita" and control!="não factivel" and j==len(demanda_U): 
                control="factivel"
            else:
                control="não factivel"
                break

        # Restrição de capacidade
        
        #arcos
        for p in range(len(rota[savings[i][1][0]])-1):
            if p+1!=len(rota[savings[i][1][0]])-1:
                arco=[rota[savings[i][1][0]][p],rota[savings[i][1][0]][p+1]]
                soma=0
                for j in range(len(demanda_U)): 
                    if demanda_U[j][0]=="A" and demanda_U[j][1][1]==arco and demanda_U[j][2]=="d":
                        soma+=demanda_U[j][1][0]
                    if demanda_U[j][0]=="A" and demanda_U[j][1][1][0]==arco[0] and demanda_U[j][2]=="a" :
                        soma+=demanda_U[j][1][0]
                    if demanda_U[j][0]=="B" and demanda_U[j][1][1][0]==arco[0] and demanda_U[j][2]=="d":
                        soma+=demanda_U[j][1][0]
                    if demanda_U[j][0]=="B" and demanda_U[j][1][1][0]==arco[0] and demanda_U[j][2]=="a" :
                        soma+=demanda_U[j][1][0]
                if soma<=tipo_v[t_rota[savings[i][1][1]]]["cap_V"]:
                    capFAC="factivel"
                    dispo=[tipo_v[t_rota[savings[i][1][1]]]["cap_V"]-soma,arco]
                else:
                    capFAC="não factivel"
                    control="não factivel"         
                    break
            if p+1==len(rota[savings[i][1][0]])-1:
                arco=[rota[savings[i][1][0]][p],rota[savings[i][1][1]][1]]
                soma=0
                for j in range(len(demanda_U)): 
                    if demanda_U[j][0]=="B" and demanda_U[j][1][1][1]==arco[1] and demanda_U[j][2]=="a":
                        soma+=demanda_U[j][1][0]
                    if demanda_U[j][0]=="A" and demanda_U[j][1][1][0]==arco[0] and demanda_U[j][2]=="a" :
                        soma+=demanda_U[j][1][0]
                    if demanda_U[j][0]=="A" and demanda_U[j][1][1][0]==arco[0] and demanda_U[j][2]=="d":
                        soma+=demanda_U[j][1][0]
                    if demanda_U[j][0]=="B" and demanda_U[j][1][1][1]==arco[1] and demanda_U[j][2]=="d" :
                        soma+=demanda_U[j][1][0]
                if soma<=tipo_v[t_rota[savings[i][1][1]]]["cap_V"]:
                    capFAC="factivel"
                    dispo=[tipo_v[t_rota[savings[i][1][1]]]["cap_V"]-soma,arco]
                else:
                    capFAC="não factivel"
                    control="não factivel"         
                    break
                for q in range(len(rota[savings[i][1][1]])-2):
                    arco=[rota[savings[i][1][1]][q+1],rota[savings[i][1][1]][q+2]]
                    soma=0
                    for j in range(len(demanda_U)): 
                        if demanda_U[j][0]=="B" and demanda_U[j][1][1]==arco and demanda_U[j][2]=="d":
                            soma+=demanda_U[j][1][0]
                        if demanda_U[j][0]=="B" and demanda_U[j][1][1][1]==arco[1] and demanda_U[j][2]=="a" :
                            soma+=demanda_U[j][1][0]
                        if demanda_U[j][0]=="A" and demanda_U[j][1][1][0]==arco[0] and demanda_U[j][2]=="a":
                            soma+=demanda_U[j][1][0]
                        if demanda_U[j][0]=="A" and demanda_U[j][1][1][1]==arco[1] and demanda_U[j][2]=="d" :
                            soma+=demanda_U[j][1][0]
                    if soma<=tipo_v[t_rota[savings[i][1][1]]]["cap_V"]:
                        capFAC="factivel"
                        dispo=[tipo_v[t_rota[savings[i][1][1]]]["cap_V"]-soma,arco]
                    else:
                        capFAC="não factivel"
                        control="não factivel"         
                        break
                    disponible.append(dispo)
                    if q==len(rota[savings[i][1][1]])-3 and p+1==len(rota[savings[i][1][0]])-1  and capFAC=='factivel':
                        control="factivel"
        if capFAC=="factivel" and demanda_aux=='satisfeita' and dias=='factivel':
            control='factivel'
        else:
            control='não factivel'
        factivel.append([control, savings[i]])
            
        print(control)

print(factivel)

for i in range(len(factivel)):
    if factivel[i][0]=='não factivel':
        for j in range(len(savings)):
            
            if savings[j]==factivel[i][1]:
                savings[j]=None
                break
print(savings)


while None in savings:
    savings.remove(None)
print(savings)

# Crear elemento en forma de lista para rotas unidas
aux=[]# auxiliar
ruta_con=[] # auxiliar de rota

for i in list(range(len(savings))):
    conju=[]
    if savings[i]!=None:
        for k in list(range(len(rota[savings[i][1][0]]))):
            aux=rota[savings[i][1][0]][k]            
            conju.append(aux)
            if k==len(rota[savings[i][1][0]])-2:# unir rota de volta
                for k1 in list(range(len(rota[savings[i][1][1]])-2)):
                    aux=rota[savings[i][1][1]][k1+1]
                    conju.append(aux)
        ruta_con.append(conju)   
        
# eliminacion de rutas: 

for i in list(range(len(savings))):#sustitucion de unidas e eliminacion de la volta
    if savings[i]!=mat.inf:
        rota[savings[i][1][0]]=ruta_con[i]
        COSTO_R[savings[i][1][0]]=COSTO_R[savings[i][1][0]]+COSTO_R[savings[i][1][1]]-savings[i][0]
        tempo[savings[i][1][0]]=tempoA[i]
 
        rota[savings[i][1][1]]=mat.inf
        COSTO_R[savings[i][1][1]]=mat.inf
        t_rota[savings[i][1][1]]=mat.inf
        tempo[savings[i][1][1]]=mat.inf
        t_custo[savings[i][1][1]]=mat.inf
        dem[savings[i][1][1]]=mat.inf

        # vector savings sem as rotas unidas
        for j in range(len(savings)):
            if i!=j and savings[j]!=mat.inf:
                if savings[i][1][0]==savings[j][1][0]or savings[i][1][0]==savings[j][1][1]or savings[i][1][1]==savings[j][1][0]or savings[i][1][1]==savings[j][1][1]:
                    savings[j]=mat.inf


while mat.inf in COSTO_R :# eliminacionde rutas sobrantes
    rota.remove(mat.inf)
    t_rota.remove(mat.inf)
    COSTO_R.remove(mat.inf)
    tempo.remove(mat.inf)
    t_custo.remove(mat.inf)
    dem.remove(mat.inf)
    
print(len(savings))
while mat.inf in savings:
    savings.remove(mat.inf)
len(savings)

# valor objetivo
FO1=sum(COSTO_R)
print(' valor objetivo',FO1)
print('redução de custo ',FO-FO1)
