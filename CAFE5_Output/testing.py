def readFile(baseDir, dirname, filename):
    """ Read in csv file from the basedir and the specific dir names into a pandas dataframe and convert all counts to integers. Return the dataframe""" 
    filepath = os.path.join(baseDir, dirname, filename) 
    return pd.read_csv(filepath, header=0, sep='\t' index_col=0, converters={'count': lambda x: int(x)})


    df=pd.read_csv(baseDir+dirname+filename, sep='\t')
    df.iloc[:,1:].astype(int) # convert all to integers after name. 
    return df


def text_to_bow(some_text):
  """ accepts some_text and set bow_dictionary as an empty dictionary and return """ 
  bow_dictionary = {}
  for word in some_text.split():
    if word in bow_dictionary:
      bow_dictionary[word] += 1
    else:
      bow_dictionary[word] = 1
  return bow_dictionary

def create_features_dictionary(documents):
  """ Take a training set input (documents and returns a dictionary of words with the number of instances.""" 
  