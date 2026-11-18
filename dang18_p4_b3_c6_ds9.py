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


def bt_dang18_p4_b3_c6_ds9(self):
    def fmt_vn(val):
        s = str(val).rstrip('0').rstrip('.') if '.' in str(val) else str(val)
        return s.replace('.', ',')

    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        von_ao = randint(8, 15)
        von_quan = randint(von_ao + 3, 25)
        S_von = von_ao + von_quan
        P_von = von_ao * von_quan
        lai_ao_pt = randint(15, 25)
        lai_quan_pt = randint(20, 35)
        
        tien_lai = (Decimal(von_ao) * Decimal(lai_ao_pt) + Decimal(von_quan) * Decimal(lai_quan_pt)) / Decimal(100)
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một cửa hàng nhập về hai lô hàng gồm áo sơ mi và quần âu với tổng số vốn ban đầu là $%s$ triệu đồng. Sau khi bán hết, lô áo sơ mi mang lại lợi nhuận $%s\\%%$, lô quần âu mang lại lợi nhuận $%s\\%%$. Biết rằng tích số tiền vốn (tính theo đơn vị triệu đồng) của hai lô hàng là $%s$ và vốn nhập quần âu nhiều hơn vốn nhập áo sơ mi. Tính tổng số tiền lãi cửa hàng thu được.'''
                         % (latex(S_von), latex(lai_ao_pt), latex(lai_quan_pt), latex(P_von)))
        
        # Nội dung lời giải
        loigiai = ('''Gọi số tiền vốn nhập lô áo sơ mi và lô quần âu lần lượt là $x_{1}$ (triệu đồng) và $x_{2}$ (triệu đồng) (điều kiện: $x_{2} > x_{1} > 0$). \\\\
Theo đề bài, tổng số vốn là $%s$ triệu đồng và tích hai số vốn là $%s$ nên ta có: \\\\
$\\begin{cases} x_{1} + x_{2} = %s \\\\ x_{1}x_{2} = %s \\end{cases}$. \\\\
Do đó, $x_{1}$ và $x_{2}$ là hai nghiệm của phương trình bậc hai: $x^{2} - %sx + %s = 0$. \\\\
Ta có: $\\Delta = (-%s)^{2} - 4 \\cdot 1 \\cdot %s = %s > 0 \\Rightarrow \\sqrt{\\Delta} = %s$. \\\\
Phương trình có hai nghiệm phân biệt là $x_{1} = %s$ và $x_{2} = %s$. \\\\
Vì $x_{2} > x_{1} > 0$ nên vốn nhập áo sơ mi là $%s$ triệu đồng và vốn nhập quần âu là $%s$ triệu đồng. \\\\
Tổng số tiền lãi cửa hàng thu được là: \\\\
$%s \\cdot %s\\%% + %s \\cdot %s\\%% = %s$ (triệu đồng).'''
                   % (latex(S_von), latex(P_von),
                      latex(S_von), latex(P_von),
                      latex(S_von), latex(P_von),
                      latex(S_von), latex(P_von), latex((von_quan - von_ao)**2), latex(von_quan - von_ao),
                      latex(von_ao), latex(von_quan),
                      latex(von_ao), latex(von_quan),
                      latex(von_ao), latex(lai_ao_pt), latex(von_quan), latex(lai_quan_pt), fmt_vn(tien_lai)))
    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
