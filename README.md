# Head-to-Head Win-Loss Matrix Table Generator

## Overview

This Python script demonstrates how to process structured JSON data and build a head-to-head win-loss matrix table for a set of teams. The output is presented in a tabular format in a similar style to the example table in the Sports Reference Engineering Application question

## Problem Description

Given a JSON file that includes each team's win-loss records versus opponents, the task is to write a script that builds a matrix of head-to-head records in table form.

## Solution Approach

In the example table, we see that each row displays the team's wins against other opponents and each column represents their losses. Diagonal entries are empty since they represent a team's record against itself.

This solution leverages the parallel structure of a win-loss matrix. The number of losses that team A has against team B are equivalent to the number of wins team B has against team A. Therefore, we can build the win-loss matrix by only extracting the wins each team has against all other opponents. Each team's number of wins are stored in a list, and these lists are appended to the win-loss matrix, building the entire table.

At a high level, the solution follows these steps:

1. **Parse input JSON data**
- Read and load the JSON data as a dictionary in Python.

2. **Construct the matrix**
- Iterate through teams and opponent records to extract number of wins.
- Insert placeholders along the diagonal to represent self-matchups.

3. **Prepare matrix for display**
- Add row and column labels to make the table readable.

4. **Plot table**
- Generate a table-style visualization of the win-loss matrix.
- Save the output table as a png file to an output folder.

## Project Structure

```text
.
├── jonathan_calixto_application.py         # Script for generating win-loss matrix table from JSON data
├── README.md                               # Project description and documentation
├── team_record.json                        # Input data (from application)
└── table/                                  # Output folder with table visualization
    └── win_loss_matrix_table.png
```

## Usage

The script is designed to be run from the command line with a JSON file as an input. Your current working directory must be the folder containing the Python script.

Make the script executable (only required once):

```bash
chmod +x jonathan_calixto_application.py
```

Run the script, providing the path to the input JSON file:

```bash
./jonathan_calixto_application.py /path/to/data.json
```

Alternatively, the script can be run using:

```bash
python3 jonathan_calixto_application.py /path/to/data.json
```

## Assumptions

There are a few assumptions that I made for the script, in both the input and the output.

### Input

1. JSON data format

    - Data is in proper JSON format

    - JSON format is the same as the one in the example win-loss data in the application:

        ```text
        teams
        ├── opponents:
            ├── W
            ├── L
        ```

    - Win values are stored under the key "W" and are integers

### Output

1. Formatting of the example table.

    - Stubhead (row label descriptor) is abbreviated as "Tm", for "Teams"

## Dependencies

- Python 3.8+

- matplotlib