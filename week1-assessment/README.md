Approach & Logic

The CSV file is read manually using basic file handling functions such as open(), readlines(), and split().  

The first row of the file is treated as the header, and the remaining rows are considered as data records.

The program processes the file in multiple stages:
- Reading raw lines from the CSV file
- Separating column headers and data rows
- Cleaning column names to remove extra spaces
- Processing data row by row 

Handling Missing Values
In this assessment, missing values appear as:
- Empty strings (`""`)
- `"NA"`
- `"null"`
- `"None"`

- Use of NumPy
NumPy is used only for statistical calculations such as mean, median, and standard deviation after valid numeric values are extracted and converted to floats.  
It is not used for reading, cleaning, or manipulating the CSV file.

- Frequency Analysis
  
All valid values are normalized (converted to lowercase), and missing values are ignored.  
The top 5 most frequent values are then identified by sorting the dictionary based on counts.

No external libraries are used for this process.

-  Output Generation
After analysis, a summary report is generated in a text file named summary_report.txt 

This report includes:
- Column analyzed
- Total records processed
- Missing value count
- Mean, median, and standard deviation
- Top 5 most frequent categorical values

This allows the results to be reviewed without re-running the program.

