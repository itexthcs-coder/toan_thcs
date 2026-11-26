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
def bt_dang17_p3_b3_c6_ds8(self):
    # Dạng 17: Bài toán kinh tế / chia sẻ chi phí thuê xe du lịch
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # T / (x - d) - T / x = T*d / (x*(x - d))
        bo = [
            (1200, 4, 20, 15),
            (1500, 5, 30, 10),
            (1800, 6, 30, 15),
            (2400, 4, 24, 20)
        ]
        tong_tien, bot_nguoi, x_val, kq = random.choice(bo)
        tu_so = tong_tien * bot_nguoi
        
        noidungcauhoi = ('Một nhóm học sinh gồm $x$ bạn ($x > %s$) dự định cùng nhau thuê một chiếc xe du lịch với giá $%s$ nghìn đồng và chia đều chi phí cho mỗi người. Đến ngày khởi hành có $%s$ bạn bận việc nên không tham gia được. Hỏi nếu ban đầu nhóm có $%s$ bạn thì mỗi bạn còn lại phải đóng thêm bao nhiêu nghìn đồng so với dự định?' % (bot_nguoi, tong_tien, bot_nguoi, x_val))
        
        loigiai = ('Số tiền dự định mỗi bạn phải đóng là $\\dfrac{%s}{x}$ (nghìn đồng).\\'
                   'Số tiền thực tế mỗi bạn còn lại phải đóng là $\\dfrac{%s}{x - %s}$ (nghìn đồng).\\'
                   'Phân thức biểu thị số tiền mỗi bạn còn lại phải đóng thêm là:\\'
                   '$$\\dfrac{%s}{x - %s} - \\dfrac{%s}{x} = \\dfrac{%sx - %s(x - %s)}{x(x - %s)} = \\dfrac{%s}{x(x - %s)}\\text{ (nghìn đồng)}.$$\\'
                   'Thay $x = %s$ vào biểu thức trên, số tiền mỗi bạn phải đóng thêm là $\\dfrac{%s}{%s \\cdot (%s - %s)} = %s$ (nghìn đồng).'
                   % (tong_tien, tong_tien, bot_nguoi, tong_tien, bot_nguoi, tong_tien, tong_tien, tong_tien, bot_nguoi, bot_nguoi, tu_so, bot_nguoi, x_val, tu_so, x_val, x_val, bot_nguoi, kq))
        
        dapan = '\\shortans[0]{$%s$}\n' % str(kq)
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
