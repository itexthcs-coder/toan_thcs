import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D


def bt_dang14_p2_b1_c8_ds9(self):
    ans = 16
    noidungcauhoi = ("""Ở một loài thực vật, xét hai cặp gene phân li độc lập quy định hai tính trạng khác nhau: cặp gene thứ nhất có $2$ allele $A, a$; cặp gene thứ hai có $2$ allele $B, b$. Thực hiện phép thử cho lai giữa cây bố có kiểu gene $(Aa, Bb)$ với cây mẹ có kiểu gene $(Aa, Bb)$. Cây con nhận ngẫu nhiên $1$ gene từ bố và $1$ gene từ mẹ ở mỗi cặp.""" % ())
    # Ý 1
    st_1_d = '\\True ' + ('Ở cặp tính trạng thứ nhất, không gian mẫu về tổ hợp gene nhận từ bố và mẹ có $4$ kết quả là $AA; Aa; aA; aa$')
    st_1_s = ('Ở cặp tính trạng thứ nhất, không gian mẫu về tổ hợp gene nhận từ bố và mẹ chỉ có $3$ kết quả là $AA; Aa; aa$')
    sol_1_d = ('Đúng. Xét theo nguồn gốc giao tử (bố trước, mẹ sau), $Aa$ (bố cho $A$, mẹ cho $a$) và $aA$ (bố cho $a$, mẹ cho $A$) là hai kết quả phân biệt.')
    sol_1_s = ('Sai. Trong phép thử lai tạo, kết quả $Aa$ và $aA$ có nguồn gốc giao tử khác nhau nên là $4$ phần tử.')
    pair_1 = [(st_1_d, sol_1_d), (st_1_s, sol_1_s)]
    # Ý 2
    st_2_d = '\\True ' + ('Không gian mẫu của phép lai hai tính trạng trên có tất cả $16$ phần tử')
    st_2_s = ('Không gian mẫu của phép lai hai tính trạng trên có tất cả $9$ phần tử')
    sol_2_d = ('Đúng. Cặp gene thứ nhất có $4$ tổ hợp và cặp gene thứ hai có $4$ tổ hợp nên không gian mẫu có $4 \\cdot 4 = 16$ phần tử.')
    sol_2_s = ('Sai. Lập bảng hai chiều $4 \\times 4$, không gian mẫu có $4 \\cdot 4 = 16$ phần tử.')
    pair_2 = [(st_2_d, sol_2_d), (st_2_s, sol_2_s)]
    # Ý 3
    st_3_d = '\\True ' + ('Số kết quả trong không gian mẫu mà cây con có kiểu gene đồng hợp lặn ở cả hai cặp tính trạng $(aa, bb)$ là $1$')
    st_3_s = ('Số kết quả trong không gian mẫu mà cây con có kiểu gene đồng hợp lặn ở cả hai cặp tính trạng $(aa, bb)$ là $4$')
    sol_3_d = ('Đúng. Cây con chỉ có $(aa, bb)$ khi cả bố và mẹ đều truyền giao tử $a$ và $b$, nên chỉ có duy nhất $1$ kết quả.')
    sol_3_s = ('Sai. Chỉ có $1$ kết quả duy nhất tạo ra $(aa, bb)$.')
    pair_3 = [(st_3_d, sol_3_d), (st_3_s, sol_3_s)]
    # Ý 4
    st_4_d = '\\True ' + ('Số kết quả trong không gian mẫu mà cây con mang ít nhất một allele trội $A$ ở cặp thứ nhất là $12$')
    st_4_s = ('Số kết quả trong không gian mẫu mà cây con mang ít nhất một allele trội $A$ ở cặp thứ nhất là $8$')
    sol_4_d = ('Đúng. Có $3$ tổ hợp ở cặp thứ nhất chứa $A$ ($AA; Aa; aA$) kết hợp với $4$ tổ hợp ở cặp thứ hai nên có $3 \\cdot 4 = 12$ kết quả.')
    sol_4_s = ('Sai. Số kết quả chứa ít nhất một allele trội $A$ là $3 \\cdot 4 = 12$.')
    pair_4 = [(st_4_d, sol_4_d), (st_4_s, sol_4_s)]

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        c1 = random.choice(pair_1)
        c2 = random.choice(pair_2)
        c3 = random.choice(pair_3)
        c4 = random.choice(pair_4)
        answers = [c1[0], c2[0], c3[0], c4[0]]
        if 1 <= count_true_answers(answers) <= 3:
            break

    shuffled_answers_nb = [c1[0]]
    shuffled_solutions_nb = [c1[1]]
    shuffled_answers_th = [c2[0]]
    shuffled_solutions_th = [c2[1]]
    shuffled_answers_vd = [c3[0]]
    shuffled_solutions_vd = [c3[1]]
    shuffled_answers_vdc = [c4[0]]
    shuffled_solutions_vdc = [c4[1]]

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
               '{' + str(shuffled_answers_nb[0]) + '}\n' +
               '{' + str(shuffled_answers_th[0]) + '}\n' +
               '{' + str(shuffled_answers_vd[0]) + '}\n' +
               '{' + str(shuffled_answers_vdc[0]) + '}\n' +
               '\\loigiai{ \n' +
               '\\begin{enumEX}[a)]{1} \n' +
               '\\item ' + str(shuffled_solutions_nb[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_th[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_vd[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_vdc[0]) + '\n' +
               '\\end{enumEX}} \n' +
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
