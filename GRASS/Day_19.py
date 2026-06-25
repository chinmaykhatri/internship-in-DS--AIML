""" What is matplotlib?
    -> Matplotlib is a Python library used for creating static, animated, and interactive plots.
    -> Data visualization: It's the graphical representation of data to identify patterns, trends, and insights
"""
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

# line graph
# x = [2010,2015,2020,2025]
# y = [100,200,250,300]
# plt.plot(x,y) # line graph
# plt.show() # graph show
# plt.xlabel("years") # x label
# plt.ylabel("sales report") # y label
# plt.title("sales report") # graph title 
# plt.show()

# graph size
# x = [2010,2015,2020,2025]
# y = [100,200,250,300]
# plt.figure(figsize=(6,2))
# plt.plot(x,y)
# plt.show()

x = [2010,2015,2020,2025] # x cord
y = [100,200,250,300] # y cord.
 
""" **Markers**
 
    |character      |  |  |description |
    |-------------|  -------------------------------|
    |'.'       | | |point marker|
    |','       | | |pixel marker|
    |'o'       | | |circle marker|
    |'v'       | | |triangle_down marker|
    |'^'       | | |triangle_up marker|
    |'<'       | | |triangle_left marker|
    |'>'       | | |triangle_right marker|
    |'1'       | | |tri_down marker|
    |'2'       | | |tri_up marker|
    |'3'       | | |tri_left marker|
    |'4'       | | |tri_right marker|
    |'8'       | | |octagon marker|
    |'s'       | | |square marker|
    |'p'       | | |pentagon marker|
    |'P'       | | |plus (filled) marker|
    |'*'       | | |star marker|
    |'h'       | | |hexagon1 marker|
    |'H'       | | |hexagon2 marker|
    |'+'       | | |plus marker|
    |'x'       | | |x marker|
    |'X'       | | |x (filled) marker|
    |'D'       | | |diamond marker|
    |'d'       | | |thin_diamond marker|
    |'|'       | | |vline marker|
    |'_'       | | |hline marker|
 


-----**Line Styles**-------
    
    |character      |  |  |  |description |
    |-------------|   -------------------------------|
    |'-'       | | | |solid line style|
    |'--'      | | | |dashed line style|
    |'-.'      | | | |dash-dot line style|
    |':'       | | | |dotted line style|
    
Example format strings:
 
    'b'    # blue markers with default shape
    'or'   # red circles
    '-g'   # green solid line
    '--'   # dashed line with default color
    '^k:'  # black triangle_up markers connected by a dotted line


    
-------**Colors**-----
 
    |character      |  |  |  |color |
    |-------------|   -------------------------------|
    |'b'       | | | |blue|
    |'g'       | | | |green|
    |'r'       | | | |red|
    |'c'       | | | |cyan|
    |'m'       | | | |magenta|
    |'y'       | | | |yellow|
    |'k'       | | | |black|
    |'w'       | | | |white|
"""
# graph size
# plt.figure(figsize=(6,2)) # width or height
# plt.plot(x,y,color="y",marker='*',linestyle=":",linewidth=4,markersize=14,)
# plt.show()
# x = [2010,2015,2020,2025]
# y1 = [100,200,260,290]
# y2 = [150,185,195,300]

# plt.plot(x,y1,label="jeans")
# plt.plot(x,y2,label="shirt")
# plt.legend() # info of label
# plt.show()

# question on multiple line chart ->
# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
# sales = [12000, 15000, 18000, 17000, 22000, 25000]

# plt.figure(figsize=(8, 5))

# plt.plot(
#     months,
#     sales,
#     marker='o',
#     linestyle='-',
#     linewidth=2,
#     label='Sales'
# )

# plt.title("Monthly Sales Trend")
# plt.xlabel("Month")
# plt.ylabel("Sales (₹)")
# plt.grid(True)
# plt.legend()
# plt.show()

# example 2
# months = ["Jan","Feb","Mar","Apr","May","Jun"]

# product_A = [100,120,140,160,180,200]
# product_B = [90,110,130,150,170,210]

# plt.figure(figsize=(9,5))

# plt.plot(
#     months,
#     product_A,
#     marker='o',
#     linewidth=2,
#     label='Product A'
# )

# plt.plot(
#     months,
#     product_B,
#     marker='s',
#     linewidth=2,
#     label='Product B'
# )

# plt.title("Sales Comparison")
# plt.xlabel("Month")
# plt.ylabel("Units Sold")

# plt.grid(True)
# plt.legend()

# plt.show()

# bar chart
# x = [2015,2020,2025,2030]
# y = [100,150,200,290]

# size
# plt.figure(figsize=(6,2)) #
# plt.bar(x,y)
# plt.show()

# multi bar chart -> using numpy 
# x = np.array([1,2,3,4])
# y1 = [10,20,20,40]
# y2 = [20,30,25,30]
# calculation -> width
# w = 0.40
# plt.bar(x - w/2,y1 , label="boys",width=w) # hide second
# plt.bar(x + w/2,y2, label="girls",width=w) # show

# plt.xlabel("groups")
# plt.ylabel("number of students")
# plt.title("Number of Students in Each group")
# plt.legend()
# plt.show()  

# multi bar chart -> without using numpy 
# import matplotlib.pyplot as plt

# groups = ['group A','group B','group C','group D']

# y1 = [10,20,20,40]
# y2 = [20,30,25,30]

# x = [0,1,2,3]
# w = 0.4

# plt.bar(
#     [i-w/2 for i in x],
#     y1,
#     width=w,
#     label='Boys'
# )

# plt.bar(
#     [i+w/2 for i in x],
#     y2,
#     width=w,
#     label='Girls'
# )

# plt.xticks(x, groups)

# plt.xlabel("Groups")
# plt.ylabel("Number of Students")
# plt.title("Number of Students in Each Group")

# plt.legend()
# plt.show()+A