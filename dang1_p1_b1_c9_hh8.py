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
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
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
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
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
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang1_p1_b1_c9_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        k_val = random.choice([2, 3, 4, 5])
        cau_hoi_kieu = random.choice(['tim_sai', 'tim_dung'])
        if cau_hoi_kieu == 'tim_sai':
            da = 'Hai tam giác đồng dạng với nhau thì luôn bằng nhau'
            s = [
                'Hai tam giác bằng nhau thì đồng dạng với nhau theo tỉ số đồng dạng $k = 1$',
                'Mọi tam giác đều đồng dạng với chính nó',
                'Nếu $\\Delta A\'B\'C\' \\backsim \\Delta ABC$ với tỉ số đồng dạng $k = %s$ thì $\\Delta ABC \\backsim \\Delta A\'B\'C\'$ với tỉ số đồng dạng $\\frac{1}{%s}$' % (k_val, k_val),
                'Hai tam giác có các góc tương ứng bằng nhau và các cạnh tương ứng tỉ lệ thì đồng dạng với nhau'
            ]
            das1, das2, das3 = random.sample(s, 3)
            noidungcauhoi = ('Khẳng định nào sau đây là \\textbf{sai}?')
            loigiai = ('Theo định nghĩa và tính chất của hai tam giác đồng dạng:\\\\ '
                       '- Hai tam giác bằng nhau thì đồng dạng với nhau theo tỉ số đồng dạng $k = 1$.\\\\ '
                       '- Mọi tam giác đều đồng dạng với chính nó.\\\\ '
                       '- Nếu $\\Delta A\'B\'C\' \\backsim \\Delta ABC$ với tỉ số $k = %s$ thì $\\Delta ABC \\backsim \\Delta A\'B\'C\'$ với tỉ số $\\frac{1}{%s}$.\\\\ '
                       '- Hai tam giác đồng dạng chỉ bằng nhau khi tỉ số đồng dạng $k = 1$, do đó khẳng định hai tam giác đồng dạng luôn bằng nhau là sai.'
                       % (k_val, k_val))
        else:
            da = 'Hai tam giác bằng nhau thì đồng dạng với nhau theo tỉ số đồng dạng $k = 1$'
            s = [
                'Hai tam giác đồng dạng với nhau thì luôn bằng nhau',
                'Hai tam giác vuông bất kì luôn đồng dạng với nhau',
                'Hai tam giác cân bất kì luôn đồng dạng với nhau',
                'Nếu $\\Delta A\'B\'C\' \\backsim \\Delta ABC$ với tỉ số $k = %s$ thì $\\Delta ABC \\backsim \\Delta A\'B\'C\'$ cũng có tỉ số $k = %s$' % (k_val, k_val)
            ]
            das1, das2, das3 = random.sample(s, 3)
            noidungcauhoi = ('Khẳng định nào sau đây là \\textbf{đúng}?')
            loigiai = ('Theo nhận xét về hai tam giác đồng dạng:\\\\ '
                       '- Hai tam giác bằng nhau có các góc tương ứng bằng nhau và các cạnh tương ứng bằng nhau nên tỉ số đồng dạng là $k = 1$. Do đó hai tam giác bằng nhau thì đồng dạng với nhau theo tỉ số đồng dạng $k = 1$.\\\\ '
                       '- Các khẳng định còn lại đều sai vì tỉ số đồng dạng có thể khác $1$ hoặc các góc tương ứng chưa chắc bằng nhau.')
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
