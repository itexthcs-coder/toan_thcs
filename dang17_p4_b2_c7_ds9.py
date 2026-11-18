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


def bt_dang17_p4_b2_c7_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        cp_nc = random.choice([240000, 300000])
        tong_cp = cp_nc * 3

        hinh_quat = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt] (0,0) circle (2);\n'
            '\\draw[line width=1pt] (0,0) -- (0:2);\n'
            '\\draw[line width=1pt] (0,0) -- (180:2);\n'
            '\\draw[line width=1pt] (0,0) -- (300:2);\n'
            '\\node at (90:1.15) {$180^\\circ$};\n'
            '\\node at (240:1.15) {$x^\\circ$};\n'
            '\\node at (330:1.15) {$y^\\circ$};\n'
            '\\node[right] at (2.3, 0.7) {Nguyên vật liệu: $180^\\circ$};\n'
            '\\node[right] at (2.3, 0.0) {Nhân công: $x^\\circ$};\n'
            '\\node[right] at (2.3, -0.7) {Chi phí khác: $y^\\circ$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Biểu đồ hình quạt tròn dưới đây biểu diễn cơ cấu chi phí sản xuất một sản phẩm gồm 3 khoản:%s'
            'Biết chi phí Nhân công gấp $2$ lần Chi phí khác và chi phí Nhân công là $%s$ đồng.\\\\ '
            'a) Tìm số đo góc $x, y$ và lập bảng tần số tương đối cơ cấu chi phí (làm tròn đến hàng phần mười).\\\\ '
            'b) Tính tổng chi phí sản xuất một sản phẩm.'
        ) % (hinh_quat, cp_nc)

        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Ta có $x + y = 360 - 180 = 180$. Thay $x = 2y$ ta được $3y = 180 \\Leftrightarrow y = 60$, suy ra $x = 120$.\\\\ '
            'Tần số tương đối các khoản chi phí: Nguyên vật liệu ($50,0\\%%$), Nhân công ($\\frac{120^\\circ}{360^\\circ} \\cdot 100\\%% \\approx 33,3\\%%$), Chi phí khác ($\\frac{60^\\circ}{360^\\circ} \\cdot 100\\%% \\approx 16,7\\%%$).\\\\ '
            '\\begin{center}\n'
            '\\begin{tabular}{|l|c|c|c|}\n'
            '\\hline\n'
            'Khoản chi phí & Nguyên vật liệu & Nhân công & Chi phí khác \\\\ \n'
            '\\hline\n'
            'Tần số tương đối & $50,0\\%%$ & $33,3\\%%$ & $16,7\\%%$ \\\\ \n'
            '\\hline\n'
            '\\end{tabular}\n'
            '\\end{center}\n'
            '\\item Vì chi phí Nhân công ứng với góc ở tâm $120^\\circ = \\frac{1}{3}$ đường tròn nên tổng chi phí sản xuất một sản phẩm là: $%s \\cdot 3 = %s$ (đồng).\n'
            '\\end{enumEX}'
        ) % (cp_nc, tong_cp)
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
