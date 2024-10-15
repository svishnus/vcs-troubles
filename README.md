# Issues with traditional Version Control Systems (VCS)

- Each branch in this repository represents a user change

- When Alice tries pulling in Bob's changes for each of the cases, we observe merge conflicts in `alice-rename` and `alice-move`

## Granularity Problem

 1. Alice renames `func1` to `add` in **alice-rename**
 2. Bob adds a param `c` to `func1` in **bob-add-param** 

- Could not figure out that renaming and adding a parameter are morally independent actions (observe extra-linguistic markers after changes pulled in **alice-rename**)

## Relocation Problem

1. Alice relocates `func1` below `func2` in **alice-move**
2. Bob renames `func1` to `sum` in **bob-rename**

- Could not detect that the definition was relocated when its name was changed (observe extra-linguistic markers after changes pulled in **alice-move**)
