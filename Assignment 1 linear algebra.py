#!/usr/bin/env python
# coding: utf-8

# In[17]:


A=matrix([[0,1,0,0],[1,0,1,1],[0,1,0,1],[0,1,1,0]])#This is adjacency matrix of graph G
show(Graph(A)) #This show the graph G


# In[18]:


A.eigenvalues() #This gives the eigenvalues of A


# In[19]:


D,P=A.eigenmatrix_right()#This code give us D the diagonal matrix of eigenvalues
                        #P which is the matrix that diagonalizes A


# In[20]:


P #The columns are eigenvectors of adjacency matrix A


# In[21]:


D #This prints out the diagonal matrix of eigenvalues.


# In[22]:


A*P == P*D #This code checks if the matrix we found indeed diagonalize A
#This returns a boolean that checks if what we obtained is true or false


# In[23]:


P.inverse()*A*P == D #This code checks that P diagonilzes the adjacency matrix of the graph G

