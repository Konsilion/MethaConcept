#!/usr/bin/env python
# coding: utf-8

# # Dimensionnez votre biodigesteur domestique
# 
# Ce document est régi par les termes de la licence juridique [Creative Commons CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.fr) 
# 
# :::{tip} To auto-exclude all files outside of your table of contents, see :::
# 
# :::{seealso} and . :::
# 
# :::{important} The default behaviour of cache is now to run in the local directory. This is a change from v0.7. :::
# 
# 
# 
# ---

# * Pour commencer, téléchargez le tableur

# In[1]:


# Import des donnees calc

import pandas as pd
import numpy as np
import ipywidgets as widgets


# [Lien de téléchargements WEB](https://konsilion.fr/wp/wp-content/uploads/2022/07/MetaConcept.xlsx)

# ---
# 
# 2. Une fois le tableur remplis, vous pouvez le reverser dans la machine.

# In[2]:


uploader = widgets.FileUpload(
    accept='.xlsx',  # Accepted file extension e.g. '.txt', '.pdf', 'image/*', 'image/*,.pdf'
    multiple=False  # True to accept multiple files upload else False
)

display(uploader)



# In[3]:


uploaded_file = uploader.value['MetaConcept.xlsx']


# In[11]:


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

# In[6]:


pd_df_mef(tab_intrant,2)


# ## Les informations digesteurs
# 
# Retrouvez ici les informations propres aux digesteurs :

# In[7]:


pd_df_mef(info_dig,2)


# ## Les informations techniques
# 
# Ici les informations techniques :

# In[15]:


pd_df_mef(tab_temperature,1)


# In[ ]:




