SCCM4910 coursework: public example data
Read the accompanying brief.

The examples explain the requirement. Write your own assessed function,
tests and configuration; these are not a complete test suite.

After implementing the function, from your repository root:
  python3 batch_runner.py data/normal.csv results.csv
  python3 batch_runner.py data/mixed.csv mixed-results.csv

normal.csv: 6 successful calculations.
mixed.csv: 8 calculations, 4 successes and 4 errors; later valid rows continue.
The runner reports individual errors to standard error and a summary to
standard output. Completed batches exit 0, including batches with errors.
Calculation errors are identified in the output CSV.
The output header is row,status,result,error_code. For successful calculations,
status is OK and error_code is empty because there is no error to report.

Expected CSV files show the outputs. Compare CSV fields/numeric values rather
than bytes: 5 and 5.0 are equivalent, and LF/CRLF line endings are accepted.
The marking comparison allows 1e-9 relative or absolute numeric tolerance.

Optional examples handled by supplied code:
  header-only.csv: output header only and a zero-count summary.
  invalid-header.csv: helpful error, no output written, exit status 1.
You do not need to implement or test these file-handling cases.

Use different ordinary numeric values within the stated range in your tests.
Do not change expected results to make an incorrect implementation pass.
