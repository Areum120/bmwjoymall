import win32com.client as win32


def converToxlsx(fname):
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    wb = excel.Workbooks.Open(fname)

    wb.SaveAs(fname+'x', FileFormat = 51)
    wb.Close()
    excel.Application.Quit()

converToxlsx('C:\\Users\\웍스컴바인\\Desktop\\work\\BMWJoymall\\product_classification\\sendRequest.xls')