#!/usr/bin/env python
# coding: utf-8

# # Dimensionnez votre biodigesteur domestique
# 
# Ce document est régi par les termes de la licence juridique [Creative Commons CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.fr) 
# 
# ---

# In[1]:


filename = r'./Analyse_TechnicoEconomique.xlsx'


# Import des donnees calc

import pandas as pd
import numpy as np

# pd.set_option('display.float_format', '{:.1f}'.format)

def variable_creation(filepath):
    
    # Lecture du tableau export_data du fichier filename.
    df = pd.read_excel(filepath, sheet_name="export_data",
                             engine="openpyxl").dropna(how='all')
    df = df.to_numpy()
    
    # Initialisation tableau des variables à importer dans Jupyter.
    dfi = [0]*(df.shape[0])
    for i in range(0,df.shape[0]):

        # Routine pour extraire et enregistrer les valeurs depuis le fichier Excel/Ods
        name_sheet = df[i][2]
        col_use = df[i][3]
        skip_r = df[i][4]-1
        n_row = df[i][5]   
        # Extraction et création de la variable i du tableur --> python (numpy)
        dfi[i] = pd.read_excel(filepath, 
                  sheet_name = name_sheet, 
                  skiprows = skip_r,  
                  nrows= n_row, 
                  usecols = col_use,
                  engine="openpyxl").dropna(how='all')
        dfi[i] = dfi[i].replace(np.nan, '', regex=True)
        globals()[df[i][0]]=dfi[i].round(decimals = 4) 
        
variable_creation(filename)

def pd_df_mef(df,nb_round):
           
    styler = df.style.hide(axis='index')\
    .set_properties(subset=[df.columns[0]],
                    **{'font-weight': '', 'background-color': 'white', 'color': ''})\
    .set_caption('')\
    .format(precision=nb_round)
    
    return styler



# ## Les intrants
# 
# Nous vous présentons ici les différents intrants que vous avez selectionné ainsi que leurs caractéristiques :

# In[2]:


pd_df_mef(tab_intrant,2)


# ## Les informations digesteurs
# 
# Retrouvez ici les informations propres aux digesteurs :

# In[3]:


pd_df_mef(info_dig,2)


# ## Les informations techniques
# 
# Ici les informations techniques :

# In[4]:


pd_df_mef(tab_temperature,1)

