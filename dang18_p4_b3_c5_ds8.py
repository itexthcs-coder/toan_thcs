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

def bt_dang18_p4_b3_c5_ds8(self):
    # Dạng 18: Đánh giá sự thay đổi hình dạng biểu đồ đoạn thẳng khi thay đổi đơn vị đo lường
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        t22, t23, t24, t25 = 1200000, 1350000, 1500000, 1800000
        tr22, tr23, tr24, tr25 = Decimal('1.2'), Decimal('1.35'), Decimal('1.5'), Decimal('1.8')
        
        # Biểu đồ 1: nghìn tấn -> 1800 nghìn tấn, mỗi 1 cm = 200 nghìn tấn -> cao 9 cm
        # Biểu đồ 2: triệu tấn -> 1,8 triệu tấn, mỗi 1 cm = 0,5 triệu tấn -> cao 3,6 cm
        
        noidungcauhoi = ('Một công ty vận tải biển thống kê khối lượng hàng hóa thông qua cảng trong $4$ năm: Năm $2022$ đạt $1\\,200\\,000$ tấn; Năm $2023$ đạt $1\\,350\\,000$ tấn; Năm $2024$ đạt $1\\,500\\,000$ tấn; Năm $2025$ đạt $1\\,800\\,000$ tấn.\n' +
                         'a) Hãy quy đổi các số liệu trên sang đơn vị triệu tấn và lập bảng thống kê tương ứng.\\\n' +
                         'b) Nếu vẽ hai biểu đồ đoạn thẳng có cùng độ rộng trên trục ngang: Biểu đồ $1$ dùng đơn vị nghìn tấn với trục đứng chia mỗi $1\\text{ cm}$ ứng với $200$ nghìn tấn; Biểu đồ $2$ dùng đơn vị triệu tấn với trục đứng chia mỗi $1\\text{ cm}$ ứng với $0,5$ triệu tấn. Hãy so sánh độ cao của điểm biểu diễn năm $2025$ trên hai biểu đồ và giải thích vì sao độ dốc của đường biểu diễn ở Biểu đồ $1$ lại lớn hơn Biểu đồ $2$.')
        
        loigiai = ('\\begin{enumEX}[a)]{1}\n' +
                   '\\item Quy đổi sang đơn vị triệu tấn ($1$ triệu tấn $= 1\\,000\\,000$ tấn):\\\\' +
                   '- Năm $2022$: $1,2$ triệu tấn; Năm $2023$: $1,35$ triệu tấn; Năm $2024$: $1,5$ triệu tấn; Năm $2025$: $1,8$ triệu tấn.\\\\' +
                   'Bảng thống kê:\\\\' +
                   '\\begin{center}\n' +
                   '\\begin{tabular}{|l|c|c|c|c|}\n' +
                   '\\hline\n' +
                   '\\textbf{Năm} & $2022$ & $2023$ & $2024$ & $2025$ \\\\ \\hline\n' +
                   '\\textbf{Khối lượng (triệu tấn)} & $1,2$ & $1,35$ & $1,5$ & $1,8$ \\\\ \\hline\n' +
                   '\\end{tabular}\n' +
                   '\\end{center}\n' +
                   '\\item Đổi $1\\,800\\,000$ tấn $= 1\\,800$ nghìn tấn $= 1,8$ triệu tấn.\\\\' +
                   '- Trên Biểu đồ $1$, độ cao của điểm biểu diễn năm $2025$ là: $\\dfrac{1\\,800}{200} = 9\\text{ (cm)}$.\\\\' +
                   '- Trên Biểu đồ $2$, độ cao của điểm biểu diễn năm $2025$ là: $\\dfrac{1,8}{0,5} = 3,6\\text{ (cm)}$.\\\\' +
                   'Vậy độ cao điểm biểu diễn năm $2025$ trên Biểu đồ $1$ gấp $\\dfrac{9}{3,6} = 2,5$ lần trên Biểu đồ $2$. Đường biểu diễn ở Biểu đồ $1$ có độ dốc lớn hơn vì tỉ lệ chia khoảng trên trục đứng của Biểu đồ $1$ ($1\\text{ cm}$ ứng với $0,2$ triệu tấn) được phóng to gấp $2,5$ lần so với Biểu đồ $2$ ($1\\text{ cm}$ ứng với $0,5$ triệu tấn) trong khi độ rộng trục ngang giữ nguyên.\n' +
                   '\\end{enumEX}'
                   )

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
