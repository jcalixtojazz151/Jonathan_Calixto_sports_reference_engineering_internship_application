#!/usr/bin/env python3

import os
import json
import argparse
from pathlib import Path
import matplotlib.pyplot as plt

# Global variables:
parent_path = str(Path(__file__).resolve().parent)
output_folder_name = parent_path + "/table"
output_file_name = "win_loss_matrix_table.png"
column_label_background_color = "lightgray"
column_label_text_color = "firebrick"
table_image_dpi = 250
table_figure_size = (6, 3.5)
stubhead_text = "Tm"
NA_for_table = "--"


def read_in_json(path: str) -> tuple[list, list]:
    """
    Read in JSON file and build win-loss matrix as a nested list
    
    Parameters:
    path (str): path to JSON file that includes head-to-head wins and losses

    Returns:
    matrix (list): win-loss matrix as a nested list
    teams (list): list of team names (the keys of JSON data)
    """

    # Open json file with the data

    with open(path, 'r') as file:
        data = json.load(file)

    # Define and fill the matrix (nested list) with the win-loss information of each team

    matrix = []
    teams = list(data.keys())

    for index_in_list, team in enumerate(teams):
        
        # For each team, we store their records against all opponents
        team_record = data[team]

        # Define a wins list to be filled with each team's number of wins against other opponents - each row 
        # in the matrix is the wins of a single team against the rest.
        # We only need the wins of each team to fill the matrix row by row (list by list).
        wins = []

        # We extract the team's number of wins against each opponent
        for opponent in team_record:
            wins.append(team_record[opponent]["W"])
        
        # Insert a symbol to represent NA along the diagonal. The team does not win or lose against itself.
        # NA_for_table is a variable that can be changed at the top of the script
        wins.insert(index_in_list, NA_for_table)
        
        # Add all the wins to that team's row
        matrix.append(wins)

    return matrix, teams


def prepare_display_matrix(matrix: list, teams: list) -> tuple[list, list]:
    """
    Prepare the win-loss matrix for display with row and column labels, matching the style of the sample table from the application
    
    Parameters:
    matrix (list): win-loss matrix as a nested list
    teams (list): list of team names
    
    Return:
    matrix (list): win-loss matrix as a nested list for display/printing - with row and column labels
    column labels (list): list of column labels, including team names and stubhead (top left corner of table)
    """

    # Define the column labels, including the stubhead (for display purposes)
    # Stubhead text is a variable that can be changed at the top of the script

    column_labels = [stubhead_text] + teams

    # Add the column of team names in front of the table (for display purposes)

    for i, row in enumerate(matrix):
        row.insert(0, teams[i])

    
    # Add the row of team names at the bottom of the table (for display purposes)

    matrix.append(column_labels)

    return matrix, column_labels


def plot_table(matrix: list, column_labels: list) -> None:
    """
    Plot the win-loss matrix as a table using matplotlib
    
    Parameters:
    matrix (list): win-loss matrix as a nested list for display/printing - with row and column labels
    column_labels (list): list of column labels, including team names and stubhead (top left corner of table)

    Returns:
    None: saves matplotlib table as fileon the parent folder of this code file
    """
    
    # Define the matplotlib figure

    plt.figure(figsize=table_figure_size)

    # Remove any axes because we are only drawing a table, not a graph

    ax = plt.gca()
    ax.axis('off')

    # Define the table, center it in the axes, and add column labels

    table = plt.table(cellText = matrix, 
                        loc = "center", 
                        colLabels=column_labels, 
                        colLoc = "center")

    table.scale(1, 1.5)

    # Styling for column labels at top/bottom of table and row labels

    for x in range(len(column_labels)):
        top_column_labels = table[(0, x)]
        top_column_labels.get_text().set_color(column_label_text_color)
        top_column_labels.get_text().set_fontweight("bold")
        top_column_labels.set_facecolor(column_label_background_color)

        bottom_column_labels = table[(len(column_labels), x)]
        bottom_column_labels.set_facecolor(column_label_background_color)
        bottom_column_labels.get_text().set_fontweight("bold")
        bottom_column_labels.get_text().set_horizontalalignment("center")

        row_labels = table[(x, 0)]
        row_labels.get_text().set_horizontalalignment("center")

    # Save the figure to a table figures folder inside the parent folder
    # Parent path, output_folder_name, output file name, and table image dpi are variables that can be changed at the top of the script

    os.makedirs(output_folder_name, exist_ok=True)

    plt.savefig(output_folder_name + "/" + output_file_name, dpi = table_image_dpi)



def main() -> None:
    """
    Parse JSON file path argument and run functions to plot table
    """

    parser = argparse.ArgumentParser(description="Generate a win/loss matrix table from a JSON file")
    parser.add_argument("file_path", help = "Path to the JSON file with team record", type = str)
    args = parser.parse_args()

    matrix, teams = read_in_json(path=args.file_path)
    display_matrix, column_labels = prepare_display_matrix(matrix=matrix, teams=teams)
    plot_table(matrix=display_matrix, column_labels=column_labels)



if __name__ == "__main__":
    main()

    