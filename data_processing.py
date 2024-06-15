import pandas as pd

class data:

    def create_dataframe(path):
        """
        Creates dataframe from productor excel file and creates table with a 'Round' column

        :param path: path to excel file
        """ 
        excel_df = pd.read_excel(path)
        design_titles = excel_df['Unnamed: 3'].copy()
        design_titles_df = pd.DataFrame({'Titles':design_titles.values, 'Round' :0})
        design_titles_df.drop(index=design_titles_df.index[0], axis=0, inplace=True)
        # print(design_titles_df)
        
        save_file_path = data.parse_IO_path(path)
        design_titles_df.to_csv(save_file_path + '/Titles_table.csv', index=False)
        # design_titles_df.to_csv("C:/Users/Administrator/Desktop/Product_Multiplier/Titles_Table.csv")

    def parse_IO_path(path):
        """
        Returns the path of the folder where the productor excel file is

        :param path: path to excel file
        """
        list = path.split('/')
        list.pop()
        path_str = '/'.join(list)
        
        return path_str

    def next_title(path, first_attempt, temp_row):
        """
        Returns round # & string of a title which is up next based on round #

        :param path: path to csv file
        """
        csv_df = pd.read_csv(path)
        # for row in csv_df['Round']:
        print('THIS IS TEMP_ROW: ' + str(temp_row))
        for row in csv_df.index:
            # print('----------------Row count: ' + str(row) + ' | Round: ' + str(csv_df['Round'][row]))
            if row == len(csv_df.index) -1 :
                # print('----------------Length: ' + str(len(csv_df.index)))
                # print('----------------ROW COUNT EQUALS LENGTH----------------')
                # print('mATCH? ' + str(csv_df['Round'][len(csv_df.index) -1]) +' VS '+ str(csv_df['Round'][0]))
                row = 0
                if csv_df['Round'][len(csv_df.index) -1] <= csv_df['Round'][0] and first_attempt is True:
                    # print('----------------IIIINNNNN----------------')
                    print('TITLE: ' + csv_df['Titles'][len(csv_df.index) -1])
                    temp_row = row
                    return str(csv_df['Titles'][len(csv_df.index) -1]), len(csv_df.index) -1, temp_row
            if csv_df['Round'][row] < csv_df['Round'][row + 1] or csv_df['Round'][row] == 0 and first_attempt is True:
                # print(str(csv_df['Round'][row]) + ' VS ' + str(csv_df['Round'][row + 1]))
                print('TITLE: ' + csv_df['Titles'][row])
                temp_row = row
                return str(csv_df['Titles'][row]), row, temp_row
            if first_attempt is False:
                temp_row += 1
                print('TITLE: ' + csv_df['Titles'][temp_row])
                return str(csv_df['Titles'][temp_row]), row, temp_row

    def complete_round(row, path):
        """
        Adds a +1 count on the 'Round' column of 'Titles_table.csv' to the title which finished a round

        :param row: Row number of table
        :param table: Table of 'Titles_table.csv'
        """
        csv_df = pd.read_csv(path)
        # csv_df['Round'][row] = csv_df['Round'][row]  + 1
        csv_df['Round'][row] += 1
        save_file_path = data.parse_IO_path(path)
        csv_df.to_csv(save_file_path + '/Titles_table.csv', index=False)
        print(csv_df.loc[[row]])
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&-------- ROUND COMPLETE------&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')