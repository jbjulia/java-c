# JavaC
Automatic Java File Conversion

Requirements: Python 3
How to Run: python3 javac.py


JavaC is a small Python utility that allows you to select multiple Java (.java) files and convert them into Class
Class (.class) files. 
![Alt text](/resources/images/GUI.png)
Selected files are added to a QListWidget, where they can then be converted in bulk.
![Alt text](/resources/images/FileSelection.png)
Once complete, successfully compiled Class files will appear in the same directory the Java files were selected from.
If errors occur, the conversion will halt and no files will be converted.
![Alt text](/resources/images/FileConversion.png)