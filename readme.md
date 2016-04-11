# Overview
The "Redshift View Materializer" is intended to allow for easy creation and refreshing of complex calculated tables in Redshift, similar to materialized views in other databases. "View" (yes, I know, they're really tables) definitions can include references to user-defined snippets of SQL code, which allows code to be re-used between multiple views. Views can be re-created programatically whenever necessary allowing, for example, lengthy calculations of complex business statistics to run during a nightly ETL job, rather than when needed by an executive of analyst.

# Usage
To use the view materializer, simply run `materializer.py`. The script is controlled by `config.json` which must contain:

1. A list of snippet names with associated files containing relevant SQL code.
2. A list of views to be created, containing:
  1. The name of the view (i.e., the table you want to create in your database).
  2. The SQL file containing the code for creating the view.
  3. A SQL-formatted list of users and groups that you would like to grant access to the view.

A simple snippet and simple view are provided by default.