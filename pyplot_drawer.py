# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 22:11:49 2019

@author: zhouyu
"""

import numpy as np

from matplotlib import pyplot as plt
import argparse

def draw_whole():
    # create an empty figure 
    #fig = plt.figure() 
    # or very full filled figure
    fig = plt.figure(num=1, figsize=[6,6], 
                     facecolor='plum', edgecolor='seagreen',
                     title="my figure")
    # create a plot in the figure
    pic = fig.add_subplot(1,1,1)
    
    pic.plot(1,1,'*')
    

    plt.show()
    return

###############################################################################

def line_partition(x=[1, 2, 3, 4, 5],
                   y_list = [[4, 3, 4, 3, 2],
                             [6, 4, 3, 5, 4],
                             [5, 8, 8, 7, 9]],
                   labels=["same ", "similar", "new"],
                   colors = ["blue","orange","green"],
                   x_ticks = ["2015","2016","2017","2018","2019"],
                   title = "LDA", file=None, ylabel=None, legend=False):
    avg_x = [x[-1]+0.03,x[-1]+0.23]
    avg_y = [[sum(y)/len(y)]*2 for y in y_list]
    fig, ax = plt.subplots()
    if ylabel is not None:
        plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(x,x_ticks)
    ax.stackplot(x, np.vstack(y_list), labels=labels, colors=colors)
    if legend:
        ax.legend(loc='upper right')
    ax.stackplot(avg_x, np.vstack(avg_y), labels=labels, colors=colors)
    height = 0.0
    for a_y in avg_y:
        cur_h = a_y[0]
        ax.text(sum(avg_x)/len(avg_x), height+cur_h/2, str(cur_h))
        height += cur_h
        
    if file is None:
        plt.show()
    else:
        plt.savefig(file)

    return

def scatter_line(x=[1,2,3,4,5],
                 y_list = [[4, 3, 4, 3, 2],
                           [6, 4, 3, 5, 4],
                           [5, 8, 8, 7, 9]],
                 lineStyles = ['go-','rs','--'],
                 labels = ['lab1', 'lab2', 'lab3'],
                 title = "LDA", file=None, ylabel=None, legend=True):
    fig = plt.figure()
    pic = fig.add_subplot(111)
    pic.set_xlim(0.5, 6)
    for y, line_style, label in zip(y_list,lineStyles,labels):
        pic.plot(x,y,line_style,label)
    if legend:
        pic.legend(loc='upper right')
    if file is None:
        plt.show()
    else:
        plt.savefig(file)
    return

if __name__ == "__main__":
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument('-whole', default=True, action='store_true')
    parser.add_argument('-no_lp', '--line_partition', default=True, action='store_true')
    parser.add_argument('-no_sl', '--scatter_line', default=True, action='store_true')
    
    parser.add_argument('-lp_f', '--line_partition_file', default="lp_f.png")
    parser.add_argument('-sl_f', '--scatter_line_file', default="sl_f.png")
    args = parser.parse_args()

    if args.whole:
        draw_whole()
        #exit()

    if not args.line_partition:
        line_partition(file=args.line_partition_file)
    if not args.scatter_line:
        scatter_line(file=args.scatter_line_file)