-- Switch to the alx_book_store database
USE alx_book_store;

-- Get full description of the 'books' table
SELECT 
    COLUMN_NAME AS 'Column Name',
    COLUMN_TYPE AS 'Data Type',
    IS_NULLABLE AS 'Nullable',
    COLUMN_KEY AS 'Key',
    COLUMN_DEFAULT AS 'Default Value',
    EXTRA AS 'Extra Info'
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'books'
ORDER BY ORDINAL_POSITION;
