
from pytest_cases import parametrize_with_cases
def data_r():
    return "r"
def data_p():
    return "p"



def user_h():
    return "h"

@parametrize_with_cases("data",cases='.',prefix="data_")
@parametrize_with_cases("user",cases='.',prefix="user_")
def test_check(data,user):
    assert data in ("r","p")
    assert user =="h"
