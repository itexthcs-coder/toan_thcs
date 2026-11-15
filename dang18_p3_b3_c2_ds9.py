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


def bt_dang18_p3_b3_c2_ds9(self):
    x = symbols('x')
    so_kwh_du_kien = randint(65, 100)
    ngan_sach_dong = 50 * 1800 + (so_kwh_du_kien - 50) * 2100 + randint(500, 1900)
    ngan_sach_nghin = ngan_sach_dong / 1000
    
    x_max_val = 50 + (ngan_sach_nghin - 90) / 2.1
    ans = math.floor(x_max_val)
    kq_str = str(ans)
    ns_str = str(ngan_sach_nghin).replace('.', ',')
    
    noidungcauhoi = ('''Giá bán lẻ điện sinh hoạt quy định cho $50\\text{ kWh}$ đầu tiên là $1\\,800$ đồng/kWh và từ kWh thứ $51$ đến $100$ tính giá $2\\,100$ đồng/kWh. Nếu một hộ gia đình dự trù ngân sách tiền điện tháng này không vượt quá $%s$ nghìn đồng thì gia đình đó sử dụng được tối đa bao nhiêu kWh điện (làm tròn xuống hàng đơn vị)?'''
                     % (ns_str))
    
    loigiai = ('''Gọi $x$ ($x > 50$, đơn vị: kWh) là lượng điện tiêu thụ của hộ gia đình. \\
               Số tiền phải trả cho $50\\text{ kWh}$ đầu là $50 \\cdot 1,8 = 90$ (nghìn đồng). \\
               Số tiền phải trả cho $(x - 50)\\text{ kWh}$ tiếp theo là $2,1(x - 50)$ (nghìn đồng). \\
               Theo đề bài, ta có bất phương trình: \\
               $90 + 2,1(x - 50) \\le %s \\Leftrightarrow 2,1(x - 50) \\le %s \\Leftrightarrow x - 50 \\le %.2f \\Leftrightarrow x \\le %.2f$. \\
               Vậy gia đình đó sử dụng được tối đa $%s\\text{ kWh}$ điện.'''
               % (ns_str,
                  str(round(ngan_sach_nghin - 90, 3)).replace('.', ','), (ngan_sach_nghin - 90) / 2.1, x_max_val,
                  kq_str))
    
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
        '\\loigiai{ \n' + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage}\n\n')
    return content
