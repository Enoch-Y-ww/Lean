import pytest
import yaml

'''
 @auther: YangWei
 @date： 2023/1/2
 @description： 
'''

def funadd(x,y):
    return x + y

class TestFun:
    # @pytest.mark.parametrize('anum,bnum,cnum',[
    #     (10,20,30),
    #     (20,30,50),
    #     (18,21,33)
    # ])
    @pytest.mark.parametrize(["anum", "bnum","cnum"], yaml.safe_load(open("./data.yaml")))
    def test_aNum(self, anum, bnum, cnum):
        assert funadd(anum, bnum) == cnum



