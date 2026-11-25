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


def bt_dang18_p4_b2_c5_ds8(self):
    # Dạng 18 (Tự luận - Vận dụng thực tế): Phân tích dữ liệu môi trường và lựa chọn biểu đồ đa mục tiêu
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        p1, p2, p3, p4 = 42, 28, 18, 12
        ang_gt = Decimal(str(p1 * 360)) / Decimal('100')
        s_ang_gt = str(ang_gt.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace(".", ",")
        
        tikz_a = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt] (0,0) circle (1.5);
        \\draw[line width=1pt] (0,0) -- (0:1.5) (0,0) -- (151.2:1.5) (0,0) -- (252:1.5) (0,0) -- (316.8:1.5);
        \\node at (75.6:0.9) {$42\\%$};
        \\node at (201.6:0.9) {$28\\%$};
        \\node at (284.4:0.95) {$18\\%$};
        \\node at (338.4:1.05) {$12\\%$};
        \\node[right] at (1.9, 0.8) {Giao thông vận tải: $42\\%$};
        \\node[right] at (1.9, 0.25) {Xây dựng: $28\\%$};
        \\node[right] at (1.9, -0.3) {Sản xuất công nghiệp: $18\\%$};
        \\node[right] at (1.9, -0.85) {Sinh hoạt dân cư: $12\\%$};
        \\end{tikzpicture}
        \\end{center}""" )
        
        noidungcauhoi = ("""Sở Tài nguyên và Môi trường một thành phố thực hiện hai khảo sát:\\\\
        - \\textbf{Khảo sát 1:} Đo nồng độ bụi mịn $\\text{PM}_{2,5}$ trung bình hằng tháng (đơn vị: $\\mu\\text{g/m}^3$) tại trạm quan trắc trung tâm liên tục trong $12$ tháng của năm $2025$.\\\\
        - \\textbf{Khảo sát 2:} Phân tích thành phần nguồn phát thải bụi mịn tại thành phố gồm: Giao thông vận tải ($42\\%$), Xây dựng ($28\\%$), Sản xuất công nghiệp ($18\\%$) và Sinh hoạt dân cư ($12\\%$).\\\\
        a) Với mỗi khảo sát trên, hãy chọn loại biểu đồ phù hợp nhất và giải thích lí do lựa chọn.\\\\
        b) Vẽ biểu đồ cho Khảo sát 2 và tính số đo góc ở tâm của hình quạt biểu diễn nguồn phát thải từ Giao thông vận tải.""" )
        
        loigiai = ("""\\begin{enumEX}[a)]{1}
        \\item - \\textbf{Khảo sát 1} nên dùng \\textbf{biểu đồ đoạn thẳng} vì mục đích là theo dõi sự thay đổi (xu hướng tăng, giảm) của nồng độ bụi mịn qua $12$ mốc thời gian liên tục trong năm.\\\\
        - \\textbf{Khảo sát 2} nên dùng \\textbf{biểu đồ hình quạt tròn} vì mục đích là biểu diễn cơ cấu tỉ lệ phần trăm của từng nguồn phát thải trong tổng thể ($100\\%%$).
        \\item Số đo góc ở tâm của hình quạt biểu diễn nguồn phát thải từ Giao thông vận tải là:
        $$360^\\circ \\cdot 42\\%% = %s^\\circ.$$
        Biểu đồ hình quạt tròn biểu diễn Khảo sát 2:%s
        \\end{enumEX}""" % (s_ang_gt, tikz_a))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
