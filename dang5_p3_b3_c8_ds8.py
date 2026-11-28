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


def bt_dang5_p3_b3_c8_ds8(self):
    # Dạng 5: Ước lượng xác suất thực nghiệm qua bảng dữ liệu hai chiều khuyết số liệu
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n8 = random.choice([120, 150, 160, 180])
        h8 = random.randint(int(0.65 * n8), int(0.8 * n8))
        n9 = random.choice([150, 160, 200, 250])
        # Chọn h9 chia hết cho n9 // 10 để kết quả là số thập phân đẹp 1-2 chữ số
        p_chon = random.choice([0.72, 0.75, 0.76, 0.8, 0.84, 0.85])
        while (Decimal(str(p_chon)) * Decimal(n9)) % 1 != 0:
            p_chon = random.choice([0.72, 0.75, 0.76, 0.8, 0.84, 0.85])
        h9 = int(Decimal(str(p_chon)) * Decimal(n9))
        tong_n = n8 + n9
        tong_h = h8 + h9

        kq = (Decimal(h9) / Decimal(n9)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).rstrip('0').rstrip('.').replace('.', ',')

        noidungcauhoi = ('''Khảo sát mức độ hài lòng về căn-tin của học sinh khối 8 và khối 9 tại một trường THCS thu được bảng số liệu sau (một số ô bị mờ):\\
\\begin{center}
\\begin{tabular}{|l|c|c|}
\\hline
Đối tượng & Số học sinh khảo sát & Số học sinh hài lòng \\\\
\\hline
Khối 8 & $%s$ & $%s$ \\\\
\\hline
Khối 9 & ? & ? \\\\
\\hline
Tổng cộng & $%s$ & $%s$ \\\\
\\hline
\\end{tabular}
\\end{center}
Chọn ngẫu nhiên $1$ học sinh khối 9 được khảo sát, hãy ước lượng xác suất để học sinh đó hài lòng (viết kết quả dưới dạng số thập phân).'''
                         % (n8, h8, tong_n, tong_h))

        loigiai = ('''Từ bảng số liệu tổng cộng, ta tính được số học sinh khối 9 được khảo sát là: $%s - %s = %s$ (học sinh).\\\\
Số học sinh khối 9 hài lòng là: $%s - %s = %s$ (học sinh).\\\\
Xác suất thực nghiệm của biến cố $E$: ``Học sinh khối 9 được chọn hài lòng'' là $\\dfrac{%s}{%s} = %s$.\\\\
Vậy xác suất của biến cố $E$ được ước lượng là $%s$.'''
                   % (tong_n, n8, n9, tong_h, h8, h9, h9, n9, kq_str, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
