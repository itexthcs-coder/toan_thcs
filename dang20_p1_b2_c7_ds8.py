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


def bt_dang20_p1_b2_c7_ds8(self):
    # Dạng 20: Phát hiện lỗi sai khi chia hai vế của phương trình cho nhân tử chứa ẩn
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        a = random.choice([1, 2, 3, 4])
        b = random.choice([2, 3, 4, 5])
        c = random.choice([1, 2, 3])
        # Phương trình: (x - a)(x + b) = (x - a)(2x - c) -> nghiệm mất là x = a, nghiệm tìm được là x = b + c
        nghiem_con = b + c
        
        noidungcauhoi = "Khi giải phương trình $(x - %s)(x + %s) = (x - %s)(2x - %s)$, bạn An thực hiện các bước sau:\\\\- Bước 1: Chia cả hai vế của phương trình cho $(x - %s)$, ta được: $x + %s = 2x - %s$.\\\\- Bước 2: Chuyển vế, ta được: $x - 2x = -%s - %s$.\\\\- Bước 3: Thu gọn, ta được: $-x = -%s \\Rightarrow x = %s$.\\\\- Bước 4: Kết luận phương trình có nghiệm duy nhất là $x = %s$.\\\\Nhận xét nào sau đây đúng về bài làm của bạn An?" % (
            a, b, a, c, a, b, c, c, b, nghiem_con, nghiem_con, nghiem_con
        )
        da = "Bạn An sai ở Bước 1 vì chia cả hai vế cho nhân tử chứa ẩn $(x - %s)$ làm mất nghiệm $x = %s$." % (a, a)
        s = [
            "Bạn An giải hoàn toàn chính xác.",
            "Bạn An sai ở Bước 2 do chuyển vế đổi dấu nhầm.",
            "Bạn An sai ở Bước 3 vì tính toán sai phép trừ số nguyên."
        ]
        loigiai = "Bạn An đã chia cả hai vế của phương trình cho biểu thức chứa ẩn $(x - %s)$ mà chưa xét trường hợp $x - %s = 0$, dẫn đến làm mất nghiệm $x = %s$.\\\\Cách giải đúng là chuyển vế và đặt nhân tử chung:\\\\$(x - %s)(x + %s) - (x - %s)(2x - %s) = 0$\\\\$(x - %s)[(x + %s) - (2x - %s)] = 0$\\\\$(x - %s)(%s - x) = 0$\\\\Suy ra $x - %s = 0$ hoặc $%s - x = 0$, tìm được hai nghiệm là $x = %s$ và $x = %s$." % (
            a, a, a, a, b, a, c, a, b, c, a, nghiem_con, a, nghiem_con, a, nghiem_con
        )

    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)

    da_d = ('\\True ' + str(da))
    list_1 = [da_d, str(das1), str(das2), str(das3)]
    random.shuffle(list_1)

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
