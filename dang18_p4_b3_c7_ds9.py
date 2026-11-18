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


def bt_dang18_p4_b3_c7_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        noidungcauhoi = ('''Trên một hệ trục tọa độ của biểu đồ tần số tương đối ghép nhóm dạng cột biểu diễn tốc độ gió (đơn vị: $\\text{km/h}$) trong $100$ giờ quan trắc:
\\begin{itemize}
\\item Trục ngang chia thành $4$ đoạn liên tiếp có độ dài đều bằng $1,5\\text{ cm}$ ứng với $4$ nhóm: $[0; 10)$, $[10; 20)$, $[20; 30)$, $[30; 40)$.
\\item Trục đứng quy ước $1\\text{ cm}$ ứng với $10\\%%$ tần số tương đối.
\\end{itemize}
Biết rằng số giờ quan trắc thuộc $4$ nhóm trên lần lượt là $18$ giờ, $42$ giờ, $26$ giờ và $14$ giờ.\\
a) Tính chiều cao (đơn vị: $\\text{cm}$) của mỗi cột hình chữ nhật trên biểu đồ.\\
b) Tính diện tích của từng cột hình chữ nhật và tổng diện tích của cả $4$ cột trên biểu đồ. Giải thích tại sao tổng diện tích này không phụ thuộc vào cách phân chia tần số giữa các nhóm.''')

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Tần số tương đối của $4$ nhóm lần lượt là $18\\%%$; $42\\%%$; $26\\%%$; $14\\%%$. Vì $1\\text{ cm}$ ứng với $10\\%%$ nên chiều cao của $4$ cột trên biểu đồ lần lượt là:
$$h_1 = 1,8\\text{ cm}; \\quad h_2 = 4,2\\text{ cm}; \\quad h_3 = 2,6\\text{ cm}; \\quad h_4 = 1,4\\text{ cm}.$$
\\item Diện tích của từng cột hình chữ nhật (với đáy $1,5\\text{ cm}$) lần lượt là:
\\begin{itemize}
\\item $S_1 = 1,5 \\cdot 1,8 = 2,7\\text{ (cm}^2\\text{)}$;
\\item $S_2 = 1,5 \\cdot 4,2 = 6,3\\text{ (cm}^2\\text{)}$;
\\item $S_3 = 1,5 \\cdot 2,6 = 3,9\\text{ (cm}^2\\text{)}$;
\\item $S_4 = 1,5 \\cdot 1,4 = 2,1\\text{ (cm}^2\\text{)}$.
\\end{itemize}
Tổng diện tích của cả $4$ cột là: $S = 2,7 + 6,3 + 3,9 + 2,1 = 15\\text{ (cm}^2\\text{)}$.\\
Tổng diện tích này bằng $1,5 \\cdot (h_1 + h_2 + h_3 + h_4) = 1,5 \\cdot \\dfrac{f_1 + f_2 + f_3 + f_4}{10} = 1,5 \\cdot 10 = 15\\text{ (cm}^2\\text{)}$, luôn không đổi do tổng các tần số tương đối luôn bằng $100\\%%$.
\\end{enumEX}''')

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
