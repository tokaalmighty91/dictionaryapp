#Create dataframe with column and row names
df=pandas.DataFrame([[],[]],columns=[''], index=[''])

#Create dataframe with dictionaries. Key as column names, value as cell value
df=pandas.DataFrame([{'':''},{'':''}])


df.mean()#Calculate all column means.Type will be pandas.Series
df.column_name #return column

#jupyter notebook shortcut
ctrl + Enter -> run code (cell in edit mode)
while in edit mode, press Enter to go back to Edit mode
alt + Enter -> create new cell
shift + Enter -> run code and create new cell
esc + dd -> delete cell

pandas.read_csv('text.txt', sep='') #read txt files with; 
#if separated by commas, no need to specify

pandas.set_index('column_name')

#Data slicing
df.loc['index value1':'index value2','column_name1':'column_name2']
df.loc[:,'column_name']
df.iloc[:, :] #position based indexing
df.ix[:, 'column_name'] #find cells based on row # and column name

#Deleting rows or columns
df.drop('column_name', 1) #1 is to tell pandas to delete a column
df.drop('row_name',0) #0 is to delete a row
#delete more than one row and column
df.drop(df.index[1:3],0)#delete rows
df.drop(df.column[1:3],1)#delete columns

#Add column and row
df['column_name']=['']
#to create a column of same value. df.shape[0] returns the same value of shape tuple
df['column_name']=df.shape[0]*['value to pass in the column'] 
#update column values based on another column values
df['column_name']=df['another_column_name']+ 'something'
#add a new row
df_new=df.T #transpose original dataframe, then add a new column
df_new.T #transpose again back to original format

