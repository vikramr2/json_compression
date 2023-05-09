# json_compression
.json compression application for converting MACHINA outputs into interpretable inputs for MACHINA-Viz
<!-- TABLE OF CONTENTS -->
## Table of Contents
* [Depenndencies](#Dependencies)
* [Setup](#Setup)
* [Run](#Run)
* [Directory Structure](#Directory)
* [Output Structure](#Output)
## Dependencies
Make sure to have Python3 installed
## Setup
Simply run
```bash
chmod +x install.sh
./install.sh
```
## Run
Simply run the shell script on a directory containing all the output files from MACHINA.
```bash
./run.sh <MACHINA output directory>
```
## Directory
Your directory should have one of the following structures:
```
- Input Directory
  - solution1.tree
  - solution1.labeling (You can change the name from solution1 as long as the tree and labeling have the same name)
  - solution2.tree
  - solution2.labeling
  - ...
  - coloring.txt (Optional)
```
or 
```
- Input Directory
  - pmh
    - solution1.tree
    - solution2.tree
    - ...
  - potential_labelings
    - solution1.labeling
    - solution2.labeling
    - ...
  - coloring.txt (Optional)
```
## Output
The program will compress the directory into a single json file containing the following format:
```
{
  "name": <patient name>,
  "solutions": [
    {
      "name": <solution name>,
      "tree": [
        [u, v],
        ...
      ],
      "labeling": [
        [n, label],
        ...
      ],
      "migration": [
        [label_u, label_v, # occurences],
        ...
      ]
    },
    ...
  ],
  "summary": {
    "migration": [
      [label_u, label_v, # occurences],
      ...
    ]
  }
}
```
