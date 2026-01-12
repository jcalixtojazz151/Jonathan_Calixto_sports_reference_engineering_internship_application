# Head-to-Head Win-Loss Matrix Table Generator

## Overview

This python script demonstrates how to process structured JSON data and build a head-to-head win-loss matrix table for a set of teams. The output is presented in a tabular format in a similar style to the example table in the Sports Reference Engineering Application question

## Problem description

Given a json file that includes each team's Win-Loss records versus opponents, the task is to write a script that builds a matrix of head-to-head records in table form.

## Solution approach

In this matrix, each row displays the team's wins against other opponents and each column represents their losses. Diagonal entries are empty since they represent a team's record against itself.

I solved this problem by identifying the parallel structure of a win-loss matrix. The number of losses that team A has against team B are equivalent to the number of wins team B has against team A. Therefore, we can build the matrix by only extracting the wins each team has against all their opponents. Each team's number of wins are stored in a list, and these lists are appended to the win-loss matrix, building the entire table.

At a high level, the solution follows these steps:

1. Parse input JSON data

- Read and load the JSON data as a dictionary in Python.

2. Construct the matrix

- Iterate through teams and opponent records to extract number of wins.

- Insert placeholders along the diagonal to represent self-matchups.

3. Prepare matrix for display

- Add row and column labels to make the table readable.

4. Plot table

- Generate a table-style visualization of the win-loss matrix.

- Save the output table as a png file to an output folder.

## Project structure




## Usage

## Assumptions

### Input format

### Output

## Packages used