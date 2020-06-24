#!/usr/bin/env python
# coding: utf-8

# In[1]:


x_numbers = [1, 2, 3]
y_numbers = [2, 4, 6]


# In[2]:


from pylab import plot, show
plot(x_numbers, y_numbers)


# In[3]:


plot(x_numbers, y_numbers, marker = 'o')


# In[4]:


plot(x_numbers, y_numbers, 'o')


# In[5]:


nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
plot(nyc_temp, marker = 'o')


# In[6]:


years = range(2000, 2013)


# In[8]:


plot(years, nyc_temp, marker = 'o')


# In[9]:


nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]
nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5]


# In[11]:


months = range(1, 13)
plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)


# In[13]:


from pylab import legend
months = range(1, 13)
plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
legend([2000, 2006, 2012])


# In[14]:


from pylab import plot, show, title, xlabel, ylabel, legend
plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
title('Average monthly temperature in NYC')
xlabel('Month')
ylabel('Temperature')
legend([2000, 2006, 2012])


# In[17]:


nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
plot(nyc_temp, marker = 'o')
from pylab import axis
axis()


# In[18]:


axis(ymin = 0)


# In[ ]:




