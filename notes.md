 
3. DATA WRANGLING 

  3.1 PANDAS DEEP DIVE

  dealing with encoding issues:
  >>> import sys
  >>> reload(sys)
  >>> sys.setdefaultencoding('utf-8')

  *unstack* starts with a U so think up, while stack brings a dimension down. *Warning* in order for unstacking to bring a vertical dimension up to run horizontaly there has to be a remaining vertical dimension else dataframe is represented as a series.


  3.2 DATA CLEANING WITH PANDAS

  * determining encoding being used:
  >>> import chardet
  >>> chardet.detect(rawdata)
  {'encoding': 'EUC-JP', 'confidence': 0.99}

  * decoding using:
  >>> from unidecode import unidecode
  >>> print u'H\xeb\xe4vy M\xebt\xe41'
  Hëävy Mëtäl
  >>> unidecode(u'H\xeb\xe4vy M\xebt\xe41')
  'Heavy Metal'

  * exploring the data
  >>> df.describe()
  >>> df.info()

  * converting types:
  >>> pd.read_csv(..., dtype={"column_1": int, "column_2": object})
  >>> df.column = df. column.astype(int)

  * dealing with missing data
  1) converting custom N/A values:
  >>> pd.read_csv(..., na_values=["N/A", "Unknown"])
  >>> df.replace("N/A", None)

  2) dropping nulls
  >>> df.dropna(axis=1, how="all")
  >>> df.fillna(method="bfill")
  >>> df.interpolate()

  3) dealing with inconsistant values
  >>> df = df.replace({"UI":["EA", "EACH", "PR" ...]},
                      {"UI":["Each", "Each", "Pair" ...]})
  >>> df = df.replace({"UI":"Unknown"}, {"UI":np.NaN})

  * check if items exist in a list
  >>> dontcare = df.UI.value_counts()[20:]
  >>> df = df[~df.UI.isin(dontcare.index)]

  * regex and other string functions
  >>> df.column[df.column.str.contains("(\d{4}-\d{2}-\d{2})")]
  >>> df["Item Name"].str.lower()

  * reshaping data
  >>> df.pivot(index='date', columns='variable', values='value')
  >>> df.groupby("State")[['Acquisition Cost']].sum()

  >>> df4
  >>> f = lambda x: len(str(x))
  >>> df4['one'].map(f)

  * merging datasets
    * Make sure the types match
    * Check dataframe size before and after
    * Try with how=inner and how=outer
    >>> pd.merge(ages, weights, left_on="cats", right_on="cats", how="outer")

  * visualize data
    * ggplot
    * bokeh
    * seaborn
    * matplotlib
    * glue #has a type of QlikView functionality with ability to have many graphs and see the impact of selections in one graphs on the others.

  * extractign data from PDFs
    * tool called tabula that allows you to select a table within a pdf and turn it into a csv for you

  * scaling up
    Sometimes repeatability matters
    * Build tools: Make, tup
    * Data pipelines: OKFN Bubbles, Storm, Spark, Blaze, etc

  * Takeaways
    * Use the proper types for things
    * Data has a tendency to be used in unanticipated ways (consider how others coulld use this)
    * Documentation matters (source, possible range of values, how was it gathered?)
    * Fix data at source (use drop-downs)
    * Data cleaning is a necessary evil



