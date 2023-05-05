# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 11:58:07 2022

@author: 王
"""

import order_module

appetizer = order_module.order_appetizer()
soup = order_module.order_soup()
main = order_module.order_main()
dessert = order_module.order_dessert()
print()

msg = "你點的菜單為 開胃菜：{}，湯品：{}，主菜：{}，甜點：{}"

print(msg.format(appetizer, soup, main, dessert))