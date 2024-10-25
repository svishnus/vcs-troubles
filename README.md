# Issues with traditional Version Control Systems (VCS)

- This repository serves as an example of the granularity and relocation problems in practice due to 3-way merge-and-diff heuristics.

- Each branch in this repository represents a user change.

- When Alice tries pulling in Bob's changes for each of the cases, we observe merge conflicts in `alice-rename` and `alice-move`.

- **checkout** `alice-rename` and `alice-move` to see the extralinguistic markers that git inserts.

- Note that we cannot parse, typecheck, or run code in the presence of these markers.

## Granularity Problem

 1. Alice renames `func1` to `add` in **alice-rename**.
 2. Bob adds a param `c` to `func1` in **bob-add-param**.

- Git could not figure out that renaming and adding a parameter are morally independent actions (observe extra-linguistic markers after changes pulled in **alice-rename**)

## Relocation Problem

1. Alice relocates `func1` below `func2` in **alice-move**.
2. Bob renames `func1` to `sum` in **bob-rename**.

- Gitc could not detect that the definition was relocated when its name was changed (observe extra-linguistic markers after changes pulled in **alice-move**)
