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
### CÔNG CỤ
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


def bt_dang17_p4_b1_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        cases = [(Decimal('3.2'), 4, Rational(-1, 5), 1, 3, Decimal('1.8'), Decimal('1.4'), Decimal('1.2')),
                 (Decimal('4.5'), 6, Rational(-1, 8), 2, 4, Decimal('2.0'), Decimal('2.5'), Decimal('2.0')),
                 (Decimal('5.0'), 5, Rational(-1, 5), 1, 4, Decimal('3.2'), Decimal('1.8'), Decimal('1.5'))]
        h_max, x_land, a_par, d_from_land, x_tree, y_tree_abs, h_water, h_tree = random.choice(cases)
        
        h_max_str = str(h_max).replace('.', ',')
        y_tree_str = str(y_tree_abs).replace('.', ',')
        h_water_str = str(h_water).replace('.', ',')
        h_tree_str = str(h_tree).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một vòi phun nước đặt trên mặt đất phun tia nước theo quỹ đạo là một cung parabol. Chọn hệ trục tọa độ $Oxy$ sao cho đỉnh cao nhất của tia nước là gốc tọa độ $O(0; 0)$, trục $Oy$ hướng thẳng đứng lên trên và trục $Ox$ nằm ngang. Biết tia nước đạt độ cao tối đa là $%s$ m so với mặt đất và rơi chạm đất ở vị trí cách hình chiếu của đỉnh cao nhất một khoảng theo phương ngang là $%s$ m. \\\\
a) Viết phương trình parabol $y = ax^2$ biểu diễn quỹ đạo tia nước. \\\\
b) Một cây cảnh cao $%s$ m được trồng cách vị trí tia nước chạm đất $%s$ m (nằm phía trong vùng tưới). Hỏi tia nước có phun vượt qua ngọn cây này hay không? Giải thích.'''
                         %(h_max_str, latex(x_land), h_tree_str, latex(d_from_land)
                         ))
        
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Với hệ trục tọa độ $Oxy$ đã chọn, mặt đất nằm ngang phía dưới gốc tọa độ $O(0; 0)$ một khoảng $%s$ m. \\\\
Vị trí tia nước rơi chạm đất nằm bên phải trục $Oy$ nên có tọa độ là $B(%s; -%s)$. \\\\
Thay $x = %s$ và $y = -%s$ vào phương trình $y = ax^2$, ta được: \\\\
$-%s = a \\cdot %s^2 \\Rightarrow %sa = -%s \\Rightarrow a = %s$. \\\\
Vậy phương trình parabol biểu diễn quỹ đạo tia nước là $y = %sx^2$.
\\item Vị trí trồng cây nằm phía trong vùng tưới và cách điểm chạm đất $B$ một khoảng $%s$ m nên khoảng cách từ cây đến trục tung $Oy$ là $x = %s - %s = %s$ (m). \\\\
Thay $x = %s$ vào phương trình $y = %sx^2$, ta được: \\\\
$y = %s \\cdot %s^2 = -%s$ (m). \\\\
Suy ra độ cao của tia nước so với mặt đất tại vị trí trồng cây là: \\\\
$%s - %s = %s$ (m). \\\\
Vì $%s > %s$ nên tia nước phun vượt qua ngọn cây cảnh này.
\\end{enumEX}'''
                   %(h_max_str,
                     latex(x_land), h_max_str,
                     latex(x_land), h_max_str,
                     h_max_str, latex(x_land), latex(x_land**2), h_max_str, latex(a_par),
                     latex(a_par),
                     latex(d_from_land), latex(x_land), latex(d_from_land), latex(x_tree),
                     latex(x_tree), latex(a_par),
                     latex(a_par), latex(x_tree), y_tree_str,
                     h_max_str, y_tree_str, h_water_str,
                     h_water_str, h_tree_str
                   ))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
