#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ipywidgets as widgets


# # Importer vos données

# In[2]:


uploader = widgets.FileUpload(
    accept='.xlsx',  # Accepted file extension e.g. '.txt', '.pdf', 'image/*', 'image/*,.pdf'
    multiple=False  # True to accept multiple files upload else False
)

display(uploader)


# In[3]:


uploaded_file = uploader.value['MetaConcept.xlsx']


# In[ ]:




