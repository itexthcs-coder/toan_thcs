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


def bt_dang10_p4_b3_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        while True:
            S_val = randint(3, 8)
            P_val = randint(1, 6)
            if S_val**2 - 4*P_val > 0:
                break
        k_val = randint(2, 4)
        h_val = randint(1, 5)
        S_new = k_val*S_val + 2*h_val
        P_new = (k_val**2)*P_val + k_val*h_val*S_val + h_val**2
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Biết phương trình bậc hai $x^{2} - %sx + %s = 0$ có hai nghiệm là $x_{1}$ và $x_{2}$. Không giải phương trình, hãy lập một phương trình bậc hai ẩn $y$ có các hệ số nguyên nhận $y_{1} = %sx_{1} + %s$ và $y_{2} = %sx_{2} + %s$ làm nghiệm.'''
                         % (latex(S_val), latex(P_val), latex(k_val), latex(h_val), latex(k_val), latex(h_val)))
        
        # Nội dung lời giải
        loigiai = ('''Xét phương trình $x^{2} - %sx + %s = 0$ có $\\Delta = (-%s)^{2} - 4 \\cdot 1 \\cdot %s = %s > 0$ nên phương trình có hai nghiệm phân biệt $x_{1}, x_{2}$. \\\\
Theo định lí Viète, ta có: $\\begin{cases} x_{1} + x_{2} = %s \\\\ x_{1}x_{2} = %s \\end{cases}$. \\\\
Tính tổng và tích của $y_{1}$ và $y_{2}$: \\\\
$S = y_{1} + y_{2} = (%sx_{1} + %s) + (%sx_{2} + %s) = %s(x_{1} + x_{2}) + %s = %s \\cdot %s + %s = %s$. \\\\
$P = y_{1}y_{2} = (%sx_{1} + %s)(%sx_{2} + %s) = %sx_{1}x_{2} + %s(x_{1} + x_{2}) + %s = %s \\cdot %s + %s \\cdot %s + %s = %s$. \\\\
Vì $S^{2} - 4P = %s^{2} - 4 \\cdot %s = %s > 0$ nên $y_{1}, y_{2}$ là hai nghiệm của phương trình bậc hai: \\\\
$y^{2} - %sy + %s = 0$.'''
                   % (latex(S_val), latex(P_val), latex(S_val), latex(P_val), latex(S_val**2 - 4*P_val),
                      latex(S_val), latex(P_val),
                      latex(k_val), latex(h_val), latex(k_val), latex(h_val), latex(k_val), latex(2*h_val), latex(k_val), latex(S_val), latex(2*h_val), latex(S_new),
                      latex(k_val), latex(h_val), latex(k_val), latex(h_val), latex(k_val**2), latex(k_val*h_val), latex(h_val**2), latex(k_val**2), latex(P_val), latex(k_val*h_val), latex(S_val), latex(h_val**2), latex(P_new),
                      latex(S_new), latex(P_new), latex(S_new**2 - 4*P_new),
                      latex(S_new), latex(P_new)))
    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
