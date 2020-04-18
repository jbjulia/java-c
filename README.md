# JavaC
_Automatic Java File Conversion_

**Requirements:** _Python 3, PyQt5, javac_  
**How to Run:** _python3 javac.py_  
  
  
JavaC is a small Python utility that allows you to select multiple Java  
(.java) files and convert them into Class (.class) files.  
  
![Alt text](/resources/images/GUI.png)  
  
Selected files are added to a QListWidget, where they can then be  
converted to Class files in bulk.  
  
![Alt text](/resources/images/FileSelection.png)  
  
Once complete, successfully compiled Class files will appear in the  
same directory the Java files were selected from. If errors occur, the  
conversion will halt and no files will be converted.  
  
![Alt text](/resources/images/FileConversion.png)