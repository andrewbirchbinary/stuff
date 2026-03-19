UPDATE InventItemBarcode
SET barcodeSetupId = CASE
    WHEN LEN(itemBarCode) = 13 AND itemBarCode LIKE '2%' THEN 'FRG-EAN'
    WHEN LEN(itemBarCode) = 11                           THEN 'FRG-PC'
    ELSE                                                      'ANY'
END
WHERE barcodeSetupId != CASE
    WHEN LEN(itemBarCode) = 13 AND itemBarCode LIKE '2%' THEN 'FRG-EAN'
    WHEN LEN(itemBarCode) = 11                           THEN 'FRG-PC'
    ELSE                                                      'ANY'
END
   OR barcodeSetupId IS NULL;
