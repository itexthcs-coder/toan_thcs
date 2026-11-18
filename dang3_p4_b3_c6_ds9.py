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


def bt_dang3_p4_b3_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        c_val = randint(1, 5)
        delta_val = 4*c_val + 1
        m_ans = randint(1, 3)
        
        k_val = (2*m_ans + 1)*(m_ans**2 + m_ans + 3*c_val + 1)
        a_q = 2
        b_q = 3 + 2*m_ans
        c_q = (6*c_val + 3) + b_q*m_ans
        const_pt = 3*c_val + 1 - k_val
        str_const_pt = "+ %s" % latex(const_pt) if const_pt >= 0 else "- %s" % latex(abs(const_pt))
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Tìm tham số $m$ để phương trình $x^{2} - (2m + 1)x + m^{2} + m - %s = 0$ có hai nghiệm phân biệt $x_{1}, x_{2}$ sao cho $x_{1}^{3} + x_{2}^{3} = %s$.'''
                         % (latex(c_val), latex(k_val)))
        
        # Nội dung lời giải
        loigiai = ('''Ta có: $\\Delta = [-(2m + 1)]^{2} - 4 \\cdot 1 \\cdot (m^{2} + m - %s) = 4m^{2} + 4m + 1 - 4m^{2} - 4m + %s = %s > 0$ với mọi $m$. \\\\
Do đó phương trình luôn có hai nghiệm phân biệt $x_{1}, x_{2}$ với mọi $m$. \\\\
Theo định lí Viète, ta có: $\\begin{cases} x_{1} + x_{2} = 2m + 1 \\\\ x_{1}x_{2} = m^{2} + m - %s \\end{cases}$. \\\\
Ta có: $x_{1}^{3} + x_{2}^{3} = %s \\Leftrightarrow (x_{1} + x_{2})^{3} - 3x_{1}x_{2}(x_{1} + x_{2}) = %s$ \\\\
$\\Leftrightarrow (2m + 1)^{3} - 3(m^{2} + m - %s)(2m + 1) = %s$ \\\\
$\\Leftrightarrow (2m + 1)[(2m + 1)^{2} - 3(m^{2} + m - %s)] = %s$ \\\\
$\\Leftrightarrow (2m + 1)(4m^{2} + 4m + 1 - 3m^{2} - 3m + %s) = %s$ \\\\
$\\Leftrightarrow (2m + 1)(m^{2} + m + %s) = %s$ \\\\
$\\Leftrightarrow 2m^{3} + 3m^{2} + %sm %s = 0$ \\\\
$\\Leftrightarrow (m - %s)(%sm^{2} + %sm + %s) = 0$. \\\\
Vì $\\Delta_{m} = %s^{2} - 4 \\cdot %s \\cdot %s = %s < 0$ nên phương trình $%sm^{2} + %sm + %s = 0$ vô nghiệm. \\\\
Suy ra $m - %s = 0 \\Leftrightarrow m = %s$. \\\\
Vậy $m = %s$ là giá trị cần tìm.'''
                   % (latex(c_val), latex(4*c_val), latex(delta_val),
                      latex(c_val),
                      latex(k_val), latex(k_val),
                      latex(c_val), latex(k_val),
                      latex(c_val), latex(k_val),
                      latex(3*c_val), latex(k_val),
                      latex(3*c_val + 1), latex(k_val),
                      latex(6*c_val + 3), str_const_pt,
                      latex(m_ans), latex(a_q), latex(b_q), latex(c_q),
                      latex(b_q), latex(a_q), latex(c_q), latex(b_q**2 - 4*a_q*c_q), latex(a_q), latex(b_q), latex(c_q),
                      latex(m_ans), latex(m_ans),
                      latex(m_ans)))
    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
