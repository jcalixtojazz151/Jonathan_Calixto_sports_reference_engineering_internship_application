import json
import argparse
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt


def create_table(matrix: list, column_labels: list):
    """
    Creates a matplotlib table for a wins and losses matrix using 
    
    :param matrix: Description
    :type matrix: list
    :param column_labels: Description
    :type column_labels: list
    """

    # Define the background and text colors for the column labels
    column_label_background_color = "lightgray"
    column_label_text_color = "firebrick"
    
    # Define the matplotlib figure

    plt.figure(figsize=(6, 3.5))

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

    # Save the figure to a figures folder inside the directory

    code_path = Path(__file__).resolve().parent

    plt.savefig(str(code_path) + "/win_loss_matrix_table.png", dpi = 250)



def json_to_table(path: str):

    # Open json file with the data

    with open(path, 'r') as file:
        data = json.load(file)

    # Define and fill the matrix (nested list) with the win-loss information of each team

    matrix = []
    teams = list(data.keys())

    for index_in_list, team in enumerate(teams):
        
        # For each team, we store their records against all opponents
        team_record = data[team]

        # Define a wins list to be filled with the victories against all opponents - each row in the matrix is the wins of a single team
        # against the rest. We only need the wins of each team to fill the matrix row by row (list by list).
        wins = []

        # We extract the team's number of wins against each opponent
        for opponent in team_record:
            wins.append(team_record[opponent]["W"])
        
        # Insert a "--", equivalent to NA along the diagonal. The team does not win or lose against itself.
        wins.insert(index_in_list, "--")
        
        # Add all the wins to that team's row
        matrix.append(wins)

    # Define the column labels, include the column description "Tm" (for display purposes)

    column_labels = ["Tm"] + teams

    # Add the column of team names in front of the table (for display purposes)

    for i, row in enumerate(matrix):
        row.insert(0, teams[i])

    matrix.append(column_labels)

    # Use the defined function create_table to create a matplotlib table using the matrix (nested list) and column labels
    
    create_table(matrix=matrix, column_labels=column_labels)


parser = argparse.ArgumentParser()
parser.add_argument("file_path", help = "the file path of the json file with team wins and losses versus opponents", type = str)
args = parser.parse_args()

json_to_table(args.file_path)