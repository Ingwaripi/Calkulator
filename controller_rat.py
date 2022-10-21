
import user_interface as us
import modul_sum as ms
import modul_sub as msd
import modul_mult as mlt
import modul_div as dv
import modul_pow as pw
import modul_sqrt as sq
def rations():
    result_a = us.mode()

    if result_a == 1:
        menu =  int(input('''Options:
    1 - sum
    2 - sub
    3 - milt
    4 - div
    5 - pow
    6 - sqrt
    7 - exit
        : '''))
        if menu == 1:
            result1 = ms.sum_result()
            return result1
        if menu == 2:
            result2 = msd.sub_result()
            return result2
        if menu == 3:
            result3 = mlt.mult_result()
            return result3
        if menu == 4:
            resilt4 = dv.div_result()
            return resilt4
        if menu == 5:
            resilt5 = pw.pow_result()
            return resilt5
        if menu == 6:
            resilt6 = sq.sqrt_result()
            return resilt6
        

    elif result_a == 2:
        menu_com = int(input('''Options:
    1 - Sum
    2 - Sub
    3 - Mult
    4 - Div
    5 - Pow
    6 - Sqrt
        : '''))
        if menu_com == 1:
            result_com_sum = ms.sum_result_com()
            return result_com_sum
        if menu_com == 2:
            result_com_sub = msd.sub_result_com()
            return result_com_sub
        if menu_com == 3:
            result_com_mult = mlt.mult_result_com()
            return result_com_mult
        if menu_com == 4:
            result_com_div = dv.div_result_com()
            return result_com_div
        if menu_com == 5:
            result_com_pow = pw.pow_result_com()
            return result_com_pow
        if menu_com == 6:
            result_com_sqrt = sq.sqrt_result_com()
            return result_com_sqrt
    
        
        