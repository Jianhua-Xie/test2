import  re

regex_lis = ['\([^()]+\)','(\d+\.?\d*)(\*|\/)(\d+\.?\d*)','(\d+\.?\d*)(\+|\-)(\d+\.?\d*)','(\+|\-){2,}']

def cal(formula):
    formula = cal_mul_div(formula)
    result_cal = cal_add_sub(formula)
    return result_cal

def dealwith(formula):
    formula = formula.replace('+-', '-')
    formula = formula.replace('--', '+')
    return formula

def cal_mul_div(formula):
    while True:
        ret = re.search(regex_lis[1],formula)
        if ret:
            ret_son = ret.group()
            if '*' in ret_son:
                a, b = ret_son.split('*')
                res_ret = str(float(a) * float(b))
            elif '/' in ret_son:
                a, b = ret_son.split('/')
                res_ret= str(float(a) / float(b))
            formula = formula.replace(ret_son,res_ret)
        else:
            return formula
            break

def cal_add_sub(formula):
    while True:
        formula = dealwith(formula)
        ret = re.search(regex_lis[2],formula)
        if ret:
            ret_son = ret.group()
            if '+' in ret_son:
                a, b = ret_son.split('+')
                res_ret = str(float(a) + float(b))
            elif '-' in ret_son:
                a, b = ret_son.split('-')
                res_ret= str(float(a) - float(b))
            formula = formula.replace(ret_son,res_ret)
        else:
            return formula
            break


def remove_bracket(formula):
    while 1:
        # 匹配（）
        ret = re.search(regex_lis[0], formula)
        if ret:
            #提取（）里的算式
            ret_son = ret.group()
            ret_formula = ret_son.strip('()')
            res = cal(ret_formula)
            #返回结果替换括号
            formula = formula.replace(ret_son,res)
        else:
            return formula
            break

def main():
    while 1:
        exp = input('>>>').strip()
        exp = exp.replace(" ",'')   #去空格
        print(exp)
        exp = remove_bracket(exp)
        res = cal(exp)
        print(res)

main()

