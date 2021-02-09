# SQLite in practice

Data & solutions to Anton Zhiyanov's course “[SQLite in practice](https://stepik.org/course/90778/info)”.

## SQLite statistical functions

Adapted library from [Liam Healy's extension-functions.c](https://sqlite.org/contrib/) by [@nalgeon](https://github.com/nalgeon/sqlite-stats).
Download the latest version from [GitHub](https://github.com/nalgeon/sqlite-stats/releases/latest) or look it up in [libs](libs) directory.

You can load `sqlite3-stats` using:
- SQLite shell: `sqlite> .load ../libs/sqlite3-stats` 
- SQL query: `select load_extension('../libs/sqlite3-stats');`