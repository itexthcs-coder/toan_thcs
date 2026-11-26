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
def bt_dang19_p4_b3_c6_ds8(self):
    # Dạng 19: Bài toán Hóa học / Nông nghiệp – Pha trộn dung dịch dinh dưỡng
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo = [
            (40, 10, 50, '0,4x', '0,2x', '0,6x', '1,2x', 5, 6),
            (30, 10, 40, '0,3x', '0,2x', '0,5x', '1,25x', 4, 5),
            (60, 20, 80, '0,6x', '0,4x', 'x', '1,25x', 8, 10),
            (20, 30, 50, '0,2x', '0,6x', '0,8x', '1,6x', 5, 8)
        ]
        v1, v2, v_tong, m1_str, m2_str, m_tong_str, nd_moi_str, x_val, nd_so = random.choice(bo)
        
        noidungcauhoi = ('Để chăm sóc cây trồng thủy canh, người ta pha $%s$ lít dung dịch dinh dưỡng có nồng độ khoáng chất là $x\\%%$ ($x > 0$). Sau đó, người ta đổ thêm $%s$ lít dung dịch cùng loại có nồng độ khoáng chất là $2x\\%%$ vào bể chứa.\\'
                         'a) Viết biểu thức biểu thị tổng lượng khoáng chất nguyên chất (tính theo lít) có trong bể sau khi pha trộn.\\'
                         'b) Viết phân thức biểu thị nồng độ phần trăm khoáng chất của dung dịch mới sau khi pha trộn và tính nồng độ đó khi $x = %s$.'
                         % (v1, v2, x_val))
        
        loigiai = ('\\begin{enumEX}[a)]{1} \n'
                   '\\item Lượng khoáng chất nguyên chất có trong $%s$ lít dung dịch đầu là $\\dfrac{%sx}{100} = %s$ (lít).\\'
                   'Lượng khoáng chất nguyên chất có trong $%s$ lít dung dịch đổ thêm là $\\dfrac{%s \\cdot 2x}{100} = %s$ (lít).\\'
                   'Tổng lượng khoáng chất nguyên chất có trong bể sau khi pha trộn là:\\'
                   '$$%s + %s = %s\\text{ (lít)}.$$\n'
                   '\\item Tổng thể tích dung dịch sau khi pha trộn là $%s + %s = %s$ (lít).\\'
                   'Nồng độ phần trăm khoáng chất của dung dịch mới là:\\'
                   '$$C = \\dfrac{%s}{%s} \\cdot 100\\%% = %s\\%%.$$\\'
                   'Khi $x = %s$, nồng độ phần trăm khoáng chất của dung dịch mới là $%s\\%%$.\n'
                   '\\end{enumEX} \n'
                   % (v1, v1, m1_str, v2, v2, m2_str, m1_str, m2_str, m_tong_str,
                      v1, v2, v_tong, m_tong_str, v_tong, nd_moi_str, x_val, nd_so))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
