import numpy as np
import pandas as pd


class Cloudy(object):
    """
    Parses Cloudy output files into Pandas DataFrames for analysis.

    There is one main DataFrame and a list of data frames (see _Attributes).
    The reasoning for the list is to make it easier to graph and analyze.

    Parameters
    ----------
    grd : str
        Path to the .grd file from the Cloudy output.
    data : str
        Path to the output file with the data to be analyzed.

    Attributes
    ----------
    grd : numpy array
        Array(s) of the data from the grd file.
    df : DataFrame
        DataFrame of the data file.
    labels : list
        The column headers of the data file. Makes easier access to df.
    dfs : list
        List of DataFrames that are subcategories of the main DataFrame.
    """

    def __init__(self, grd, data):
        self.grd = self._read_grd(grd)
        self.df = self._make_df(data)
        self.labels = sorted(list(self.df.columns[1:]))
        self.dfs = self._make_dfs()

    def __repr__(self):
        return repr(self.labels)

    def __getitem__(self, key):
        return self.df[key]

    def _read_grd(self, grd):
        """Read the grd file into a numpy array"""
        df = self._make_df(grd)  # Turn grd into a data frame
        array = df['grid parameter string'].as_matrix()  # Column with Data
        # If the values are not floats, convert.
        if array.dtype != 'float64':
            # Turn [('1', '2'), ('3', '4')] to [[1.,2.], [3.,4.]]
            array = np.array(
                [item.split(',') for item in array]).astype('float')
        return np.column_stack(array)

    def _make_df(self, data):
        """Turn the data file into a DataFrame"""
        names = self._get_header(data)  # Get Column names
        # Create DataFrame
        df = pd.read_table(
            data, sep='\t', header=None, skiprows=1, names=names, comment='#')
        return df

    def _make_dfs(self):
        """Make a list of DataFrames containing subcategories of the main df

        The subcategories are based on the iterations in the cloudy. For
        example, if cloudy iterated over 3 hdens first and then 100
        temperatures, the list would contain 3 different DataFrames with 100
        indices, one for each hden. However, if the temperatures was iterated
        first and then hden, there would be 100 DataFrames with three indices.
        So the order in which the user runs cloudy is important

        TODO: Give ability to choose/change how dfs are sub-categorized"""
        dfs = [self.df]  # Initiate dfs list
        num_arrs = len(self.grd)  # Number of Arrays
        # When there are more than 1 arrays, then there will be categories
        if num_arrs > 1:
            for n in range(num_arrs - 1):
                groups = sorted(list(set(self.grd[n])))
                dfs = [
                    self._create_df_list(df, groups, self.grd[n]) for df in
                    dfs]
        return dfs

    def _create_df_list(self, df, groups, grd):
        """Create a subcategories of the the df"""
        df_list = []
        for group in groups:
            # Index the df to contain only the specific group
            df_list.append(df[grd == group])
        return df_list

    def _get_header(self, filep):
        """Grab the column headers for the df"""
        with open(filep, 'r') as filein:
            line = filein.readline()[1:-1]
            header = line.split('\t')
        return header
