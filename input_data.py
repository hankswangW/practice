
def read_days(id: str, seq: int, ratio: float) -> list:
    """
    按照要求读取日线的数据。

    Args:
        id:  预测疫苗的id 
        seq: 长度
        ratio: 比值，如果在这个比值内就是标签 1，否则 0

    Return:
        一个二维数组，每一行最后一位是标签。  
        [
            [12,22,21,0],
            [12,22,21,1],
        ]

    """
    pass 

def read_month(id: str, seq: int, ratio: float) -> list:
    """
    按照要求读取月线的数据。

    Args:
        id:  预测疫苗的id 
        seq: 长度
        ratio: 比值，如果在这个比值内就是标签 1，否则 0

    Return:
        一个二维数组，每一行最后一位是标签。  
        [
            [12,22,21,0],
            [12,22,21,1],
        ]

    """
    pass 

def read_days_for_analysis(id: str, seq: int) -> list:
    """
    按照要求读取日线的数据。

    Args:
        id:  预测疫苗的id 
        seq:  长度

    Return:
        List:   
        [0.3,0.4]

    """
    pass 

def read_month_for_analysis(id: str, seq: int) -> list:
    """
    按照要求读取月线的数据。

    Args:
        id:  预测疫苗的id 
        seq:  长度

    Return:
        List:   
        [0.3,0.4]

    """
    pass 

